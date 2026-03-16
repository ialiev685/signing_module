import { Layout } from "@components/layout";
import "./fonts/fonts.css";
import "./app.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Verification } from "@/pages/verification";
import { routes } from "@/routes";
import { RootCertificates } from "@/pages/root-certificates";
import { Container } from "@mantine/core";
import { MiddleCertificates } from "@/pages/middle-certificate";
import { CreateHash } from "@/pages/create-hash";

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
        path: routes.rootCertificates,
        element: <RootCertificates />,
      },
      {
        path: routes.middleCertificates,
        element: <MiddleCertificates />,
      },
      {
        path: routes.createHash,
        element: <CreateHash />,
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
