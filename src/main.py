import pycades

from fastapi import FastAPI

app = FastAPI()

# print("pycades импортирован успешно, версия:", pycades.ModuleVersion())


@app.get("/")
async def root():
    return {"message": "Hello World"}
