import { Api } from "./Api";

export const api = new Api({
  baseUrl: "http://localhost:8004",
  baseApiParams: {
    headers: {
      "Content-Type": "application/json",
    },
  },
}).api;
