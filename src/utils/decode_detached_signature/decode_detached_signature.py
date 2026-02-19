from pyasn1.codec.der import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315, rfc5280  # type: ignore

from utils.decode_detached_signature.decode_certificate_attributes import (
    DecodeCertificateAttributes,
)  #
from ..oid_configs import OID_SIGNED_DATA
from ..action_models import CertificatesChainsModel, IssuerModel
from .convert_integer_to_hex import convert_integer_to_hex

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
    def certificates_chain(self) -> list[CertificatesChainsModel]:
        certificates_chain_list: list[CertificatesChainsModel] = []

        if self.signed_data:
            try:
                certificates = self.signed_data["certificates"]  # list
                for cert in certificates:
                    serial_number = convert_integer_to_hex(
                        cert["certificate"]["tbsCertificate"]["serialNumber"]
                    )

                    issuer_certificate = DecodeCertificateAttributes(
                        certificate=cert["certificate"]["tbsCertificate"]["issuer"]
                    )
                    subject_certificate = DecodeCertificateAttributes(
                        certificate=cert["certificate"]["tbsCertificate"]["subject"]
                    )

                    certificates_chain_list.append(
                        CertificatesChainsModel(
                            issuer=issuer_certificate.certificate_info,
                            subject=subject_certificate.certificate_info,
                            serial_number=serial_number,
                        )
                    )
            except KeyError as error:
                print("Ошибка при обращении к методу 'certificates_chain': ", error)

        return certificates_chain_list

    @property
    def issuer(self) -> list[IssuerModel]:
        signer_list: list[IssuerModel] = []
        if self.signed_data:
            try:
                signer_infos = self.signed_data["signerInfos"]
                for signer in signer_infos:
                    serial_number = convert_integer_to_hex(
                        signer["sid"]["issuerAndSerialNumber"]["serialNumber"]
                    )

                    issuer_certificate = DecodeCertificateAttributes(
                        certificate=signer["sid"]["issuerAndSerialNumber"]["issuer"]
                    )
                    signer_list.append(
                        IssuerModel(
                            issuer=issuer_certificate.certificate_info,
                            serial_number=serial_number,
                        )
                    )

            except KeyError as error:
                print("Ошибка при обращении к методу 'signer': ", error)

        return signer_list
