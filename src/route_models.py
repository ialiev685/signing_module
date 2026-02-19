from pydantic import BaseModel
from utils.action_models import CertificateInfoModel


class DecodedSignature(BaseModel):
    signers_certificate_chain: list[CertificateInfoModel]
