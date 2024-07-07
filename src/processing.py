from datetime import datetime
from typing import Dict, List


def sorting_dict_status(user_dictionary: list, status: str = "EXECUTED") -> list:
    """Сортирует список по значению status"""
    list_correct = []
    for i in user_dictionary:
        for k in i.keys():
            if status == "EXECUTED":
                if i[k] == "EXECUTED":
                    list_correct.append(i)

            elif status == "PENDING":
                if i[k] == "PENDING":
                    list_correct.append(i)
            else:
                if i[k] == "CANCELED":
                    list_correct.append(i)
    return list_correct


def sorting_dict_reverse(user_time: list, flag: bool = False) -> list:
    """сортирует по убыванию, возрастанию"""
    user_time = sorted(
        user_time,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=flag,
    )
    return user_time


def sorting_by_date(list_of_dictionaries: List[Dict], flag: bool = True) -> List[Dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию или возрастанию даты (ключ 'date')."""
    sorted_list = sorted(
        list_of_dictionaries, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%SZ"), reverse=flag
    )
    return sorted_list
