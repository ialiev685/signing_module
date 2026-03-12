import { AppShell, List, Title, useMantineTheme, Box } from "@mantine/core";
import { Outlet } from "react-router-dom";
import { navItems } from "./config";
import { Link } from "react-router-dom";

export const Layout = () => {
  const { colors } = useMantineTheme();

  return (
    <AppShell header={{ height: 60 }}>
      <AppShell.Header p={12} bg="cyan">
        <Title order={2}>Модуль подписания</Title>
      </AppShell.Header>

      <AppShell.Navbar py={24} px={12} w={330}>
        <List spacing="xs" icon={<></>}>
          {navItems.map(({ title, link }) => (
            <List.Item key={title}>
              <Link
                style={{
                  textDecoration: "none",
                  color: "inherit",
                }}
                to={link}
              >
                {title}
              </Link>
            </List.Item>
          ))}
        </List>
      </AppShell.Navbar>

      <AppShell.Main pl={330} bg={colors.gray[0]}>
        <Box p={24} w={600}>
          <Outlet />
        </Box>
      </AppShell.Main>
    </AppShell>
  );
};
