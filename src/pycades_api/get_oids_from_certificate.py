from .get_data_after_processing_item import get_data_after_processing_item
from pycades_types import Certificate


def get_oids_from_certificate(certificate: Certificate):

    try:

        ekus_object = certificate.ExtendedKeyUsage().EKUs
        oids = get_data_after_processing_item(ekus_object)
        oid_value_array = [oid.OID for oid in oids]

        return oid_value_array

    except Exception as error:
        print("Ошибка при получении 'Extended Key Usage(OIDs)'", error)
        return []
