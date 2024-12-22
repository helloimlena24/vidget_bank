# from src.masks import get_mask_account, get_mask_card_number
#
#
# def mask_account_card(inf_card: str) -> str:
#     """Функция маскирует информацию и о картах, и о счетах"""
#     if "Счет" in inf_card:
#         return f"{inf_card[:4]} {get_mask_account(inf_card[-4:])}"
#     else:
#         return f"{inf_card[:-17]} {get_mask_card_number(inf_card[-16:])}"
#
#
# def get_date(date: str) -> str:
#     """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
#     return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
#
#
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("Visa 2134765899800077"))