import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 0000646864736788947795890000", "Неверный формат"),
        ("", "Передана пустая строка"),
        ("Visa 2134765899800077", "Visa 2134 76** **** 0077"),
        ("Visa 000064686947795890000", "Неверный формат"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", "Ошибка: Ввод пустой."),
        ("756432980184-02", "Ошибка: Неправильный формат даты."),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
