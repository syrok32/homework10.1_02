from datetime import datetime


def sorting_dict_status(user_dictionary: list, status: str = "EXECUTED") -> list:
    """Сортирует список по status"""
    list_correct = []
    for i in user_dictionary:
        for k in i.keys():
            if status == "EXECUTED":
                if i[k] == "EXECUTED":
                    list_correct.append(i)
            else:
                if i[k] == "CANCELED":
                    list_correct.append(i)
    return list_correct


def sorting_dict_reverse(user_time: list, flag: bool = False) -> list:
    """сортирует по убыванию, возрастанию"""
    sorted(
        user_time,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=flag,
    )
    return user_time
