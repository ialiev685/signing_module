from pydantic import BaseModel
from utils.action_models import CertificatesChainsModel


class DecodedSignature(BaseModel):
    signers_certificate_chain: list[CertificatesChainsModel]
