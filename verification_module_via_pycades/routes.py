from fastapi import UploadFile, APIRouter, status, HTTPException, Body
from typing import Annotated
import base64
from models_types import (
    CertificateInfoModel,
    ResponseModel,
    RemoveDataModel,
    ResponseDataModel,
)
from fastapi.responses import JSONResponse
from utils.convert_file_to_base64 import convert_file_to_base64
from pycades_api import (
    create_hash_by_base64,
    verify_signature_by_hash,
    get_certificates_from_store,
    set_certificates_from_store,
    remove_certificate_from_store,
)


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
    response_model=ResponseModel,
)
async def verify_signature(
    document: Annotated[UploadFile, "Загрузите подписанный документ"],
    detached_signature: Annotated[UploadFile, "Загрузите открепленную подпись"],
):
    if not check_required_files([document, detached_signature]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Отсутствуют файл(ы)"
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


@router.get(
    "/get_root_certificates",
    summary="Корневые сертифкаты",
    status_code=status.HTTP_200_OK,
    response_model=ResponseDataModel[list[CertificateInfoModel]],
    responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ResponseDataModel}},
)
async def get_root_certificates():

    certificates = get_certificates_from_store(store_name="mRoot")
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


# @router.post(
#     "/set_personal_certificate",
#     summary="Загрузить сертифкат",
#     status_code=status.HTTP_200_OK,
#     # response_model=ResponseModel,
# )
# async def set_personal_certificates(
#     certificate: Annotated[UploadFile, "Загрузите подписанный документ"],
# ):
#     content = await certificate.read()
#     return set_certificates_from_store(file=content, filename=certificate.filename)


# @router.post(
#     "/remove_certificate",
#     summary="Удалить сертифкат",
#     status_code=status.HTTP_200_OK,
#     # response_model=ResponseModel,
# )
# async def remove_certificate(
#     request: Annotated[RemoveDataModel, Body()],
# ):

#     return remove_certificate_from_store(thumbprint=request.thumbprint)
