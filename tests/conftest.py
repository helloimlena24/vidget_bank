from typing import Tuple

import pytest


@pytest.fixture(
    params=[
        ("", "Передана пустая строка"),
        ("12345", "Неверное количество символов"),
        ("123451234512345123451234512345", "Неверное количество символов"),
    ]
)
def fixture_for_num_card_or_account(request) -> Tuple[str, str]:
    return request.param
