export const getNameFromSubjectName = (subjectName?: string | null): string => {
  if (!subjectName) return "";

  return (
    subjectName
      .split(",")
      .find((code) => code.trim().startsWith("CN="))
      ?.replace("CN=", "") ?? ""
  );
};
