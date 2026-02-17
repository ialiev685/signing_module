from fastapi import UploadFile, APIRouter
from typing import Annotated
import base64
from libs.decode_detached_signature import DecodeDetachedSignature
from libs.convert_file_to_base64 import convert_file_to_base64
from pycades_api import create_hash_by_base64, verify_signature_by_hash
import os

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
    summary="Данные открепленной подписи",
)
async def decoded_signature():
    decodedDetachedSignature = DecodeDetachedSignature()

    return {"data": ""}
