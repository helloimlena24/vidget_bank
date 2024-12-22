import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def fixture_masks_card_number():
    return "2134765899800077"


def test_get_mask_card_number(fixture_masks_card_number):
    assert get_mask_card_number(fixture_masks_card_number) == "2134 76** **** 0077"


@pytest.fixture
def fixture_masks_account():
    return "64686473678894779589"


def test_get_mask_account(fixture_masks_account):
    assert get_mask_account(fixture_masks_account) == "**9589"