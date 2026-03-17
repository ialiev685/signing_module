import { AppShell, List, Title, useMantineTheme, Box } from "@mantine/core";
import { NavLink, Outlet } from "react-router-dom";
import { navItems } from "./config";
import styles from "./styles.module.css";

export const Layout = () => {
  const { colors } = useMantineTheme();

  return (
    <AppShell header={{ height: 60 }}>
      <AppShell.Header p={12} bg={colors.gray[8]}>
        <Title order={2} c={colors.yellow[0]}>
          Модуль проверки подписания
        </Title>
      </AppShell.Header>

      <AppShell.Navbar py={24} px={12} w={330}>
        <List spacing="xs" icon={<></>}>
          {navItems.map(({ title, link }) => (
            <List.Item key={title}>
              <NavLink
                className={({ isActive }) =>
                  [styles.link, isActive ? styles.active : ""].join(" ")
                }
                to={link}
              >
                {title}
              </NavLink>
            </List.Item>
          ))}
        </List>
      </AppShell.Navbar>

      <AppShell.Main pl={330} bg={colors.gray[1]}>
        <Box p={24} w={600}>
          <Outlet />
        </Box>
      </AppShell.Main>
    </AppShell>
  );
};
