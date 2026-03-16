import { Text } from "@mantine/core";
import { type CertificateInfoModel } from "@/services/Api";

import { type NotificationData } from "@mantine/notifications";
import { IconX, IconCheck } from "@tabler/icons-react";
import { type DataTableColumn } from "mantine-datatable";
import { getNameFromSubjectName } from "@/utils/lib";

export const columns: DataTableColumn<CertificateInfoModel>[] = [
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

export const errorNotificationOptions: Partial<NotificationData> = {
  icon: <IconX />,
  title: "Ошибка",
  position: "top-center",
  color: "red",
};

export const successNotificationOptions: Partial<NotificationData> = {
  icon: <IconCheck />,
  title: "Успешно",
  position: "top-center",
  color: "green",
};
