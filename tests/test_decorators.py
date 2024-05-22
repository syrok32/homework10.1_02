from typing import Any

from src.decorators import my_function


def test_log(capsys: Any) -> None:
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ок\n"


def test_log_neget(capsys: Any) -> None:
    my_function(1, "w")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: <class 'TypeError'>.Inputs: (1, 'w'), {}\n"


def test_log_in() -> None:
    with open("..\\mylog.txt", "r", encoding="utf-8") as file:
        content = file.read()
        assert "my_function ок" == content
