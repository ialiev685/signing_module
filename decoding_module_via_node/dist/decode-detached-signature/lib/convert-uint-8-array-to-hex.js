"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.convertUint8ArrayToHex = void 0;
const convertUint8ArrayToHex = (uint8Array) => {
    if (uint8Array instanceof Uint8Array) {
        return Array.from(uint8Array)
            .map((byte) => byte.toString(16).padStart(2, "0"))
            .join("")
            .toUpperCase();
    }
    return "";
};
exports.convertUint8ArrayToHex = convertUint8ArrayToHex;
