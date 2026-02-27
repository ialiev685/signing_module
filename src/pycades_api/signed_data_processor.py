from dict_types import SigningStructureDict

from .get_data_after_processing_item import get_data_after_processing_item
from .get_oids_from_certificate import get_oids_from_certificate
from pycades_types import SignedData, Certificate


class SignedDataProcessor:

    def __init__(self, signed_data: SignedData):
        self._signed_data = signed_data

    def _get_certificates_chain(self) -> list[Certificate] | None:
        try:

            return get_data_after_processing_item(
                object_data=self._signed_data.Certificates
            )
        except Exception as error:
            print(
                "Ошибка при вызове метода SignedDataProcessor._get_certificates_chain",
                error,
            )
            return None

    @property
    def issuer(self):
        try:
            return get_data_after_processing_item(object_data=self._signed_data.Signers)
        except Exception as error:
            print("Ошибка при вызове метода SignedDataProcessor.issuer", error)
            return None

    @property
    def certificates_chain_with_oids(self):
        try:
            certificates_chain = self._get_certificates_chain()
            if certificates_chain:
                result = []
                for certificate in certificates_chain:
                    result.append(
                        {
                            "certificate": certificate,
                            "oids": get_oids_from_certificate(certificate),
                        }
                    )
                return result
            return None
        except Exception as error:
            print(
                "Ошибка при вызове метода SignedDataProcessor.certificates_chain_with_oids",
                error,
            )
            return None

    @property
    def signing_structure(self) -> SigningStructureDict:

        issuer_data = self.issuer[0]
        signature_time_stampTime = None

        try:
            signature_time_stampTime = issuer_data.SignatureTimeStampTime
        except:
            pass

        return {
            "certificates_chain": self.certificates_chain_with_oids,
            "issuer": self.issuer,
            "SignatureTimeStampTime": signature_time_stampTime,
            "SigningTime": issuer_data.SigningTime,
        }
