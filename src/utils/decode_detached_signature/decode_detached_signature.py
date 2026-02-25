from pyasn1.codec.ber import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315, rfc5280  # type: ignore

from utils.decode_detached_signature.decode_certificate_attributes import (
    DecodeCertificateAttributes,
)  #
from ..oid_configs import OID_SIGNED_DATA, SIGNING_TIME_OID
from ..action_models import CertificatesChainsModel, IssuerModel
from .convert_integer_to_hex import convert_integer_to_hex
from .format_asn1_time import format_asn1_time

# path_signature = "src/test_signature/test_detached_signature.sig"
path_signature = "src/test_signature/test1_pdf.p7s"


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
                    and decoded_value["contentType"] == rfc5652.id_signedData
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
                    date = cert["certificate"]["tbsCertificate"]["validity"]
                    valid_from_date = format_asn1_time(date["notBefore"]["utcTime"])
                    valid_to_date = format_asn1_time(date["notAfter"]["utcTime"])

                    certificates_chain_list.append(
                        CertificatesChainsModel(
                            issuer=issuer_certificate.certificate_info,
                            subject=subject_certificate.certificate_info,
                            serial_number=serial_number,
                            valid_from_date=valid_from_date,
                            valid_to_date=valid_to_date,
                        )
                    )
            except KeyError as error:
                print("Ошибка при обращении к методу 'certificates_chain': ", error)

        return certificates_chain_list

    @property
    def issuer(self) -> list[IssuerModel]:
        issuer_list: list[IssuerModel] = []
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
                    issuer_list.append(
                        IssuerModel(
                            issuer=issuer_certificate.certificate_info,
                            serial_number=serial_number,
                        )
                    )

            except KeyError as error:
                print("Ошибка при обращении к методу 'issuer': ", error)

        return issuer_list

    @property
    def signing_time(self) -> str | None:
        value = None
        if self.signed_data:
            try:
                signer_infos = self.signed_data["signerInfos"]
                value_encoded = next(
                    (
                        attr["attrValues"]
                        for attr in signer_infos[0]["signedAttrs"]
                        if str(attr["attrType"]) == SIGNING_TIME_OID
                    ),
                    None,
                )
                if value_encoded:
                    value_decoded, _ = decoder.decode(value_encoded[0])
                    value = format_asn1_time(value_decoded)

            except KeyError as error:
                print("Ошибка при обращении к методу 'signing_time': ", error)

        return value
