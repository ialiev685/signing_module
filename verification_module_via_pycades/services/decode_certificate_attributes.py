# Cryptographic Message Syntax (CMS)
from pyasn1_modules import rfc5652  # type: ignore

# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280

from utils.parse_attributes_value_from_certificate import (
    parse_attributes_value_from_certificate,
)


class DecodeCertificateAttributes:
    certificate: rfc5280.Name
    error: list[str] = []

    def __init__(self, certificate: rfc5652.CertificateChoices):
        self.certificate = certificate

    @property
    def certificate_info(self):
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
            self.error.append(str(error))
            return values

        return values
