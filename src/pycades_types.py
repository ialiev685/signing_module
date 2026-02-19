from typing import Callable, Type


class HashedData:
    Algorithm: int
    DataEncoding: int
    Hash: Callable[[str], None]
    Value: str
    SetHashValue: Callable[[str], None]


class SignedData:
    GetMsgType: Callable[[str], int]
    VerifyHash: Callable[[HashedData, str, int], dict]


class Pycades:
    CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256: int
    CADESCOM_BASE64_TO_BINARY: int
    HashedData: Type[HashedData]
    SignedData: Type[SignedData]
