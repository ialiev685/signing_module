# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652  # type: ignore

# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280

from models_types import ResponseDataModel

from .parse_attributes_value_from_certificate import (
    parse_attributes_value_from_certificate,
)


class DecodeCertificateAttributes:
    certificate: rfc5280.Name

    def __init__(self, certificate: rfc5652.CertificateChoices):
        try:
            self.certificate = certificate

        except KeyError as error:
            print(
                "Ошибка при получении общих данных сертификата (декодирование): ", error
            )

    @property
    def certificate_info(self) -> ResponseDataModel:
        values = None
        try:

            issuer_rdn_attributes = self.certificate["rdnSequence"]
            if isinstance(issuer_rdn_attributes, rfc5280.RDNSequence):
                values = parse_attributes_value_from_certificate(
                    rdn_attributes=issuer_rdn_attributes
                )
        except KeyError as error:
            print(
                "Ошибка при вызове метода DecodeCertificateAttributes.certificate_info: ",
                error,
            )
            return ResponseDataModel(is_success=False, data=values)

        return ResponseDataModel(is_success=True, data=values)
