import {
  FileButton,
  Flex,
  Button,
  useMantineTheme,
  Group,
} from "@mantine/core";
import { api } from "@/services/client";
import { StoreNamePathModel, type CertificateInfoModel } from "@/services/Api";
import { useEffect, useState } from "react";

import { notifications } from "@mantine/notifications";
import { DataTable } from "mantine-datatable";
import { modals } from "@mantine/modals";
import {
  columns,
  errorNotificationOptions,
  successNotificationOptions,
} from "./config";
import { isErrorResponse } from "@/utils/lib";

type CertificatesListProps = {
  storeName: StoreNamePathModel;
};

export const CertificatesList = ({ storeName }: CertificatesListProps) => {
  const [selectedThumbprint, setSelectedThumbprint] = useState<
    string | undefined
  >(undefined);
  const { colors } = useMantineTheme();

  const [data, setData] = useState<CertificateInfoModel[]>([]);
  const getRootCertificate = async () => {
    try {
      const { data } =
        await api.getRootCertificatesApiV1GetRootCertificatesStoreNameGet(
          storeName,
        );

      setData(data.data ?? []);
    } catch (error: unknown) {
      if (isErrorResponse(error)) {
        console.log("error", error.error);
      }

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
          storeName,
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
      if (isErrorResponse(error)) {
        console.log("error", error.error);
      }
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
              store_name: storeName,
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
          if (isErrorResponse(error)) {
            console.log("error", error.error);
          }
        }
      },
    });
  };

  return (
    <Flex direction="column" gap={24}>
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
            <Button {...props} color={colors.blue[5]}>
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
    </Flex>
  );
};
