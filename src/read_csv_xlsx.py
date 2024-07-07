from typing import Any

import pandas as pd


def reader_csv_file(file_csv: str) -> Any:
    """Читает .csv файл и возврощает словарь"""

    dateframe = pd.read_csv(file_csv, delimiter=";")
    return dateframe.to_dict("records")


def reader_xlsx_file(file_xlsx: str) -> list[dict]:
    """Читает .xlsx файл и возврощает словарь"""
    dateframe = pd.read_excel(file_xlsx)
    return dateframe.to_dict("records")
