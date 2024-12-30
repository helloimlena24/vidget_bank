from typing import List, Dict

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "inp_list_dict, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_filter_by_state(inp_list_dict: List[Dict], expected: List[Dict] | str) -> None:
    assert filter_by_state(inp_list_dict) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ([{}], "Пустое значение"),
        (
            [{"id": 41428829, "state": "RANDOM", "date": "2019-07-03T18:35:29.512364"}],
            "Неверный формат ввода поля 'state'",
        ),
    ],
)
def test_invalid_filter_by_state(value: List[Dict], expected: List[Dict] | str) -> None:
    with pytest.raises(ValueError) as ex_info:
        filter_by_state(value)
    assert str(ex_info.value) == expected


@pytest.mark.parametrize(
    "input_data, arg_for_sort, expected",
    [
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            False,
            [
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            True,
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            False,
            [
                {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(input_data: List[Dict], arg_for_sort: bool, expected: List[Dict] | str) -> None:
    result = sort_by_date(input_data, arg_for_sort)
    assert result == expected


@pytest.mark.parametrize(
    "input_data",
    [
        [
            {"id": 1, "state": "EXECUTED", "date": "invalid-date"},
            {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        [
            {"id": 1, "state": "EXECUTED", "date": "30-06-2018 02:08:58"},
            {"id": 2, "state": "EXECUTED", "date": "03-07-2019 18:35:29"},
        ],
    ],
)
def test_sort_with_invalid_date(input_data: List[Dict]) -> None:
    with pytest.raises(ValueError):
        sort_by_date(input_data, False)
