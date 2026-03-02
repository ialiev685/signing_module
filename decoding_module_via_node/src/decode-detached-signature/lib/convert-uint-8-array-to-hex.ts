export const convertUint8ArrayToHex = (uint8Array?: Uint8Array) => {
  if (uint8Array instanceof Uint8Array) {
    return Array.from(uint8Array)
      .map((byte) => byte.toString(16).padStart(2, "0"))
      .join("")
      .toUpperCase();
  }

  return "";
};
