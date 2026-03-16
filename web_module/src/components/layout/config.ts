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
    link: routes.rootCertificates,
    title: "Корневые сертификаты",
  },
  {
    link: routes.trustedCertificates,
    title: "Промежуточные сертификаты",
  },
];
