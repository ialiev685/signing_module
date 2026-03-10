from fastapi import FastAPI, Request, status
from routes import router
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from models_types import ResponseDataModel

app = FastAPI()
app.include_router(router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("exc", exc._errors)
    error_item = exc._errors[0]
    error_message = (
        error_item["type"] + " " + error_item["loc"][1] + "-" + error_item["msg"]
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={**ResponseDataModel(has_error=True, error=error_message).model_dump()},
    )
