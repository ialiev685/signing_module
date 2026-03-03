export type CertificateInfo = {
  subjectName?: string | null;
  issuerName: string;
  thumbprint?: string | null;
  validFromDate?: string | null;
  validToDate?: string | null;
  serialNumber?: string | null;
};

export interface Signers extends CertificateInfo {
  signingTime?: string | null;
}

export type SigningStructure = {
  certificatesChain?: CertificateInfo[] | null;
  issuer?: Signers[] | null;
  signatureTimestampTime?: string | null;
  signingTime?: string | null;
};

export type ResponseModel = {
  data?: SigningStructure | null;
};
