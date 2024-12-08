from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция маскирует номер банковской карты"""

    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(account_num: Union[str]) -> Union[str]:
    """Функция маскирует номера банковского счета"""
    return f"**{account_num[:4]}"
