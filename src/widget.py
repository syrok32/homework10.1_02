import re

from src.masks import mask_card, mask_check


def mask_card_and_check(number: str) -> str:
    """Возврощает маску карты и счета"""

    list_account = number.split()
    list_number = list()
    list_data = list()
    for i in list_account:
        if i.isdigit():
            list_number.append(i)
        else:
            list_data.append(i)
    word = "".join(list_data).strip()

    if bool(re.search('[а-яА-Я]', list_data[0])):

        check_mask_account = mask_check(''.join(list_number))

        return f'{word} {check_mask_account}'

    else:
        card_mask_account = mask_card(''.join(list_number))

        return f'{''.join(list_data)} {card_mask_account}'


def time_correct(mask_time : str) -> str:
    """расшифровывает маску"""
    list_time = mask_time.split('T')
    string_time = ''.join(list_time[0])
    list_time_correct = string_time.split('-')
    data = '.'.join(list_time_correct[::-1])
    return data
