import type { VerificationModel } from "@/services/Api";

export const getCertificateContentBar = (
  data: VerificationModel,
): { key: string; value?: string | null }[] => {
  if (!data.result) return [];
  const issuer = data.result?.issuer?.at(0);
  if (data.is_valid) {
    return [
      {
        key: "Субъект",
        value: issuer?.subject_name,
      },
      {
        key: "Серийный номер",
        value: issuer?.serial_number,
      },
      {
        key: "Отпечаток",
        value: issuer?.thumbprint,
      },
      {
        key: "Издатель",
        value: issuer?.issuer_name,
      },
      {
        key: "Срок действия",
        value: `${issuer?.valid_from_date} - ${issuer?.valid_to_date}`,
      },
    ];
  } else {
    const signatoryCertificate = data.result.certificates_chain?.find(
      (certificate) => certificate.serial_number === issuer?.serial_number,
    );

    return [
      {
        key: "Субъект",
        value: signatoryCertificate?.subject_name,
      },
      {
        key: "Серийный номер",
        value: signatoryCertificate?.serial_number,
      },

      {
        key: "Издатель",
        value: signatoryCertificate?.issuer_name,
      },
      {
        key: "Срок действия",
        value: `${signatoryCertificate?.valid_from_date} - ${issuer?.valid_to_date}`,
      },
    ];
  }
};
