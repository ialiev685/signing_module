from typing import TypedDict


class CertificateDict(TypedDict):
    SubjectName: str
    IssuerName: str
    Thumbprint: str | None
    ValidFromDate: str
    ValidToDate: str
    SerialNumber: str
    OIDs: list[str] | None


class SigningStructureDict(TypedDict):
    certificates_chain: list[CertificateDict]
    issuer: list[CertificateDict]
    SignatureTimeStampTime: str | None
    SigningTime: str
