from fastapi import UploadFile, APIRouter, status, File
from pydantic import BaseModel
from typing import Annotated
import base64
from models_types import CertificateInfoModel, VerificationModel, ResponseDataModel
from fastapi.responses import JSONResponse
from utils.convert_file_to_base64 import convert_file_to_base64
from pycades_api import (
    create_hash_by_base64,
    verify_signature_by_hash,
    get_certificates_from_store,
    set_certificates_from_store,
    remove_certificate_from_store,
)
from enum import Enum


router = APIRouter(prefix="/api/v1")


def check_required_files(files: list[UploadFile]):
    return all(file.size and file.filename for file in files)


@router.post(
    "/create_hash",
    summary="Создание хеша документа",
)
async def create_hash(
    file: Annotated[UploadFile, "Загрузите документ"],
):
    content = await file.read()
    file_base64 = base64.b64encode(content).decode("utf-8")
    hash = create_hash_by_base64(file_base64)

    return {"file": hash}


@router.post(
    "/verify_signature",
    summary="Проверка подписи",
    status_code=status.HTTP_200_OK,
    response_model=ResponseDataModel[VerificationModel],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ResponseDataModel[VerificationModel]
        },
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"model": ResponseDataModel},
    },
)
async def verify_signature(
    document: Annotated[UploadFile, File(description="Загрузите подписанный документ")],
    detached_signature: Annotated[
        UploadFile, File(description="Загрузите открепленную подпись")
    ],
):
    if not check_required_files([document, detached_signature]):
        raise JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                **ResponseDataModel(
                    has_error=True, error="Отсутствуют файл(ы)"
                ).model_dump()
            },
        )
    document_base64, _ = await convert_file_to_base64(document)
    hash = create_hash_by_base64(document_base64)
    detached_signature_content_base64, content_bytes = await convert_file_to_base64(
        detached_signature
    )

    result = verify_signature_by_hash(
        signed_message_base64=detached_signature_content_base64,
        hash=hash,
        signed_message_bytes=content_bytes,
    )

    return result


class StoreNamePathModel(str, Enum):
    m_root = "mRoot"
    m_ca = "mCA"


@router.get(
    "/get_root_certificates/{store_name}",
    summary="Сертифкаты",
    status_code=status.HTTP_200_OK,
    response_model=ResponseDataModel[list[CertificateInfoModel]],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ResponseDataModel[None]},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"model": ResponseDataModel},
    },
)
async def get_root_certificates(store_name: StoreNamePathModel):
    certificates = get_certificates_from_store(store_name=store_name.value)
    if certificates.has_error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                **ResponseDataModel(
                    has_error=True, error=str(certificates.error)
                ).model_dump()
            },
        )
    return certificates


class SetCertificatePathModel(BaseModel):
    certificate: UploadFile


@router.post(
    "/set_certificate/{store_name}",
    summary="Загрузить сертифкат",
    status_code=status.HTTP_200_OK,
    response_model=ResponseDataModel[CertificateInfoModel],
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ResponseDataModel[None]},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"model": ResponseDataModel},
    },
)
async def set_personal_certificates(
    store_name: StoreNamePathModel,
    certificate: Annotated[UploadFile, File(description="Загрузите файл")],
):
    if not check_required_files([certificate]):
        raise JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                **ResponseDataModel(
                    has_error=True, error="Отсутствуют файл(ы)"
                ).model_dump()
            },
        )
    content = await certificate.read()
    result = set_certificates_from_store(
        file=content, filename=certificate.filename, store_name=store_name
    )
    if result.has_error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                **ResponseDataModel(
                    has_error=True, error=str(result.error)
                ).model_dump()
            },
        )
    return set_certificates_from_store(
        file=content, filename=certificate.filename, store_name=store_name
    )


class RemoveCertificateBodyModel(BaseModel):
    thumbprint: str
    store_name: StoreNamePathModel


@router.post(
    "/remove_certificate",
    summary="Удалить сертифкат",
    status_code=status.HTTP_200_OK,
    response_model=ResponseDataModel[CertificateInfoModel],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ResponseDataModel[None]},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"model": ResponseDataModel},
    },
)
async def remove_certificate(
    request: RemoveCertificateBodyModel,
):
    result = remove_certificate_from_store(
        thumbprint=request.thumbprint, store_name=request.store_name
    )
    if result.has_error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                **ResponseDataModel(
                    has_error=True, error=str(result.error)
                ).model_dump()
            },
        )
    return result
