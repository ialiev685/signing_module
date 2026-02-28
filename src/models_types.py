from pydantic import BaseModel
from typing import Optional, List


class AttributeValueModel(BaseModel):
    oid: str
    translation: str
    name_code: str
    value: str


class ResponseDataModel(BaseModel):
    is_success: bool
    data: list[AttributeValueModel] | None


class IssuerModel(BaseModel):
    issuer: ResponseDataModel
    serial_number: str | None


class CertificateInfoModel(BaseModel):
    subject_name: Optional[str] = None
    issuer_name: str
    thumbprint: Optional[str] = None
    valid_from_date: Optional[str] = None
    valid_to_date: Optional[str] = None
    serial_number: Optional[str] = None
    oids: Optional[List[str]] = None


class SignersModel(CertificateInfoModel):
    signature_timestamp_time: Optional[str] = None
    signing_time: Optional[str] = None


class SigningStructureModel(BaseModel):
    certificates_chain: Optional[List[CertificateInfoModel]] = None
    issuer: Optional[List[SignersModel]] = None
    signature_timestamp_time: Optional[str] = None
    signing_time: Optional[str] = None


class ResponseModel(BaseModel):
    is_valid: bool
    data: Optional[SigningStructureModel] = None
