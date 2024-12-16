from typing import List, Dict


def filter_by_state(list_dict: List[Dict], value_key: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает новый список словарей,
    у которых ключ state соответствует указанному значению,
    по умолчанию 'EXECUTED'"""
    new_list_dict = []

    for every_dict in list_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date(list_dict: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    """Функция, сортирует (по умолчанию - убывание) и возвращает новый список, отсортированный по дате"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_for_sort)
    return sort_list
