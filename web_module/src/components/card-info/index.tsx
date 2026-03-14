import { Card, Grid, Text } from "@mantine/core";
import type { ReactNode } from "react";

type CardInfoProps = {
  contentBar: { key: string; value?: ReactNode | null }[];
  title?: string;
};

export const CardInfo = ({ contentBar, title }: CardInfoProps) => {
  return (
    <Card shadow="xs">
      {title && (
        <Card.Section p={16}>
          <Text fw={600}> Информация о сертификате</Text>
        </Card.Section>
      )}
      {contentBar
        .filter(({ value }) => Boolean(value))
        .map(({ key, value }) => (
          <Card.Section withBorder px={16}>
            <Grid py={8}>
              <Grid.Col span={4}>{key}</Grid.Col>
              <Grid.Col style={{ textAlign: "end" }} span={8}>
                {value}
              </Grid.Col>
            </Grid>
          </Card.Section>
        ))}
    </Card>
  );
};
