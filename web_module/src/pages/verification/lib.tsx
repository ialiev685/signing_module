import type { VerificationModel } from "@/services/Api";
import { Badge } from "@mantine/core";
import type { ReactNode } from "react";

type ContentBar = { key: string; value?: ReactNode | null };

export const getSignatureContentBar = (
  data: VerificationModel,
): ContentBar[] => {
  if (!data.result) return [];

  return [
    {
      key: "Результат проверки",
      value: (
        <Badge color={data.is_valid ? "teal" : "red"}>
          {data.is_valid ? "Подпись действительна" : "Подпись недействительна"}
        </Badge>
      ),
    },
    {
      key: "Время подписи",
      value: data.result.signing_time,
    },
  ];
};

const formatDate = (date: string) => {
  return date.split(" ").at(0);
};

export const getCertificateContentBar = (
  data: VerificationModel,
): ContentBar[] => {
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
        value:
          issuer?.valid_from_date &&
          issuer?.valid_to_date &&
          `${formatDate(issuer?.valid_from_date)} - ${formatDate(issuer?.valid_to_date)}`,
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
        value:
          signatoryCertificate?.valid_from_date &&
          signatoryCertificate?.valid_to_date &&
          `${formatDate(signatoryCertificate?.valid_from_date)} - ${formatDate(signatoryCertificate?.valid_to_date)}`,
      },
    ];
  }
};
