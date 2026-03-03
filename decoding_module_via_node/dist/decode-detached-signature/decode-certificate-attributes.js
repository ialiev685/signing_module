"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DecodeCertificateAttributes = void 0;
const parse_attributes_value_from_certificate_1 = require("./lib/parse-attributes-value-from-certificate");
const convert_uint_8_array_to_hex_1 = require("./lib/convert-uint-8-array-to-hex");
const format_date_time_1 = require("./lib/format-date-time");
class DecodeCertificateAttributes {
    constructor(certificate) {
        this.certificate = certificate;
    }
    get subject() {
        return (0, parse_attributes_value_from_certificate_1.parseAttributesValueFromCertificate)(this.certificate.subject);
    }
    get issuer() {
        return (0, parse_attributes_value_from_certificate_1.parseAttributesValueFromCertificate)(this.certificate.issuer);
    }
    get serialNumber() {
        return (0, convert_uint_8_array_to_hex_1.convertUint8ArrayToHex)(this.certificate.serialNumber.valueBlock.valueHexView);
    }
    get validFrom() {
        return (0, format_date_time_1.formatDateTime)(this.certificate.notBefore.value);
    }
    get validTo() {
        return (0, format_date_time_1.formatDateTime)(this.certificate.notAfter.value);
    }
}
exports.DecodeCertificateAttributes = DecodeCertificateAttributes;
