import { AppShell, List, Title, Container } from "@mantine/core";
import { Outlet } from "react-router-dom";
import { navItems } from "./config";
import { Link } from "react-router-dom";

export const Layout = () => {
  return (
    <AppShell header={{ height: 60 }}>
      <AppShell.Header p={12}>
        <Title order={2}>Модуль подписания</Title>
      </AppShell.Header>

      <AppShell.Navbar py={24} px={12} w={330}>
        <List spacing="xs" icon={<></>}>
          {navItems.map(({ title, link }) => (
            <List.Item key={title}>
              <Link to={link}>{title}</Link>
            </List.Item>
          ))}
        </List>
      </AppShell.Navbar>

      <AppShell.Main pl={330}>
        <Container p={24} mx={0}>
          <Outlet />
        </Container>
      </AppShell.Main>
    </AppShell>
  );
};
