from pydantic import BaseModel


class AttributeValueModel(BaseModel):
    oid: str
    translation: str
    name_code: str
    value: str


class ResponseDataModel(BaseModel):
    is_success: bool
    data: list[AttributeValueModel] | None


class CertificatesChainsModel(BaseModel):
    subject: ResponseDataModel
    issuer: ResponseDataModel
    valid_from_date: str
    valid_to_date: str
    serial_number: str | None


class IssuerModel(BaseModel):
    issuer: ResponseDataModel
    serial_number: str | None
