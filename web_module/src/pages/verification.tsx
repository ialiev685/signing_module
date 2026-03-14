import { CardInfo } from "@/components/card-info";
import type { ResponseDataModelVerificationModel } from "@/services/Api";
import { api } from "@/services/client";
import { UploadFile } from "@components/upload-file";
import { Title, Flex, Button, SimpleGrid } from "@mantine/core";
import { useState } from "react";
import { getCertificateContentBar } from "./lib";

export const Verification = () => {
  const [documents, setDocuments] = useState<File[] | undefined>(undefined);
  const [signatures, setSignatures] = useState<File[] | undefined>(undefined);
  const [decodedData, setDecodedData] =
    useState<ResponseDataModelVerificationModel["data"]>(undefined);
  const [error, setError] = useState<string | undefined>(undefined);

  const handleVerification = async () => {
    if (!documents?.length || !signatures?.length) return;

    try {
      const { data } = await api.verifySignatureApiV1VerifySignaturePost({
        detached_signature: signatures[0],
        document: documents[0],
      });
      setDecodedData(data.data);
    } catch (error: unknown) {
      if (typeof error === "string") {
        setError(error);
      }
    }
  };

  const content = decodedData ? (
    <CardInfo
      title="Информация о сертификате"
      contentBar={getCertificateContentBar(decodedData)}
    />
  ) : (
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
  );

  return (
    <Flex gap={24} direction="column">
      <Title order={4}>Проверка открепленной подписи</Title>
      {content}
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
