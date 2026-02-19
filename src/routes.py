from fastapi import UploadFile, APIRouter, status
from typing import Annotated
import base64
from utils.decode_detached_signature.decode_detached_signature import (
    DecodeDetachedSignature,
)
from utils.convert_file_to_base64 import convert_file_to_base64
from pycades_api import create_hash_by_base64, verify_signature_by_hash
from route_models import DecodedSignature


router = APIRouter(prefix="/api/v1")


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
)
async def verify_signature(
    document: Annotated[UploadFile, "Загрузите подписанный документ"],
    detached_signature: Annotated[UploadFile, "Загрузите открепленную подпись"],
):
    document_content = await convert_file_to_base64(document)
    hash = create_hash_by_base64(document_content)
    detached_signature_content = await convert_file_to_base64(detached_signature)

    result = verify_signature_by_hash(
        signed_message=detached_signature_content, hash=hash
    )

    return {"result": result["valid"]}


@router.get(
    "/decoded_signature",
    summary="Данные открепленной подписи (временный)",
    response_model=DecodedSignature,
    status_code=status.HTTP_200_OK,
)
async def decoded_signature():
    decodedDetachedSignature = DecodeDetachedSignature()

    return {
        "signers_certificate_chain": decodedDetachedSignature.signers_certificate_chain
    }
