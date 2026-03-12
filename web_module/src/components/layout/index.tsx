import { AppShell, List, Title, useMantineTheme, Box } from "@mantine/core";
import { NavLink, Outlet } from "react-router-dom";
import { navItems } from "./config";

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
              <NavLink
                to={link}
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#228be6" : "inherit",
                  fontWeight: isActive ? 600 : 400,
                  transition: "color 0.2s ease",
                })}
              >
                {title}
              </NavLink>
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
