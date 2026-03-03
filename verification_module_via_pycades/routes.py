from fastapi import UploadFile, APIRouter, status
from typing import Annotated
import base64
from models_types import ResponseModel
from utils.convert_file_to_base64 import convert_file_to_base64
from pycades_api import create_hash_by_base64, verify_signature_by_hash


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
    status_code=status.HTTP_200_OK,
    response_model=ResponseModel,
)
async def verify_signature(
    document: Annotated[UploadFile, "Загрузите подписанный документ"],
    detached_signature: Annotated[UploadFile, "Загрузите открепленную подпись"],
):
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
