from typing import Dict, TypedDict
from enum import Enum


class AlgorithmInfo(TypedDict):
    oid: str
    nameCode: str


class SubjectInfo(TypedDict):
    oid: str
    translation: str
    nameCode: str


# Константы для алгоритмов
ALGORITHM_OIDS: Dict[str, AlgorithmInfo] = {
    "1.2.643.7.1.1.1.1": {
        "oid": "1.2.643.7.1.1.1.1",
        "nameCode": "ГОСТ Р 34.10-2012 256 бит",
    },
    "1.2.643.7.1.1.2.2": {
        "oid": "1.2.643.7.1.1.2.2",
        "nameCode": "ГОСТ Р 34.11-2012 256 бит",
    },
    "1.2.643.7.1.1.3.2": {
        "oid": "1.2.643.7.1.1.3.2",
        "nameCode": "ГОСТ Р 34.11-2012/34.10-2012 256 бит",
    },
}

# OID времени подписи
SIGNING_TIME_OID = "1.2.840.113549.1.9.5"

# OID для субъектов сертификата
SUBJECT_OIDS: Dict[str, SubjectInfo] = {
    "2.5.4.6": {
        "oid": "2.5.4.6",
        "translation": "Страна",
        "nameCode": "C",
    },
    "2.5.4.42": {
        "oid": "2.5.4.42",
        "translation": "Имя Отчество",
        "nameCode": "G",
    },
    "2.5.4.4": {
        "oid": "2.5.4.4",
        "translation": "Фамилия",
        "nameCode": "SN",
    },
    "2.5.4.3": {
        "oid": "2.5.4.3",
        "translation": "Владелец",
        "nameCode": "CN",
    },
    "2.5.4.10": {
        "oid": "2.5.4.10",
        "translation": "Организация",
        "nameCode": "O",
    },
    "2.5.4.9": {
        "oid": "2.5.4.9",
        "translation": "Адрес",
        "nameCode": "STREET",
    },
    "2.5.4.7": {
        "oid": "2.5.4.7",
        "translation": "Город",
        "nameCode": "L",
    },
    "2.5.4.8": {
        "oid": "2.5.4.8",
        "translation": "Регион",
        "nameCode": "S",
    },
    "1.2.643.100.1": {
        "oid": "1.2.643.100.1",
        "translation": "ОГРН",
        "nameCode": "ОГРН",
    },
    "1.2.643.100.3": {
        "oid": "1.2.643.100.3",
        "translation": "СНИЛС",
        "nameCode": "SN",
    },
    "1.2.643.100.4": {
        "oid": "1.2.643.100.4",
        "translation": "ИНН ЮЛ",
        "nameCode": "ИНН ЮЛ",
    },
    "1.2.840.113549.1.9.1": {
        "oid": "1.2.840.113549.1.9.1",
        "translation": "Email",
        "nameCode": "E",
    },
    "2.5.4.12": {
        "oid": "2.5.4.12",
        "translation": "Должность",
        "nameCode": "T",
    },
    "1.2.643.3.131.1.1": {
        "oid": "1.2.643.3.131.1.1",
        "translation": "ИНН",
        "nameCode": "ИНН",
    },
}
