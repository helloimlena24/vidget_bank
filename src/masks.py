from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция маскирует номер банковской карты"""

    if not card_num:
        raise ValueError("Передана пустая строка")
    elif len(card_num) != 16:
        raise ValueError("Неверное количество символов")

    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(account_num: Union[str]) -> Union[str]:
    """Функция маскирует номер банковского счета"""

    if not account_num:
        raise ValueError("Передана пустая строка")
    elif len(account_num) != 20:
        raise ValueError("Неверное количество символов")

    return f"**{account_num[-4:]}"
