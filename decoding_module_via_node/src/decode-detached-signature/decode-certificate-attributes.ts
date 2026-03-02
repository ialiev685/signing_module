import * as pki from "pkijs";
import { parseAttributesValueFromCertificate } from "./lib/parse-attributes-value-from-certificate";
import { convertUint8ArrayToHex } from "./lib/convert-uint-8-array-to-hex";
import { formatDateTime } from "./lib/format-date-time";

export class DecodeCertificateAttributes {
  protected certificate: pki.Certificate;

  constructor(certificate: pki.Certificate) {
    this.certificate = certificate;
  }
  public get subject() {
    return parseAttributesValueFromCertificate(this.certificate.subject);
  }

  public get issuer() {
    return parseAttributesValueFromCertificate(this.certificate.issuer);
  }

  public get serialNumber() {
    return convertUint8ArrayToHex(
      this.certificate.serialNumber.valueBlock.valueHexView,
    );
  }

  public get validFrom() {
    return formatDateTime(this.certificate.notBefore.value);
  }

  public get validTo() {
    return formatDateTime(this.certificate.notAfter.value);
  }
}
