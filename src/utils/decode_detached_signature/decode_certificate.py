from pyasn1.codec.der import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315  # type: ignore

# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280  #

from ..oid_configs import SUBJECT_OIDS
from ..action_models import AttributeValueModel, CertificateInfoModel


def parse_attributes_value(
    rdn_attributes: rfc5280.RDNSequence,
) -> list[AttributeValueModel]:
    values: list[AttributeValueModel] = []
    for rdn in rdn_attributes:
        for attribute in rdn:
            value_encoded = attribute["value"]
            type = str(attribute["type"])
            value_parsed, _ = decoder.decode(value_encoded)
            if type in SUBJECT_OIDS:
                values.append(
                    AttributeValueModel(**SUBJECT_OIDS[type], value=str(value_parsed))
                )
    return values


class DecodeCertificate:
    certificate: rfc5280.TBSCertificate

    def __init__(self, certificate: rfc5652.CertificateChoices):

        try:
            self.certificate = certificate["certificate"]["tbsCertificate"]
        except KeyError as error:
            print("Ошибка при получении общих данных сертификата: ", error)

    # -> CertificateDataModel
    @property
    def certificate_info(self):
        values = {"subject": None, "issuer": None}
        # получения данных издателя
        try:
            issuer_rdn_attributes = self.certificate["issuer"]["rdnSequence"]
            if isinstance(issuer_rdn_attributes, rfc5280.RDNSequence):
                values["issuer"] = parse_attributes_value(
                    rdn_attributes=issuer_rdn_attributes
                )
        except KeyError as error:
            print("Ошибка при получении данных издателя сертификата: ", error)

        # получения данных субьекта
        try:
            subject_rdn_attributes = self.certificate["subject"]["rdnSequence"]
            if isinstance(subject_rdn_attributes, rfc5280.RDNSequence):
                values["subject"] = parse_attributes_value(
                    rdn_attributes=subject_rdn_attributes
                )
        except KeyError as error:
            print("Ошибка при получении данных субьекта сертификата: ", error)

        return CertificateInfoModel(**values)
