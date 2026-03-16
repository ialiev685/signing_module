import { type ResponseDataModel } from "@/services/Api";

export const getNameFromSubjectName = (subjectName?: string | null): string => {
  if (!subjectName) return "";

  return (
    subjectName
      .split(",")
      .find((code) => code.trim().startsWith("CN="))
      ?.replace("CN=", "") ?? ""
  );
};

export const isErrorResponse = (value: unknown): value is ResponseDataModel => {
  return typeof value === "object" && value !== null && "error" in value;
};
