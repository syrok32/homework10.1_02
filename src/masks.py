def mask_card(card_number: str) -> str:
    """Возврощает маску карты"""
    card_number = card_number.replace(card_number[6:12], "******")
    return card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:]


def mask_check(account_number: str) -> str:
    """Возвращает мвску счета"""
    return f"**{account_number[-4:]}"
