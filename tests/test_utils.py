import json
import os.path
from typing import Any
from unittest.mock import patch

from src.utils import conversion, loads_json

dict_cur = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


@patch("requests.get")
def test_conversion(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "timestamp": 1718958604,
        "base": "USD",
        "date": "2024-06-21",
        "rates": {"EUR": 0.935925, "USD": 1, "RUB": 89.12038},
    }
    assert (
        conversion(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        == 731280.4203601001
    )


def test_loads_json() -> None:
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(dict_cur)
        assert loads_json(os.path.join("..", "data", "operations.json")) == dict_cur
        mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf-8")
