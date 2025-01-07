from typing import List, Dict, Iterator

def filter_by_currency(get_transacts: List[Dict], currency: str = "USD") -> Iterator[list]|str:
    """
Функция принимает на вход список словарей, представляющих транзакции.
Функция должна возвращать итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной (например, USD).

Args:
    get_transacts(List[Dict]): список словарей,
    currency: str: валюта транзакции.

Returns:
        Iterator([list]) - итератор, который поочередно выдает транзакции.

"""
    iterator_for_transacts = (transact for transact in get_transacts if transact['operationAmount']['currency']['name'] == currency)

    list_transact = list(iterator_for_transacts)


    for transact in list_transact:
        yield transact



def transaction_descriptions(list_with_trans: List[Dict]) -> Iterator[str]:
    """Генераторная функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    for transact in list_with_trans:
        try:
            yield transact['description']
        except KeyError:
            yield "пустое описание"


def card_number_generator(start: int, end: int) -> str:
    """
Функция выдает номера банковских карт в формате 'XXXX XXXX XXXX XXXX', где X— цифра номера карты.
start: начальное значение диапазона от 0000 0000 0000 0001
end: конечное значение диапазона до 9999 9999 9999 9999.

Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError(
            "Диапазон должен быть от 1 до 9999999999999999 и начальное значение должно быть меньше или равно конечному.")

    for number in range(start, end + 1):
        # Форматируем номер карты
        formatted_number = f"{number:016d}"  # 016d указывает, что число должно быть представлено в десятичном виде (d)
        # с добавлением ведущих нулей до 16 символов (016).
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"


