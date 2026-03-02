import express, { Request, Response } from "express";
import { ResponseModel } from "./decode-detached-signature/types";
import { DecodeDetachedSignature } from "./decode-detached-signature";
const app = express();
const PORT = process.env.PORT || 8005;

app.use(express.json());

app.get(
  "/api/decode_detached_signature",
  (req: Request, res: Response<ResponseModel>) => {
    const decodedSignature =
      "signature" in req.body
        ? new DecodeDetachedSignature(req.body.signature)
        : undefined;
    res.json({
      hasError: decodedSignature?.signedData ? false : true,
      data: decodedSignature?.signing_structure ?? null,
    });
  },
);

app.listen(PORT, () => {
  console.log(`🚀 Сервер запущен на порту ${PORT}`);
});
