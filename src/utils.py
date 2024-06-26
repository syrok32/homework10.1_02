import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.logger_logging import setup_logging

logger = setup_logging()
load_dotenv()
TOKEN = os.getenv("token")

headers = {"apikey": f"{TOKEN}"}


def loads_json(file: str) -> Any:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                logger.info("Ошибка: ошибка преоброзования")
                print("False")
                return list()
    except FileNotFoundError:
        logger.info("Ошибка: файл не найден")
        print("erorr")
        return list()
    logger.info("Успешно")
    return data


def conversion(dict_transaction: dict) -> Any:
    """ринимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    currency = dict_transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(dict_transaction["operationAmount"]["amount"])
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=EUR%2C%20USD%2C%20RUB&base={currency}"
    response = requests.request("GET", url, headers=headers)
    api_convert = response.json()
    logger.info("Успешно")

    return api_convert["rates"]["RUB"] * float(dict_transaction["operationAmount"]["amount"])
