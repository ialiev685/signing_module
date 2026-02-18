from pydantic import BaseModel, Field


class SubjectInfoModel(BaseModel):
    oid: str
    translation: str
    nameCode: str
    value: str


class SubjectDataModel(BaseModel):
    is_success: bool
    data: list[SubjectInfoModel]
