from pycades_api.signed_data_processor import SignedDataProcessor
from pycades_engine import pycades_engine
from models_types import ResponseModel


def verify_signature_by_hash(signed_message: str, hash: str) -> ResponseModel:
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

        return ResponseModel(
            is_valid=True,
            data=SignedDataProcessor(signed_data=signedData).signing_structure,
        )
    except Exception as error:
        print("Ошибка при вызове метода verify_signature_by_hash", error)
        return ResponseModel(is_valid=False, data=None)
