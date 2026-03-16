import { Flex, Title, useMantineTheme, Text } from "@mantine/core";
import { StoreNamePathModel } from "@/services/Api";
import { CertificatesList } from "@/components/certificates-list";

export const RootCertificate = () => {
  const { colors } = useMantineTheme();

  return (
    <Flex direction="column" gap={24}>
      <Title order={4}>Корневые сертификаты</Title>
      <CertificatesList storeName={StoreNamePathModel.MRoot} />

      <Text>
        <a
          style={{ textDecoration: "none", color: colors.blue[6] }}
          target="_blank"
          href="https://testca.cryptopro.ru/certsrv/certcarc.asp"
        >
          Скачать сертификат ЦС или цепочку сертификатов ЦС
        </a>
      </Text>
    </Flex>
  );
};
