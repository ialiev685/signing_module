from typing import Callable, Type


class HashedData:
    Algorithm: Callable[[int], None]
    Hash: Callable[[str], None]
    Value: str


class CadesSignedData:
    GetMsgType: Callable[[str], int]


class Pycades:
    CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256: int

    HashedData: Type[HashedData]
    CadesSignedData: Type[CadesSignedData]
