import { Layout } from "@components/layout";
import "./fonts/fonts.css";
import "./app.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Verification } from "@/pages/verification";
import { routes } from "@/routes";
import { RootCertificate } from "@/pages/root-certificate";
import { Container } from "@mantine/core";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: (
      <Container>
        <h1>Ошибка</h1>
        <p>Что-то пошло не так</p>
      </Container>
    ),
    children: [
      {
        path: routes.verificationSignature,
        element: <Verification />,
      },
      {
        path: routes.rootCertificate,
        element: <RootCertificate />,
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
