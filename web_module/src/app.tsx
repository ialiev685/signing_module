import { Layout } from "@components/layout";
import "./fonts/fonts.css";
import "./app.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Verification } from "@pages/verification";
import { routes } from "@/routes";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: (
      <div>
        <h1>Ошибка</h1>
        <p>Что-то пошло не так</p>
      </div>
    ),
    children: [
      {
        path: routes.verificationSignature,
        element: <Verification />,
      },
      {
        path: routes.rootCertificate,
        element: <></>,
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
