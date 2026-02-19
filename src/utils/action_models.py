from pydantic import BaseModel


class SubjectInfoModel(BaseModel):
    oid: str
    translation: str
    name_code: str
    value: str


class SubjectDataModel(BaseModel):
    is_success: bool
    data: list[SubjectInfoModel]
