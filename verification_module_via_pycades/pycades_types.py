from typing import Callable, Generic, TypeVar, Any, Type

T = TypeVar("T")


class HashedData:
    Algorithm: int
    DataEncoding: int
    Hash: Callable[[str], None]
    Value: str
    SetHashValue: Callable[[str], None]


class RequestDataByItem(Generic[T]):
    Count: int
    Item: Callable[[int], T]


class OID:
    name: str
    OID: str


class ExtendedKeyUsage(Generic[T]):
    EKUs: RequestDataByItem[OID]


class Certificate:
    SubjectName: str
    IssuerName: str
    Thumbprint: str | None
    ValidFromDate: str
    ValidToDate: str
    SerialNumber: str
    ExtendedKeyUsage: Callable[[], ExtendedKeyUsage]
    Import: Callable[[bytes], None]


class Signers:
    Certificate: Certificate
    SignatureTimeStampTime: str | None
    SigningTime: str


class StoreCertificates:
    Find: Callable[[Any, Any], RequestDataByItem[Certificate]]
    Count: int
    Item: Callable[[int], Certificate]


class Store:

    Open: Callable[[int, str, int], None]
    Add: Callable[[Certificate], None]
    Remove: Callable[[Certificate], None]
    Certificates: StoreCertificates


class SignedData:
    GetMsgType: Callable[[str], int]
    VerifyHash: Callable[[HashedData, str, int], dict]
    Certificates: RequestDataByItem[Certificate]
    Signers: RequestDataByItem[Signers]


class Pycades:
    # Thumbprint
    CAPICOM_CERTIFICATE_FIND_SHA1_HASH: int
    # алгоритм кодировки
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

    HashedData: Callable[[None], HashedData]
    SignedData: Callable[[None], SignedData]
    Store: Callable[[None], Store]
    Certificate: Callable[[None], Certificate]
