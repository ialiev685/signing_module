import { Dropzone, MIME_TYPES } from "@mantine/dropzone";
import { Text, Flex } from "@mantine/core";
import { IconUpload } from "@tabler/icons-react";

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
};

export const UploadFile = ({ title, accept }: UploadFileProps) => {
  return (
    <Dropzone
      multiple={false}
      accept={accept?.map((expansion) => fileExpansion[expansion])}
      onDrop={(files) => {
        console.log("files", files);
      }}
    >
      <Flex gap={12} align="center">
        <IconUpload />
        <div>
          <Text>{title}</Text>
          {accept && (
            <Text size="sm" c="dimmed">
              {accept?.map((expansion) => expansion).join(", ")}
            </Text>
          )}
        </div>
      </Flex>
    </Dropzone>
  );
};
