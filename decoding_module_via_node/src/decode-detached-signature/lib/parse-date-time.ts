import * as asn1 from "asn1js";
import { formatDateTime } from "./format-date-time";

export const parseDateTime = (value: unknown) => {
  if (value instanceof asn1.UTCTime) {
    const signingDate = new Date(
      value.year,
      value.month - 1,
      value.day,
      value.hour,
      value.minute,
    );

    return formatDateTime(signingDate);
  }

  return undefined;
};
