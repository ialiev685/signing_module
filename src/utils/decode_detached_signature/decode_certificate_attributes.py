from pyasn1.codec.der import decoder

# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652, rfc2315  # type: ignore

# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280

from ..oid_configs import SUBJECT_OIDS
from ..action_models import AttributeValueModel, ResponseDataModel


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


class DecodeCertificateAttributes:
    certificate: rfc5280.Name

    def __init__(self, certificate: rfc5652.CertificateChoices):
        try:
            self.certificate = certificate

        except KeyError as error:
            print("Ошибка при получении общих данных сертификата: ", error)

    @property
    def certificate_info(self) -> ResponseDataModel:
        values = None
        try:

            issuer_rdn_attributes = self.certificate["rdnSequence"]
            if isinstance(issuer_rdn_attributes, rfc5280.RDNSequence):
                values = parse_attributes_value(rdn_attributes=issuer_rdn_attributes)
        except KeyError as error:
            print("Ошибка при получении значений атрибутов сертификата: ", error)
            return ResponseDataModel(is_success=False, data=values)

        return ResponseDataModel(is_success=True, data=values)
