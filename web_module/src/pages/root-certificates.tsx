import { Flex, Title } from "@mantine/core";
import { StoreNamePathModel } from "@/services/Api";
import { CertificatesList } from "@/components/certificates-list";

export const RootCertificates = () => {
  return (
    <Flex direction="column" gap={24}>
      <Title order={4}>Корневые сертификаты</Title>
      <CertificatesList storeName={StoreNamePathModel.MRoot} />
    </Flex>
  );
};
