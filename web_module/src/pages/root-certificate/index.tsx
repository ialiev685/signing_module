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
import { notifications, type NotificationData } from "@mantine/notifications";
import { IconX, IconCheck } from "@tabler/icons-react";
import { DataTable, type DataTableColumn } from "mantine-datatable";
import { modals } from "@mantine/modals";

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

const errorNotificationOptions: Partial<NotificationData> = {
  icon: <IconX />,
  title: "Ошибка",
  position: "top-center",
  color: "red",
};

const successNotificationOptions: Partial<NotificationData> = {
  icon: <IconCheck />,
  title: "Успешно",
  position: "top-center",
  color: "green",
};

export const RootCertificate = () => {
  const [selectedThumbprint, setSelectedThumbprint] = useState<
    string | undefined
  >(undefined);
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
      setData([]);
      notifications.show({
        ...errorNotificationOptions,
        message: "Ошибка при получении сертификатов",
      });
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
          ...successNotificationOptions,
          message: "Сертификат добавлен",
        });
        await getRootCertificate();
      }
    } catch (error: unknown) {
      console.log("error", error);
      notifications.show({
        ...errorNotificationOptions,
        message: "Сертификат не был добавлен",
      });
    }
  };

  const handleRemoveRootCertificate = async () => {
    if (!selectedThumbprint) return;
    modals.openConfirmModal({
      title: "Пожалуйста подтвердите удаление",
      children: "Вы действительно хотите удалить сертификат?",
      labels: { cancel: "Отмена", confirm: "Удалить" },
      confirmProps: { color: "red" },
      centered: true,
      onConfirm: async () => {
        try {
          const { data } =
            await api.removeCertificateApiV1RemoveCertificatePost({
              thumbprint: selectedThumbprint,
              store_name: StoreNamePathModel.MRoot,
            });
          if (data.data) {
            notifications.show({
              ...successNotificationOptions,
              message: "Сертификат удален",
            });
            await getRootCertificate();
          }
        } catch (error: unknown) {
          notifications.show({
            ...errorNotificationOptions,
            message: "Сертификат не был удален",
          });
          console.log("error", error);
        }
      },
    });
  };

  return (
    <Flex direction="column" gap={24}>
      <Title order={4}>Корневые сертификаты</Title>

      <DataTable
        rowBackgroundColor={(record) =>
          selectedThumbprint === record.thumbprint ? colors.cyan[4] : undefined
        }
        withColumnBorders
        withTableBorder
        highlightOnHover
        records={data}
        onRowClick={({ record }) => {
          if (record.thumbprint) {
            setSelectedThumbprint(record.thumbprint);
          }
        }}
        columns={columns}
      />
      <Group justify="space-between" grow>
        <FileButton
          accept=".p7b,.crt,.cer"
          onChange={handleUploadRootCertificate}
        >
          {(props) => (
            <Button {...props} color={colors.cyan[5]}>
              Добавить
            </Button>
          )}
        </FileButton>
        <Button
          disabled={!selectedThumbprint}
          color="red"
          onClick={handleRemoveRootCertificate}
        >
          Удалить
        </Button>
      </Group>
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
