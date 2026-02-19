from pyasn1.codec.der import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315  # type: ignore

# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280  #

from .oid_configs import SUBJECT_OIDS, OID_SIGNED_DATA
from .action_models import SubjectInfoModel, SubjectDataModel


path_signature = "src/test_signature/test_detached_signature.sig"
out_path_logs = "src/test_signature/logs.txt"


class Certificate:
    certificate: rfc5280.TBSCertificate

    def __init__(self, certificate: rfc5652.CertificateChoices):

        try:
            self.certificate = certificate["certificate"]["tbsCertificate"]
        except KeyError as error:
            print("Ошибка при получении общих данных сертификата: ", error)

    @property
    def subject(self) -> SubjectDataModel:

        subject_value: list[SubjectInfoModel] = []

        try:
            subject_rdn_attributes = self.certificate["subject"]["rdnSequence"]
            if isinstance(subject_rdn_attributes, rfc5280.RDNSequence):
                for rdn in subject_rdn_attributes:
                    for attribute in rdn:
                        value_encoded = attribute["value"]
                        type = str(attribute["type"])
                        value_parsed, _ = decoder.decode(value_encoded)
                        if type in SUBJECT_OIDS:
                            subject_value.append(
                                SubjectInfoModel(
                                    **SUBJECT_OIDS[type], value=str(value_parsed)
                                )
                            )

            return SubjectDataModel(is_success=True, data=subject_value)
        except KeyError as error:
            print("Ошибка при получении данных субьекта сертификата: ", error)
            return SubjectDataModel(is_success=False, data=[])


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
    def signers_certificate_chain(self) -> list[SubjectDataModel]:
        certificates_chain: list[SubjectDataModel] = []

        if self.signed_data:
            certificates = self.signed_data["certificates"]  # list
            for cert in certificates:
                certificate = Certificate(certificate=cert)
                certificates_chain.append(certificate.subject)

        return certificates_chain
