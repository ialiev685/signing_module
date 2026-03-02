import * as asn1 from "asn1js";
import * as pki from "pkijs";
import base64 from "base64-js";
import { DecodeCertificateAttributes } from "./decode-certificate-attributes";
import { SIGNING_TIME_OID } from "./lib/constants";
import { parseDateTime } from "./lib/parse-date-time";
import { parseAttributesValueFromCertificate } from "./lib/parse-attributes-value-from-certificate";
import { CertificateInfo, Signers, SigningStructure } from "./types";
import { convertUint8ArrayToHex } from "./lib/convert-uint-8-array-to-hex";

export class DecodeDetachedSignature {
  public signedData?: pki.SignedData;

  constructor(signature?: string | null) {
    if (!signature) return;
    try {
      const signatureBase64 = base64.toByteArray(signature);

      const decodedSignatureValue = asn1.fromBER(signatureBase64);

      const contentInfo = new pki.ContentInfo({
        schema: decodedSignatureValue.result,
      });

      if (contentInfo.contentType === pki.ContentInfo.SIGNED_DATA) {
        const signedData = new pki.SignedData({ schema: contentInfo.content });
        this.signedData = signedData;
      }
    } catch (error) {
      console.log("Ошибка при декодировании подписи (signed_data): ", error);
    }
  }

  public get certificatesChain(): CertificateInfo[] {
    const certificates =
      this.signedData?.certificates?.filter(
        (certificate) => certificate instanceof pki.Certificate,
      ) ?? [];

    if (certificates.length > 0) {
      const certificatesArray = certificates.map<CertificateInfo>(
        (certificate) => {
          const decodedCertificate = new DecodeCertificateAttributes(
            certificate,
          );
          return {
            subjectName: decodedCertificate.subject,
            issuerName: decodedCertificate.issuer,
            serialNumber: decodedCertificate.serialNumber,
            validFromDate: decodedCertificate.validFrom,
            validToDate: decodedCertificate.validTo,
          };
        },
      );

      return certificatesArray;
    }
    return [];
  }

  public get signingTime() {
    const signerInfo = this.signedData?.signerInfos[0];

    if (signerInfo) {
      const signingTimeAttribute = signerInfo.signedAttrs?.attributes.find(
        (attribute) => attribute.type === SIGNING_TIME_OID,
      );

      if (
        signingTimeAttribute?.values &&
        Array.isArray(signingTimeAttribute.values)
      ) {
        const [value] = signingTimeAttribute.values;

        return parseDateTime(value);
      }

      return undefined;
    }

    return undefined;
  }

  public get issuer(): Signers[] {
    const signers =
      this.signedData?.signerInfos?.filter(
        (certificate) => certificate.sid instanceof pki.IssuerAndSerialNumber,
      ) ?? [];

    if (signers.length > 0) {
      const decodedCertificates = signers.map<Signers>((signer) => {
        const signingTime = signer.signedAttrs?.attributes.find(
          (attr) => attr.type === SIGNING_TIME_OID,
        );
        return {
          issuerName: parseAttributesValueFromCertificate(signer.sid.issuer),
          signingTime: Array.isArray(signingTime?.values)
            ? parseDateTime(signingTime.values[0])
            : undefined,
          serialNumber: convertUint8ArrayToHex(
            signer.sid.serialNumber.valueBlock.valueHexView,
          ),
        };
      });

      return decodedCertificates;
    }

    return [];
  }
  public get signing_structure(): SigningStructure {
    return {
      certificatesChain: this.certificatesChain,
      issuer: this.issuer,
      signingTime: this.signingTime,
    };
  }
}
