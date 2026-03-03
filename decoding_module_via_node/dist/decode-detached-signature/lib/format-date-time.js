"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.formatDateTime = void 0;
const formatDateTime = (value) => {
    const formatter = new Intl.DateTimeFormat("ru-RU", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
        timeZone: "UTC",
    });
    return formatter.format(value);
};
exports.formatDateTime = formatDateTime;
