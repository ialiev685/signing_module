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


class Certificate:
    SubjectName: str
    IssuerName: str


class Store:
    class CertificateCollections:
        Count: int
        Item: Callable[[int], Certificate]

    Certificates: CertificateCollections
    Open: Callable[[int, str, int], None]


class Pycades:
    CADESCOM_HASH_ALGORITHM_CP_GOST_3411_2012_256: int
    CADESCOM_BASE64_TO_BINARY: int

    # 1 параметр для Open
    CAPICOM_CURRENT_USER_STORE: int  # хранилище юзера
    CAPICOM_LOCAL_MACHINE_STORE: int  # локальное хранилище машины
    CADESCOM_CONTAINER_STORE: int
    # 2 параметр для Open
    CAPICOM_MY_STORE: str  # личные сертификаты
    CAPICOM_CA_STORE: str  # промежуточные сертификаты
    CAPICOM_ROOT_STORE: str  # корневые сертификаты
    # 3 параметр для Open
    CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED: int

    HashedData: Type[HashedData]
    SignedData: Type[SignedData]
    Store: Type[Store]
