import { Card, Flex, useMantineTheme, Text } from "@mantine/core";
import { IconX } from "@tabler/icons-react";

type FileCardProps = {
  title: string;
  onClose?: () => void;
};

export const FileCard = ({ title, onClose }: FileCardProps) => {
  const { colors } = useMantineTheme();

  return (
    <Card shadow="xs">
      <Flex align="center" justify="space-between">
        <Text c={colors.gray[8]}>{title}</Text>
        <IconX
          color={colors.gray[8]}
          style={{ cursor: "pointer" }}
          onClick={onClose}
        />
      </Flex>
    </Card>
  );
};
