from pyasn1.codec.der import decoder


# Internet X.509 Public Key Infrastructure Certificate and Certificate
from pyasn1_modules import rfc5280  # type: ignore

from ..oid_configs import SUBJECT_OIDS
from ..action_models import AttributeValueModel, ResponseDataModel


def parse_attributes_value(
    rdn_attributes: rfc5280.RDNSequence,
) -> list[AttributeValueModel]:
    values: list[AttributeValueModel] = []
    for rdn in rdn_attributes:
        for attribute in rdn:
            value_encoded = attribute["value"]
            type = str(attribute["type"])
            value_parsed, _ = decoder.decode(value_encoded)
            if type in SUBJECT_OIDS:
                values.append(
                    AttributeValueModel(**SUBJECT_OIDS[type], value=str(value_parsed))
                )
    return values
