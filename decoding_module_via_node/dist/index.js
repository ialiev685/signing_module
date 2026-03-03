"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const decode_detached_signature_1 = require("./decode-detached-signature");
const app = (0, express_1.default)();
const PORT = process.env.PORT || 8005;
app.use(express_1.default.json());
app.post("/api/decode_detached_signature", (req, res) => {
    const decodedSignature = "signature" in req.body
        ? new decode_detached_signature_1.DecodeDetachedSignature(req.body.signature)
        : undefined;
    res.json({
        data: decodedSignature?.signing_structure ?? null,
    });
});
app.listen(PORT, () => {
    console.log(`🚀 Микросервис "decoding-service" запущен на порту ${PORT}`);
});
