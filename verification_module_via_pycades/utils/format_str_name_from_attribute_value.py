from models_types import AttributeValueModel


def format_str_name_from_attribute_value(
    attributes: list[AttributeValueModel] | None,
) -> str:
    if attributes is None:
        return ""
    return ", ".join([f"{attr.name_code}={attr.value}" for attr in attributes])
