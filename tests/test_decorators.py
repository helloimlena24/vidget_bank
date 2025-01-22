import pytest

# Импортируем декоратор из модуля
from src.decorators import log, predicate_is_filter, predicate_is_sort, predicate_is_mask


def test_log_function_success(capsys):
    @log(lambda x: x > 0, "Value must be positive")
    def test_function(x):
        return x + 1

    result = test_function(5)
    assert result == 6

    captured = capsys.readouterr()
    assert "Getting started with the test_function" in captured.out
    assert "Finished the function" in captured.out


def test_log_function_failure(capsys):
    @log(lambda x: x > 10, "Value must be greater than 10")
    def test_function(x):
        return x + 1

    with pytest.raises(ValueError, match="Value must be greater than 10"):
        test_function(5)

    captured = capsys.readouterr()
    assert "test_function" in captured.out
    assert "Error: Value must be greater than 10" in captured.out
    assert "Inputs: (5,)" in captured.out


def test_predicate_is_filter():
    assert (
        predicate_is_filter(
            None,
            [
                {"id": 41428829, "state": "EXECUTED", "date": " 2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )[1]
        is True
    )

    assert predicate_is_filter(None, [])[1] is False


def test_predicate_is_sort():
    assert predicate_is_sort(None, True)[1] is False
    assert predicate_is_sort(None, False)[1] is False


def test_predicate_is_mask():
    assert predicate_is_mask("1234567891234567") is True
    assert predicate_is_mask("wrong_mask") is False
