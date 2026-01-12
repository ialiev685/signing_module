from fastapi import UploadFile, APIRouter
from core import pycades_engine
from typing import Annotated
import base64

router = APIRouter(prefix="/api")


@router.post(
    "/create_hash",
    summary="Создание хеша документа",
)
async def create_hash(
    file: Annotated[UploadFile, "Загрузите документ для подписи"],
):
    content = await file.read()
    file_base64 = base64.b64encode(content).decode("utf-8")

    hashed_data = pycades_engine.HashedData()
    hashed_data.Algorithm = pycades_engine.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256
    hashed_data.Hash(file_base64)

    return {"file": hashed_data.Value}
