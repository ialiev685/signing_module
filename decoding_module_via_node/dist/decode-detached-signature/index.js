"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.DecodeDetachedSignature = void 0;
const asn1 = __importStar(require("asn1js"));
const pki = __importStar(require("pkijs"));
const base64_js_1 = __importDefault(require("base64-js"));
const decode_certificate_attributes_1 = require("./decode-certificate-attributes");
const constants_1 = require("./lib/constants");
const parse_date_time_1 = require("./lib/parse-date-time");
const parse_attributes_value_from_certificate_1 = require("./lib/parse-attributes-value-from-certificate");
const convert_uint_8_array_to_hex_1 = require("./lib/convert-uint-8-array-to-hex");
class DecodeDetachedSignature {
    constructor(signature) {
        if (!signature)
            return;
        try {
            const signatureBase64 = base64_js_1.default.toByteArray(signature);
            const decodedSignatureValue = asn1.fromBER(signatureBase64);
            const contentInfo = new pki.ContentInfo({
                schema: decodedSignatureValue.result,
            });
            if (contentInfo.contentType === pki.ContentInfo.SIGNED_DATA) {
                const signedData = new pki.SignedData({ schema: contentInfo.content });
                this.signedData = signedData;
            }
        }
        catch (error) {
            console.log("Ошибка при декодировании подписи (signed_data): ", error);
        }
    }
    get certificatesChain() {
        const certificates = this.signedData?.certificates?.filter((certificate) => certificate instanceof pki.Certificate) ?? [];
        if (certificates.length > 0) {
            const certificatesArray = certificates.map((certificate) => {
                const decodedCertificate = new decode_certificate_attributes_1.DecodeCertificateAttributes(certificate);
                return {
                    subjectName: decodedCertificate.subject,
                    issuerName: decodedCertificate.issuer,
                    serialNumber: decodedCertificate.serialNumber,
                    validFromDate: decodedCertificate.validFrom,
                    validToDate: decodedCertificate.validTo,
                };
            });
            return certificatesArray;
        }
        return [];
    }
    get signingTime() {
        const signerInfo = this.signedData?.signerInfos[0];
        if (signerInfo) {
            const signingTimeAttribute = signerInfo.signedAttrs?.attributes.find((attribute) => attribute.type === constants_1.SIGNING_TIME_OID);
            if (signingTimeAttribute?.values &&
                Array.isArray(signingTimeAttribute.values)) {
                const [value] = signingTimeAttribute.values;
                return (0, parse_date_time_1.parseDateTime)(value);
            }
            return undefined;
        }
        return undefined;
    }
    get issuer() {
        const signers = this.signedData?.signerInfos?.filter((certificate) => certificate.sid instanceof pki.IssuerAndSerialNumber) ?? [];
        if (signers.length > 0) {
            const decodedCertificates = signers.map((signer) => {
                const signingTime = signer.signedAttrs?.attributes.find((attr) => attr.type === constants_1.SIGNING_TIME_OID);
                return {
                    issuerName: (0, parse_attributes_value_from_certificate_1.parseAttributesValueFromCertificate)(signer.sid.issuer),
                    signingTime: Array.isArray(signingTime?.values)
                        ? (0, parse_date_time_1.parseDateTime)(signingTime.values[0])
                        : undefined,
                    serialNumber: (0, convert_uint_8_array_to_hex_1.convertUint8ArrayToHex)(signer.sid.serialNumber.valueBlock.valueHexView),
                };
            });
            return decodedCertificates;
        }
        return [];
    }
    get signing_structure() {
        return {
            certificatesChain: this.certificatesChain,
            issuer: this.issuer,
            signingTime: this.signingTime,
        };
    }
}
exports.DecodeDetachedSignature = DecodeDetachedSignature;
