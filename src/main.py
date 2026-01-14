from fastapi import FastAPI, UploadFile
from routes import router


app = FastAPI()
app.include_router(router)
