from models_types import CertificateInfoModel, SignersModel, SigningStructureModel
from utils import safe_get_attr

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
    def issuer(self) -> list[SignersModel] | None:
        try:
            processed_data = get_data_after_processing_item(
                object_data=self._signed_data.Signers
            )
            return [
                SignersModel(
                    subject_name=certificate.Certificate.SubjectName,
                    serial_number=certificate.Certificate.SerialNumber,
                    thumbprint=certificate.Certificate.Thumbprint,
                    issuer_name=certificate.Certificate.IssuerName,
                    valid_from_date=certificate.Certificate.ValidFromDate,
                    valid_to_date=certificate.Certificate.ValidToDate,
                    signing_time=certificate.SigningTime,
                )
                for certificate in processed_data
            ]
        except Exception as error:
            print("Ошибка при вызове метода SignedDataProcessor.issuer", error)
            return None

    @property
    def certificates_chain_with_oids(self) -> list[CertificateInfoModel] | None:
        try:
            certificates_chain = self._get_certificates_chain()
            if certificates_chain:
                return [
                    CertificateInfoModel(
                        subject_name=certificate.SubjectName,
                        serial_number=certificate.SerialNumber,
                        thumbprint=certificate.Thumbprint,
                        issuer_name=certificate.IssuerName,
                        valid_from_date=certificate.ValidFromDate,
                        valid_to_date=certificate.ValidToDate,
                        oids=get_oids_from_certificate(certificate),
                    )
                    for certificate in certificates_chain
                ]
            return None
        except Exception as error:
            print(
                "Ошибка при вызове метода SignedDataProcessor.certificates_chain_with_oids",
                error,
            )
            return None

    @property
    def signing_structure(self) -> SigningStructureModel:
        signing_time = (
            self.issuer[0].signing_time
            if self.issuer and len(self.issuer) > 0
            else None
        )

        return SigningStructureModel(
            certificates_chain=self.certificates_chain_with_oids,
            issuer=self.issuer,
            signing_time=signing_time,
        )
