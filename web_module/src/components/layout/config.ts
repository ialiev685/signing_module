import { routes } from "@/routes";

type NavItem = {
  link: string;
  title: string;
};

export const navItems: NavItem[] = [
  {
    link: routes.verificationSignature,
    title: "Проверка открепленной подписи",
  },
  {
    link: routes.rootCertificate,
    title: "Корневые сертификаты",
  },
];
