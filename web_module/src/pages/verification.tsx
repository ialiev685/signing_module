// import { api } from "@/services/client";
import { UploadFile } from "@components/upload-file";
import { Title, Flex, Button, SimpleGrid } from "@mantine/core";
import { useState } from "react";

export const Verification = () => {
  const [documents, setDocuments] = useState<File[] | undefined>(undefined);
  const [signatures, setSignatures] = useState<File[] | undefined>(undefined);

  const handleVerification = () => {
    // api.verifySignatureApiV1VerifySignaturePost({});
  };

  return (
    <Flex gap={24} direction="column" align="flex-start">
      <Title order={4}>Проверка открепленной подписи</Title>
      <SimpleGrid cols={2}>
        <UploadFile
          files={documents}
          title="Загрузите документ"
          accept={["doc", "jpeg", "pdf", "png", "xls", "xlsx"]}
          onChange={setDocuments}
        />
        <UploadFile
          files={signatures}
          title="Загрузите подпись"
          accept={["p7b", "p7s", "sig"]}
          onChange={setSignatures}
        />
      </SimpleGrid>
      <Button
        disabled={!documents || !signatures}
        color="teal"
        onClick={handleVerification}
      >
        Проверить
      </Button>
    </Flex>
  );
};
