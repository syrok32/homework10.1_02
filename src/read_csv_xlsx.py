import pandas as pd


def reader_csv_file(file_csv: str) -> dict:
    """Читает .csv файл и возврощает словарь"""

    dateframe = pd.read_csv(file_csv, delimiter=";")
    return dateframe.to_dict()


def reader_xlsx_file(file_xlsx: str) -> dict:
    """Читает .xlsx файл и возврощает словарь"""
    dateframe = pd.read_excel(file_xlsx)
    return dateframe.to_dict()
