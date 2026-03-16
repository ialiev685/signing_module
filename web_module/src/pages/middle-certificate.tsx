import { Flex, Title } from "@mantine/core";
import { StoreNamePathModel } from "@/services/Api";
import { CertificatesList } from "@/components/certificates-list";

export const MiddleCertificates = () => {
  return (
    <Flex direction="column" gap={24}>
      <Title order={4}>Промежуточные сертификаты</Title>
      <CertificatesList storeName={StoreNamePathModel.MCA} />
    </Flex>
  );
};
