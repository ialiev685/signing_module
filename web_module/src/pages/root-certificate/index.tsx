import {
  NativeSelect,
  type ComboboxItem,
  FileButton,
  Flex,
  Title,
  Button,
  useMantineTheme,
} from "@mantine/core";
import { api } from "@/services/client";
import { StoreNamePathModel } from "@/services/Api";
import { useEffect, useState } from "react";
import { convertDataToSelectOptions } from "./lib";
import { notifications } from "@mantine/notifications";
import { IconX, IconCheck } from "@tabler/icons-react";

export const RootCertificate = () => {
  const { colors } = useMantineTheme();

  const [data, setData] = useState<ComboboxItem[]>([]);
  const getRootCertificate = async () => {
    try {
      const { data } =
        await api.getRootCertificatesApiV1GetRootCertificatesStoreNameGet(
          StoreNamePathModel.MRoot,
        );

      setData(convertDataToSelectOptions(data.data));
    } catch (error: unknown) {
      console.log("error", error);
    }
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    getRootCertificate();
  }, []);

  const handleUploadRootCertificate = async (file: File | null) => {
    if (!file) return;
    try {
      const { data } =
        await api.setPersonalCertificatesApiV1SetCertificateStoreNamePost(
          StoreNamePathModel.MRoot,
          { certificate: file },
        );
      if (data.data) {
        notifications.show({
          title: "Успешно",
          message: "Сертификат добавлен",
          icon: <IconCheck />,
          position: "top-center",
          color: "green",
        });
      }
    } catch (error: unknown) {
      console.log("error", error);
      notifications.show({
        icon: <IconX />,
        title: "Ошибка",
        message: "Сертификат не блы добавлен",
        position: "top-center",
        color: "red",
      });
    }
  };

  return (
    <Flex direction="column" gap={24}>
      <Title order={4}>Корневые сертификаты</Title>
      <NativeSelect data={data} />
      <FileButton
        accept="application/x-x509-ca-cert, application/x-pkcs7-certificates"
        onChange={handleUploadRootCertificate}
      >
        {(props) => (
          <Button {...props} color={colors.cyan[5]}>
            Добавить
          </Button>
        )}
      </FileButton>
    </Flex>
  );
};
