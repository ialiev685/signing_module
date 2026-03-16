import subprocess

from models_types import ResponseDataModel, StoreName
from utils.parse_certmgr_output import parse_certmgr_output


def remove_certificate_from_store(
    thumbprint: str, store_name: StoreName
) -> ResponseDataModel:

    try:
        result = subprocess.run(
            [
                "/opt/cprocsp/bin/amd64/certmgr",
                "-delete",
                "-store",
                store_name,
                "-thumbprint",
                thumbprint,
            ],
            capture_output=True,
            check=True,
            text=True,
        )
        parsed_result = parse_certmgr_output(result.stdout)
        return ResponseDataModel(
            data=parsed_result[0] if len(parsed_result) > 0 else None
        )
    except Exception as error:
        print("Ошибка при сохранении данных сертификата в стор через консоль: ", error)
        return ResponseDataModel(has_error=True, error=error, data=None)
    # через pycades вызов данных стора не отрабатывают корректно

    # store = pycades_engine.Store()
    # store.Open(
    # pycades_engine.CAPICOM_CURRENT_USER_STORE,
    # pycades_engine.CAPICOM_LOCAL_MACHINE_STORE,
    # ===
    # pycades_engine.CAPICOM_ROOT_STORE,
    # pycades_engine.CAPICOM_CA_STORE,
    # pycades_engine.CAPICOM_MY_STORE,
    # ===
    # pycades_engine.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED,
    # )

    # found_certificate = store.Certificates.Find(
    #     pycades_engine.CAPICOM_CERTIFICATE_FIND_SHA1_HASH, thumbprint
    # )

    #  try:
    # if found_certificate.Count > 0:
    # certificate = found_certificate.Item(1)

    # store.Remove(certificate)
    # store.Close()

    # except Exception as error:
    # print("error", error)
