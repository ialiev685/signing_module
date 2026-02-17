from pycades_engine import pycades_engine
from typing import TypedDict


class ReturnVerifySignatureByHash(TypedDict):
    valid: bool


def verify_signature_by_hash(
    signed_message: str, hash: str
) -> ReturnVerifySignatureByHash:
    """
    Docstring для verify_signature_by_hash

    :param signed_message: Открепленная подпись в формате base64
    :type signed_message: str
    :param hash: Описание
    :type hash: хэш сумма подписанного файла
    """
    hashed_data = pycades_engine.HashedData()
    hashed_data.Algorithm = pycades_engine.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256
    hashed_data.SetHashValue(hash)

    signedData = pycades_engine.SignedData()

    signingTypeCode = signedData.GetMsgType(signed_message)

    try:
        result = signedData.VerifyHash(hashed_data, signed_message, signingTypeCode)
        return {"valid": True}
    except:

        return {"valid": False}
