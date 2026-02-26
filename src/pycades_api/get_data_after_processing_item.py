from pycades_types import RequestDataByItem, T


def get_data_after_processing_item(object_data: RequestDataByItem[T]) -> list[T]:
    if object_data is None:
        return []

    try:
        object_count = object_data.Count
        data_array = []
        for index in range(object_count):
            item = object_data.Item(index + 1)

            data_array.append(item)

        return data_array

    except Exception as error:
        print("Ошибка при обработке/итерации через метод Item", error)
        return []
