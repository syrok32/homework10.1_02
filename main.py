from typing import Any, Dict, List, Tuple

from src.processing import sorting_by_date, sorting_dict_reverse, sorting_dict_status
from src.read_csv_xlsx import reader_csv_file, reader_xlsx_file
from src.search import search_str
from src.utils import loads_json
from src.widget import mask_card_and_check, time_correct


def choose_format_read() -> Tuple[List[Dict[str, Any]], int]:
    """определяет откуда будут читаться данные"""
    user_number = int(
        input(
            """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из json файла
    2. Получить информацию о транзакциях из csv файла
    3. Получить информацию о транзакциях из xlsx файла\n"""
        )
    )

    if user_number == 1:
        print("Для обработки выбран json файл.")
        json_file = loads_json("data/operations.json")
        return json_file, 1

    elif user_number == 2:
        print("Для обработки выбран csv файл.")
        csv_file = reader_csv_file("data/transactions.csv")
        return csv_file, 2

    elif user_number == 3:
        xlsx_file = reader_xlsx_file("data/transactions_excel.xlsx")
        print("Для обработки выбран xlsx файл.")
        return xlsx_file, 3

    else:
        return [], 0


def filter_status(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтрует по статусу"""
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        user_filter = (
            input(
                "Введите статус по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                "Пользователь: "
            )
            .strip()
            .upper()
        )

        if user_filter in valid_statuses:
            if user_filter.upper() == "EXECUTED":
                return sorting_dict_status(data)
            if user_filter.upper() == "CANCELED":
                return sorting_dict_status(data, "CANCELED")
            if user_filter.upper() == "PENDING":
                return sorting_dict_status(data, "PENDING")
            return data
            break
        else:
            print(f'Статус операции "{user_filter}" недоступен.\n')


def filter_up_down(data: List[Dict[str, Any]], num: int) -> Any:
    """фильтрует по дате"""
    user_filter = input("Отсортировать операции по дате? Да/Нет\n")
    if user_filter.lower() == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n")
        if sort_order.lower() == "по убыванию":
            if num == 1:
                return sorting_dict_reverse(data)
            if num in [2, 3]:
                return sorting_by_date(data)
        if sort_order.lower() == "по возрастанию":
            if num == 1:
                return sorting_dict_reverse(data, flag=False)
            if num in [2, 3]:
                return sorting_by_date(data, flag=False)
    return data


def filter_rub(data: List[Dict[str, Any]], num: int) -> List[Dict[str, Any]]:
    """возврозыет словари с RUB"""
    user_filter = input("Выводить только рублевые тразакции? Да/Нет\n")
    if user_filter.lower() == "да":
        if num in [2, 3]:
            return [transaction for transaction in data if transaction["currency_code"] == "RUB"]
        if num == 1:
            return [i for i in data if i["operationAmount"]["currency"]["code"] == "RUB"]
    return data


def filter_to_world(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """поиск слова в значених"""
    user_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if user_filter.lower() == "да":
        user_answer = input("Введите слово")
        print("Распечатываю итоговый список транзакций...")
        return search_str(data, user_answer)
    print("Распечатываю итоговый список транзакций...")
    return data


def end_answer(data: Any, num: int) -> Any:
    """красиво ввыводит ответ"""
    if num == 1:
        print(f"Всего банковских операций в выборке {len(data)}:")
        for i in data:
            if i["description"] == "Открытие вклада":
                print(
                    f"""
            {time_correct(i['date'])} {i['description']}
            {mask_card_and_check(i['to'])}
            Сумма: {i["operationAmount"]["amount"]}{i['operationAmount']['currency']["code"]}"""
                )
            else:
                print(
                    f"""
            {time_correct(i['date'])} {i['description']}
            {mask_card_and_check(i['from'])} -> {mask_card_and_check(i['to'])}
            Сумма: {i["operationAmount"]["amount"]}{i['operationAmount']['currency']["code"]}"""
                )

    elif num in [2, 3]:
        print(f"Всего банковских операций в выборке: {len(data)}")

        for i in data:
            if i["description"] == "Открытие вклада":
                print(
                    f"""
            {time_correct(i['date'])} {i['description']}
            {mask_card_and_check(i['to'])}
            Сумма: {i["amount"]}{i['currency_code']}"""
                )
            else:
                print(
                    f"""
            {time_correct(i['date'])} {i['description']}
            {mask_card_and_check(i["from"])} -> {mask_card_and_check(i["to"])}
            Сумма: {i["amount"]}{i['currency_code']}"""
                )


def main() -> Any:
    """Главнная функция"""
    data, num = choose_format_read()
    if not data:
        print("Неверный выбор. Завершение программы.")
        return
    data_filtr = filter_status(data)

    data_filtr_2 = filter_up_down(data_filtr, num)

    filter_code = filter_rub(data_filtr_2, num)

    filter_word = filter_to_world(filter_code)
    end_answer(filter_word, num)


main()
