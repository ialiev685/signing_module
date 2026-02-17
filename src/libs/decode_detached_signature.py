from pyasn1.codec.der import decoder
from pyasn1_modules import rfc5652, rfc2315  # type: ignore


path_signature = "src/test_signature/test_detached_signature.sig"
oid_signed_data = "1.2.840.113549.1.7.2"


class DecodeDetachedSignature:
    signed_data: rfc5652.SignedData = None

    def __init__(self):

        with open(path_signature, "rb") as file:
            try:
                decoded_value, _ = decoder.decode(
                    file.read(), asn1Spec=rfc5652.ContentInfo()
                )
                if (
                    isinstance(decoded_value, rfc5652.ContentInfo)
                    and "content" in decoded_value
                ):

                    signed_data, _ = decoder.decode(
                        decoded_value["content"], rfc5652.SignedData()
                    )

                    print("signed_data", signed_data["certificates"])

            except Exception as error:
                print("error by decode content info: ", error)
