from pydantic import BaseModel, ConfigDict, AliasGenerator
from pydantic.alias_generators import to_snake, to_camel
from typing import Optional, List


class AttributeValueModel(BaseModel):
    oid: str
    translation: str
    name_code: str
    value: str


class ResponseDataModel(BaseModel):
    is_success: bool
    data: list[AttributeValueModel] | None


class BaseAliasModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=AliasGenerator(
            validation_alias=to_camel, serialization_alias=to_snake
        ),
    )


class CertificateInfoModel(BaseAliasModel):
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


class SigningStructureModel(BaseAliasModel):
    certificates_chain: Optional[List[CertificateInfoModel]] = None
    issuer: Optional[List[SignersModel]] = None
    signature_timestamp_time: Optional[str] = None
    signing_time: Optional[str] = None


class ResponseModel(BaseAliasModel):
    is_valid: bool
    data: Optional[SigningStructureModel] = None
