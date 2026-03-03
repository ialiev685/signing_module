"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseAttributesValueFromCertificate = void 0;
const constants_1 = require("./constants");
const parseAttributesValueFromCertificate = (subjectValue) => {
    try {
        const parsedSubject = subjectValue.typesAndValues
            .map(({ type, value }) => {
            const oid_key = type;
            if (oid_key in constants_1.SUBJECT_OIDS) {
                return `${constants_1.SUBJECT_OIDS[oid_key].nameCode}=${value.getValue()}`;
            }
            return undefined;
        })
            .filter(Boolean)
            .join(", ");
        return parsedSubject;
    }
    catch (error) {
        console.log("Ошибка при получении сертификата подписанта из структуры Asn1", error);
        return "";
    }
};
exports.parseAttributesValueFromCertificate = parseAttributesValueFromCertificate;
