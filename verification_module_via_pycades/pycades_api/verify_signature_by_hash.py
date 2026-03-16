from pycades_api.signed_data_processor import SignedDataProcessor
from pycades_engine import pycades_engine
from models_types import VerificationModel, ResponseDataModel
from .parse_crypto_error_code import parse_crypto_error_code
from services.decode_detached_signature import DecodeDetachedSignature


def verify_signature_by_hash(
    signed_message_base64: str, hash: str, signed_message_bytes: bytes
) -> ResponseDataModel[VerificationModel]:
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

    signingTypeCode = signedData.GetMsgType(signed_message_base64)

    try:
        signedData.VerifyHash(hashed_data, signed_message_base64, signingTypeCode)

        return ResponseDataModel(
            data=VerificationModel(
                is_valid=True,
                result=SignedDataProcessor(signed_data=signedData).signing_structure,
            )
        )
    except Exception as error:
        print("Подпись невалидна", error)
        decoded_detached_signature = DecodeDetachedSignature(
            signature_base64=signed_message_base64,
            signature_bytes=signed_message_bytes,
        )

        error_from_decode = (
            "\n" + "\n".join(decoded_detached_signature.error)
            if len(decoded_detached_signature.error) > 0
            else ""
        )

        return ResponseDataModel(
            has_error=True,
            error=parse_crypto_error_code(str(error)) + error_from_decode,
            data=VerificationModel(
                is_valid=False,
                result=decoded_detached_signature.signing_structure,
            ),
        )

    # через pycades вызов данных стора не отрабатывают корректно

    # store = pycades_engine.Store()
    # store.Open(
    #     pycades_engine.CAPICOM_CURRENT_USER_STORE,
    #     # pycades_engine.CAPICOM_ROOT_STORE,
    #     # pycades_engine.CAPICOM_CA_STORE,
    #     pycades_engine.CAPICOM_MY_STORE,
    #     pycades_engine.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED,
    # )
    # print("!!!", store.Certificates.Count)
    # certs = store.Certificates

    # for i in range(certs.Count):
    #     cert = certs.Item(i + 1)
    #     subject = str(cert.SubjectName)
    #     issuer = str(cert.IssuerName)
