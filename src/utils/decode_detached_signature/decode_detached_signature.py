from pyasn1.codec.der import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315  # type: ignore

from utils.decode_detached_signature.decode_certificate import DecodeCertificate  #
from ..oid_configs import OID_SIGNED_DATA
from ..action_models import CertificateInfoModel


path_signature = "src/test_signature/test_detached_signature.sig"


class DecodeDetachedSignature:
    signed_data: rfc5652.SignedData = None

    def __init__(self):

        with open(path_signature, "rb") as file:
            try:
                decoded_value, _ = decoder.decode(
                    file.read(), asn1Spec=rfc5652.ContentInfo()
                )

                if (
                    isinstance(decoded_value, rfc5652.ContentInfo)
                    and str(decoded_value["contentType"]) == OID_SIGNED_DATA
                ):
                    signed_data, _ = decoder.decode(
                        decoded_value["content"], rfc5652.SignedData()
                    )
                    self.signed_data = signed_data

            except Exception as error:
                print("Ошибка при декодировании подписи (signed_data): ", error)

    @property
    def signers_certificate_chain(self) -> list[CertificateInfoModel]:
        certificates_chain: list[CertificateInfoModel] = []

        if self.signed_data:
            certificates = self.signed_data["certificates"]  # list
            for cert in certificates:
                certificate = DecodeCertificate(certificate=cert)
                certificates_chain.append(certificate.certificate_info)

        return certificates_chain
