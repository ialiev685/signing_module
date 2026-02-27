from typing import Dict, TypedDict


class AlgorithmInfo(TypedDict):
    oid: str
    name_code: str


class SubjectInfo(TypedDict):
    oid: str
    translation: str
    name_code: str


# Константы для алгоритмов
ALGORITHM_OIDS: Dict[str, AlgorithmInfo] = {
    "1.2.643.7.1.1.1.1": {
        "oid": "1.2.643.7.1.1.1.1",
        "name_code": "ГОСТ Р 34.10-2012 256 бит",
    },
    "1.2.643.7.1.1.2.2": {
        "oid": "1.2.643.7.1.1.2.2",
        "name_code": "ГОСТ Р 34.11-2012 256 бит",
    },
    "1.2.643.7.1.1.3.2": {
        "oid": "1.2.643.7.1.1.3.2",
        "name_code": "ГОСТ Р 34.11-2012/34.10-2012 256 бит",
    },
}

# OID времени подписи
SIGNING_TIME_OID = "1.2.840.113549.1.9.5"

# OID CMS/PKCS7
OID_SIGNED_DATA = "1.2.840.113549.1.7.2"  # contentType

# OID для субъектов сертификата
SUBJECT_OIDS: Dict[str, SubjectInfo] = {
    "2.5.4.6": {
        "oid": "2.5.4.6",
        "translation": "Страна",
        "name_code": "C",
    },
    "2.5.4.42": {
        "oid": "2.5.4.42",
        "translation": "Имя Отчество",
        "name_code": "G",
    },
    "2.5.4.4": {
        "oid": "2.5.4.4",
        "translation": "Фамилия",
        "name_code": "SN",
    },
    "2.5.4.3": {
        "oid": "2.5.4.3",
        "translation": "Владелец",
        "name_code": "CN",
    },
    "2.5.4.10": {
        "oid": "2.5.4.10",
        "translation": "Организация",
        "name_code": "O",
    },
    "2.5.4.9": {
        "oid": "2.5.4.9",
        "translation": "Адрес",
        "name_code": "STREET",
    },
    "2.5.4.7": {
        "oid": "2.5.4.7",
        "translation": "Город",
        "name_code": "L",
    },
    "2.5.4.8": {
        "oid": "2.5.4.8",
        "translation": "Регион",
        "name_code": "S",
    },
    "1.2.643.100.1": {
        "oid": "1.2.643.100.1",
        "translation": "ОГРН",
        "name_code": "ОГРН",
    },
    "1.2.643.100.3": {
        "oid": "1.2.643.100.3",
        "translation": "СНИЛС",
        "name_code": "SN",
    },
    "1.2.643.100.4": {
        "oid": "1.2.643.100.4",
        "translation": "ИНН ЮЛ",
        "name_code": "ИНН ЮЛ",
    },
    "1.2.840.113549.1.9.1": {
        "oid": "1.2.840.113549.1.9.1",
        "translation": "Email",
        "name_code": "E",
    },
    "2.5.4.12": {
        "oid": "2.5.4.12",
        "translation": "Должность",
        "name_code": "T",
    },
    "1.2.643.3.131.1.1": {
        "oid": "1.2.643.3.131.1.1",
        "translation": "ИНН",
        "name_code": "ИНН",
    },
}
