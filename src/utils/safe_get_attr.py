def safe_get_attr(object, attr_name):
    """
    Безопасно получает атрибут COM-объекта
    """
    try:
        if object is None:
            return None

        return getattr(object, attr_name)
    except Exception:
        return None
