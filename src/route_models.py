from pydantic import BaseModel
from models_types import CertificatesChainsModel, IssuerModel


class DecodedSignature(BaseModel):
    certificate_chain: list[CertificatesChainsModel]
    issuer: list[IssuerModel]
    signing_time: str | None
