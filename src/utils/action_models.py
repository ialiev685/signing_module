from pydantic import BaseModel


class AttributeValueModel(BaseModel):
    oid: str
    translation: str
    name_code: str
    value: str


class CertificateInfoModel(BaseModel):
    subject: list[AttributeValueModel] | None
    issuer: list[AttributeValueModel] | None
