from fastapi import UploadFile
import base64


async def convert_file_to_base64(file: UploadFile) -> str:
    content = await file.read()
    file_base64 = base64.b64encode(content).decode("utf-8")
    return file_base64
