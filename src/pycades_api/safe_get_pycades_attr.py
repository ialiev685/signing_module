def safe_get_com_attr(object, attr_name, default=None):
    """
    Безопасно получает атрибут COM-объекта
    """
    if object is None:
        return default

    try:
        return getattr(object, attr_name)
    except Exception:
        return default
