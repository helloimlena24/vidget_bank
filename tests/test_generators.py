import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency():
    get_transact = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    generator = filter_by_currency(get_transact)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


@pytest.fixture()
def fixture_filter_by_currency_invalid():
    get_transact = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "none", "code": "none"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    return get_transact


def test_filter_by_currency_invalid(fixture_filter_by_currency_invalid):
    result = list(filter_by_currency(fixture_filter_by_currency_invalid, "USD"))
    assert result == []


def test_empty_filter_by_currency():
    get_transact = []
    result = list(filter_by_currency(get_transact))
    assert result == []


@pytest.mark.parametrize(
    "value, expected",
    [
        (list(card_number_generator(1, 3)), ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (
            list(card_number_generator(9999999999999991, 9999999999999993)),
            ["9999 9999 9999 9991", "9999 9999 9999 9992", "9999 9999 9999 9993"],
        ),
    ],
)
def test_card_number_generator(value, expected):
    assert value == expected


def test_correct_nums_card_card_number_generator():
    """Проверяет генерацию номеров в правильном формате и крайние значения диапазона"""
    generator_card = next(card_number_generator(0o00000000000001, 0o0000000000001))
    expected_res = "0000 0000 0000 0001"
    assert generator_card == expected_res


@pytest.mark.parametrize(
    "transactions, expected",
    [
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        ([{"description": "Перевод со счета на счет"}], ["Перевод со счета на счет"]),
        ([{}], ["пустое описание"]),
    ],
)
def test_transaction_descriptions(transactions, expected):
    descriptions = transaction_descriptions(transactions)
    assert list(descriptions) == expected
