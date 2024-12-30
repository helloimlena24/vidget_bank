import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(inf_card: str) -> str:
    """Функция маскирует информацию и о картах, и о счетах"""
    try:

        if re.search(r"сч[её]т", inf_card, re.IGNORECASE) and len(inf_card[5:]) == 20:
            return f"{inf_card[:4]} {get_mask_account(inf_card[-20:])}"
        elif len(inf_card[5:]) > 20:
            return "Неверный формат"

        elif not re.search(r"сч[её]т", inf_card, re.IGNORECASE):
            match = re.search(r"\d+", inf_card)
            if match is not None:
                if len(match.group()) == 16:
                    return f"{inf_card[:-17]} {get_mask_card_number(inf_card[-16:])}"
                else:
                    return "Неверный формат"

            else:
                return "Передана пустая строка"

    except ValueError:
        return "Неверный формат"

    return "Неверный формат"


def get_date(date_input: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"."""
    if not date_input:
        return "Ошибка: Ввод пустой."

    try:

        date_obj = datetime.fromisoformat(date_input)

        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: Неправильный формат даты."
