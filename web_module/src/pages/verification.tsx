import { UploadFile } from "@components/upload-file";
import { Title, Flex } from "@mantine/core";

export const Verification = () => {
  return (
    <Flex gap={24} direction="column">
      <Title order={4}>Проверка открепленной подписи</Title>
      <UploadFile />
    </Flex>
  );
};
