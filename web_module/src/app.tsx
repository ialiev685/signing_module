import { Layout } from "@components/layout";
import "./fonts/fonts.css";
import "./app.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Verification } from "@pages/verification";

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
        path: "verificationSignature",
        element: <Verification />,
      },
      {
        path: "rootCertificate",
        element: <></>,
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
