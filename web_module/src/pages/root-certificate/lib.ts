import { type ComboboxItem } from "@mantine/core";
import { type ResponseDataModelListCertificateInfoModel } from "@/services/Api";

const getNameFromSubjectName = (subjectName?: string | null): string => {
  if (!subjectName) return "";

  return (
    subjectName
      .split(",")
      .find((code) => code.trim().startsWith("CN="))
      ?.replace("CN=", "") ?? ""
  );
};
export const convertDataToSelectOptions = (
  data: ResponseDataModelListCertificateInfoModel["data"],
): ComboboxItem[] => {
  if (!data) return [];

  return data.map(({ thumbprint, subject_name }) => ({
    value: thumbprint ?? "",
    label: getNameFromSubjectName(subject_name),
  }));
};
