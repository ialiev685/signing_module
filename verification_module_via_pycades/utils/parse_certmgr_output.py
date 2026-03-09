import re
from models_types import CertificateInfoModel, RequiredCertificateKey


def parse_certmgr_output(output: str) -> list[CertificateInfoModel]:
    lines = output.split("\n")
    certificates: list[str] = []
    current_cert: dict[RequiredCertificateKey, str] = {}

    for line in lines:
        if re.match("\d+-{7,}", line):
            if current_cert:
                certificates.append(CertificateInfoModel(**current_cert))
                current_cert = {}
            continue

        if ":" in line:
            name, value = line.split(":", 1)
            key = name.strip()
            value = value.strip()
            if "thumbprint" in key.lower():
                current_cert["thumbprint"] = value.upper()
            elif "issuer" in key.lower():
                current_cert["issuer_name"] = value
            elif "subject" in key.lower():
                current_cert["thumbprint"] = value

    return certificates
