from fastapi import FastAPI, UploadFile
from api.create_hash import router


app = FastAPI()
app.include_router(router)
