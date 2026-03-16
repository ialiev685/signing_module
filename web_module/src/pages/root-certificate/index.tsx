import {
  FileButton,
  Flex,
  Title,
  Button,
  useMantineTheme,
  Text,
  Group,
} from "@mantine/core";
import { api } from "@/services/client";
import { StoreNamePathModel, type CertificateInfoModel } from "@/services/Api";
import { useEffect, useState } from "react";
import { getNameFromSubjectName } from "./lib";
import { notifications } from "@mantine/notifications";
import { IconX, IconCheck } from "@tabler/icons-react";
import { DataTable, type DataTableColumn } from "mantine-datatable";

const columns: DataTableColumn<CertificateInfoModel>[] = [
  {
    accessor: "subject",
    title: "Имя субъкта",
    render: ({ subject_name }) => (
      <Text truncate maw={190} size="xs">
        {getNameFromSubjectName(subject_name)}
      </Text>
    ),
  },
  {
    accessor: "thumbprint",
    title: "Отпечаток",
    render: ({ thumbprint }) => <Text size="xs">{thumbprint}</Text>,
  },
];

export const RootCertificate = () => {
  const [selectedIndex, setSelectedIndex] = useState<number | undefined>(
    undefined,
  );
  const { colors } = useMantineTheme();

  const [data, setData] = useState<CertificateInfoModel[]>([]);
  const getRootCertificate = async () => {
    try {
      const { data } =
        await api.getRootCertificatesApiV1GetRootCertificatesStoreNameGet(
          StoreNamePathModel.MRoot,
        );

      setData(data.data ?? []);
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

      <DataTable
        rowBackgroundColor={(_, index) =>
          selectedIndex === index ? colors.cyan[4] : undefined
        }
        withColumnBorders
        withTableBorder
        highlightOnHover
        records={data}
        onRowClick={({ index }) => {
          setSelectedIndex(index);
        }}
        columns={columns}
      />
      <Group justify="space-between" grow>
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
        <Button disabled={!selectedIndex} color="red">
          Удалить
        </Button>
      </Group>
    </Flex>
  );
};
