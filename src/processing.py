from datetime import datetime
from typing import Dict, List


def filter_by_state(list_dict: List[Dict], value_key: str = "EXECUTED") -> List[Dict] | str:
    """Функция возвращает новый список словарей,
    у которых ключ state соответствует указанному значению,
    по умолчанию 'EXECUTED'"""

    if list_dict == [{}]:
        raise ValueError("Пустое значение")

    elif [
        every_dict
        for every_dict in list_dict
        if every_dict["state"] != "EXECUTED" and every_dict["state"] != "CANCELED"
    ]:
        raise ValueError("Неверный формат ввода поля 'state'")

    else:
        new_list_dict = []
        for every_dict in list_dict:
            if every_dict["state"] == value_key:
                new_list_dict.append(every_dict)

        return new_list_dict


def sort_by_date(list_dict: List[Dict], arg_for_sort: bool = True) -> List[Dict] | str:
    """Функция, сортирует (по умолчанию - убывание) и возвращает новый список, отсортированный по дате"""

    # Преобразуем строки дат в объекты datetime
    for item in list_dict:
        try:
            item["date"] = datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError(f"Invalid date format: {item['date']}")

    # Сортируем данные
    sorted_data = sorted(list_dict, key=lambda x: x["date"], reverse=arg_for_sort)

    # Преобразуем обратно к исходному формату
    for item in sorted_data:
        item["date"] = item["date"].isoformat()

    return sorted_data


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)
