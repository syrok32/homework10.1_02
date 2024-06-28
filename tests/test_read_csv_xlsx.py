import os
from typing import Any
from unittest.mock import patch

from pandas import DataFrame

from src.read_csv_xlsx import reader_csv_file, reader_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_read: Any) -> None:
    mock_read.return_value = DataFrame({"id": ["aleks", "23"]})
    assert reader_csv_file(os.path.join("..", "data", "transactions.csv")) == {"id": {0: "aleks", 1: "23"}}


@patch("pandas.read_excel")
def test_reader_xlsx_file(mock_read: Any) -> None:
    mock_read.return_value = DataFrame({"id": ["aleks", "23"]})
    assert reader_xlsx_file(os.path.join("..", "data", "transactions_excel.xlsx")) == {"id": {0: "aleks", 1: "23"}}
