import { Dropzone, MIME_TYPES } from "@mantine/dropzone";
import { Text, Flex } from "@mantine/core";
import { IconUpload } from "@tabler/icons-react";
import { useMantineTheme } from "@mantine/core";
import { FileCard } from "../file-card";

const fileExpansion = {
  p7b: "application/pkcs7-signature",
  p7s: "application/pkcs7-signature",
  sig: "application/pgp-signature",
  pdf: MIME_TYPES.pdf,
  jpeg: MIME_TYPES.jpeg,
  png: MIME_TYPES.png,
  doc: MIME_TYPES.doc,
  xls: MIME_TYPES.xls,
  xlsx: MIME_TYPES.xlsx,
} as const;

type UploadFileProps = {
  title?: string;
  accept?: (keyof typeof fileExpansion)[];
  onChange: (files?: File[]) => void;
  files?: File[];
};

export const UploadFile = ({
  title,
  accept,
  onChange,
  files,
}: UploadFileProps) => {
  const { colors } = useMantineTheme();

  return files?.length ? (
    files.map((file) => (
      <FileCard title={file.name} onClose={() => onChange(undefined)} />
    ))
  ) : (
    <Dropzone
      multiple={false}
      accept={accept?.map((expansion) => fileExpansion[expansion])}
      onDrop={onChange}
    >
      <Flex gap={12} align="center" justify="center">
        <IconUpload color={colors.gray[8]} />
        <div>
          <Text c={colors.gray[8]}>{title}</Text>
          {accept && (
            <Text size="sm" c={colors.gray[6]}>
              {accept?.map((expansion) => expansion).join(", ")}
            </Text>
          )}
        </div>
      </Flex>
    </Dropzone>
  );
};
