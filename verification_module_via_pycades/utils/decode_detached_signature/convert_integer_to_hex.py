from pyasn1_modules import rfc5280  # type: ignore


def convert_integer_to_hex(value: rfc5280.CertificateSerialNumber):
    try:
        return "0" + hex(value)[2:].upper()
    except Exception as error:
        print("Ошибка при конвертации значения INTEGER в HEX: ", error)
        return None
