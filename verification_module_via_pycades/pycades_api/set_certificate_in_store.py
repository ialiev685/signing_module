from pycades_engine import pycades_engine
import subprocess
import os

from models_types import ResponseDataModel, StoreName
from utils.parse_certmgr_output import parse_certmgr_output


def set_certificates_from_store(
    file: bytes, filename: str, store_name: StoreName
) -> ResponseDataModel:
    try:
        root_app = os.getcwd()
        temp_dir_path = os.path.join(root_app, "temp_files")
        if not os.path.exists(temp_dir_path):
            os.mkdir(temp_dir_path)
        temp_file_path = os.path.join(temp_dir_path, filename)

        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file)

        result = subprocess.run(
            [
                "/opt/cprocsp/bin/amd64/certmgr",
                "-inst",
                "-all",
                "-store",
                store_name,
                "-file",
                temp_file_path,
            ],
            capture_output=True,
            check=True,
            text=True,
        )

        os.unlink(temp_file_path)
        parsed_result = parse_certmgr_output(result.stdout)
        return ResponseDataModel(
            data=parsed_result[0] if len(parsed_result) > 1 else None
        )
    except Exception as error:
        print("Ошибка при сохранении данных сертификата в стор через консоль: ", error)
        return ResponseDataModel(has_error=True, error=error, data=None)

    # через pycades вызов данных стора не отрабатывают корректно

    # store = pycades_engine.Store()
    # store.Open(
    # pycades_engine.CAPICOM_CURRENT_USER_STORE,
    # pycades_engine.CAPICOM_LOCAL_MACHINE_STORE,
    # ======
    # pycades_engine.CAPICOM_ROOT_STORE,
    # pycades_engine.CAPICOM_CA_STORE,
    # pycades_engine.CAPICOM_MY_STORE,
    # ======
    # pycades_engine.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED,
    # )
    # certificate_object = pycades_engine.Certificate()
    # certificate_object.Import(file)
    # store.Add(certificate_object)

    # print(os.path.dirname(__file__))
    # print(os.path.basename(__file__))
    # print(os.getcwd())
    # response = store.Certificates.Find(
    #     pycades_engine.CAPICOM_CERTIFICATE_FIND_SHA1_HASH, certificate_object.Thumbprint
    # )

    # if response.Count > 0:
    #     found_certificate = response.Item(1)
    #     if found_certificate.Thumbprint == cert.Thumbprint:
    #         print(
    #             "Сертификат с такими отпечатком уже имеется: ",
    #             found_certificate.Thumbprint,
    #         )
