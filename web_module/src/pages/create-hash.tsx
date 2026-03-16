import { UploadFile } from "@/components/upload-file";
import { api } from "@/services/client";
import { Button, Flex, useMantineTheme, Text } from "@mantine/core";
import { useState } from "react";

export const CreateHash = () => {
  const [files, setFiles] = useState<File[] | undefined>(undefined);
  const [hash, setHash] = useState<string | undefined>(undefined);
  const { colors } = useMantineTheme();

  const handleCreateHash = async () => {
    if (!files) return;
    const { data } = await api.createHashApiV1CreateHashPost({
      file: files[0],
    });

    if (data.data) {
      setHash(data.data);
    }
  };

  return (
    <Flex direction="column" gap={24}>
      <Text
        bg="#FFF"
        fw={600}
        size="sm"
        h={40}
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {hash}
      </Text>

      <UploadFile
        files={files}
        title="Загрузите файл"
        onChange={(files) => {
          setFiles(files);
          if (!files) {
            setHash(undefined);
          }
        }}
        accept={["doc", "jpeg", "pdf", "png", "xls", "xlsx"]}
      />
      <Button color={colors.cyan[5]} onClick={handleCreateHash}>
        Рассчитать
      </Button>
    </Flex>
  );
};
