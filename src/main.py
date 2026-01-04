from fastapi import FastAPI
from core import pycades_engine

app = FastAPI()


@app.get("/")
async def root():

    return {"result": "hello world"}
