from pydantic import BaseModel
from utils.action_models import SubjectDataModel


class DecodedSignature(BaseModel):
    signers_certificate_chain: list[SubjectDataModel]
