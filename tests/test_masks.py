from typing import Tuple

import pytest

from src.masks import get_mask_account, get_mask_card_number

"""Проверка положительных сценариев в функциях модуля"""


@pytest.fixture
def fixture_masks_card_number() -> str:
    return "2134765899800077"


def test_get_mask_card_number(fixture_masks_card_number: str) -> None:
    assert get_mask_card_number(fixture_masks_card_number) == "2134 76** **** 0077"


@pytest.fixture
def fixture_masks_account() -> str:
    return "64686473678894779589"


def test_get_mask_account(fixture_masks_account: str) -> None:
    assert get_mask_account(fixture_masks_account) == "**9589"


"""Проверка отрицательных сценариев в функциях модуля"""


def test_get_mask_card_number_error(fixture_for_num_card_or_account: Tuple[str, str]) -> None:
    number_card_or_account, expected_error = fixture_for_num_card_or_account
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(number_card_or_account)
    assert str(exc_info.value) == expected_error


def test_get_mask_account_error(fixture_for_num_card_or_account: Tuple[str, str]) -> None:
    number_card_or_account, expected_error = fixture_for_num_card_or_account
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(number_card_or_account)
    assert str(exc_info.value) == expected_error
