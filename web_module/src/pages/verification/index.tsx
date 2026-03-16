import { CardInfo } from "@/components/card-info";
import type { ResponseDataModelVerificationModel } from "@/services/Api";
import { api } from "@/services/client";
import { UploadFile } from "@components/upload-file";
import {
  Title,
  Flex,
  Button,
  SimpleGrid,
  useMantineTheme,
  Alert,
} from "@mantine/core";
import { useState } from "react";
import { getCertificateContentBar, getSignatureContentBar } from "./lib";

export const Verification = () => {
  const { colors } = useMantineTheme();
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
      if (data.has_error && typeof data.error === "string") {
        setError(data.error);
      }
    } catch (error: unknown) {
      console.error("error", error);
    }
  };

  const handleClear = async () => {
    setDecodedData(undefined);
    setDocuments(undefined);
    setSignatures(undefined);
    setError(undefined);
  };

  const content = decodedData ? (
    <Flex direction="column" gap={24}>
      <CardInfo
        title="Информация о подписи"
        contentBar={getSignatureContentBar(decodedData)}
      />
      <CardInfo
        title="Информация о сертификате"
        contentBar={getCertificateContentBar(decodedData)}
      />
    </Flex>
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
        accept={["p7s", "sig"]}
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
        color={colors.cyan[5]}
        onClick={decodedData ? handleClear : handleVerification}
      >
        {decodedData ? "Назад" : "Проверить"}
      </Button>
      {error && (
        <Alert
          title="Ошибка"
          color="red"
          onClose={() => setError(undefined)}
          withCloseButton
        >
          {error}
        </Alert>
      )}
    </Flex>
  );
};
