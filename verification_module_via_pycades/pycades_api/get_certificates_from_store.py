import subprocess
from models_types import (
    CertificateInfoModel,
    StoreName,
    ResponseDataModel,
)
from utils.parse_certmgr_output import parse_certmgr_output


def get_certificates_from_store(
    store_name: StoreName,
) -> ResponseDataModel[list[CertificateInfoModel]]:
    try:

        result = subprocess.run(
            [
                "/opt/cprocsp/bin/amd64/certmgr",
                "-list",
                "-store",
                store_name,
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return ResponseDataModel(data=parse_certmgr_output(result.stdout))
    except Exception as error:
        print("Ошибка при выполнении запроса данных из стора через консоль: ", error)
        return ResponseDataModel(has_error=True, error=error, data=None)

    # через pycades вызов данных стора не отрабатывают корректно

    # store = pycades_engine.Store()
    # store.Open(
    #     pycades_engine.CAPICOM_LOCAL_MACHINE_STORE,
    #     # pycades_engine.CADESCOM_CONTAINER_STORE,
    #     # pycades_engine.CAPICOM_CURRENT_USER_STORE,
    #     # ======
    #     pycades_engine.CAPICOM_ROOT_STORE,
    #     # pycades_engine.CAPICOM_CA_STORE,
    #     # pycades_engine.CAPICOM_MY_STORE,
    #     # ======
    #     pycades_engine.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED,
    # )

    # if store.Certificates.Count > 0:
    #     for index, cert in enumerate(range(1, 10)):
    #         got_cert = store.Certificates.Item(index + 1)
