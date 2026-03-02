import * as pki from "pkijs";

import { SUBJECT_OIDS } from "./constants";

export const parseAttributesValueFromCertificate = (
  subjectValue: pki.Certificate["subject"],
) => {
  try {
    const parsedSubject = subjectValue.typesAndValues
      .map(({ type, value }) => {
        const oid_key = type as keyof typeof SUBJECT_OIDS;
        if (oid_key in SUBJECT_OIDS) {
          return `${SUBJECT_OIDS[oid_key].nameCode}=${value.getValue()}`;
        }
        return undefined;
      })
      .filter(Boolean)
      .join(", ");

    return parsedSubject;
  } catch (error) {
    console.log(
      "Ошибка при получении сертификата подписанта из структуры Asn1",
      error,
    );

    return "";
  }
};
