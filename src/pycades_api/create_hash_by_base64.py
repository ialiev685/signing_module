from pycades_engine import pycades_engine


def create_hash_by_base64(value: str):
    """
    Docstring для create_hash

    :param value: Файл в формате base64
    :type value: str
    """
    hashed_data = pycades_engine.HashedData()
    hashed_data.Algorithm = pycades_engine.CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256
    hashed_data.DataEncoding = pycades_engine.CADESCOM_BASE64_TO_BINARY
    hashed_data.Hash(value)
    return hashed_data.Value
