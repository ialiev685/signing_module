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

    # store = pycades_engine.Store()
    # store.Open(
    #     pycades_engine.CAPICOM_CURRENT_USER_STORE,
    #     pycades_engine.CAPICOM_ROOT_STORE,
    #     # pycades_engine.CAPICOM_CA_STORE,
    #     pycades_engine.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED,
    # )
    # print(f"Cертификатов: {store.Certificates.Count}")

    # certs = store.Certificates

    # for i in range(certs.Count):
    #     cert = certs.Item(i + 1)
    #     subject = str(cert.SubjectName)
    #     issuer = str(cert.IssuerName)

    hashed_data = pycades_engine.HashedData()
    hashed_data.Algorithm = pycades_engine.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256
    hashed_data.SetHashValue(hash)

    signedData = pycades_engine.SignedData()

    signingTypeCode = signedData.GetMsgType(signed_message)

    try:
        signedData.VerifyHash(hashed_data, signed_message, signingTypeCode)
        print("result", signedData)
        return {"valid": True}
    except Exception as error:
        print("error", error)
        return {"valid": False}


# Certificates
[
    "Count",
    "Find",
    "Item",
    "__class__",
    "__delattr__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
]
# signedData
[
    "AdditionalStore",
    "Certificates",
    "CoSign",
    "CoSignCades",
    "CoSignHash",
    "Content",
    "ContentEncoding",
    "EnhanceCades",
    "GetMsgType",
    "IsMsgType",
    "Sign",
    "SignCades",
    "SignHash",
    "Signers",
    "Verify",
    "VerifyCades",
    "VerifyHash",
    "__class__",
    "__delattr__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
]
