from pyasn1.codec.der import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315  # type: ignore

# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280  #

from ..oid_configs import SUBJECT_OIDS
from ..action_models import SubjectInfoModel, SubjectDataModel


class DecodeCertificate:
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
