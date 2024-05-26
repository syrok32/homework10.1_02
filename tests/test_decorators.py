from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log()
    def test_my_function_ok(x: int, y: int) -> int:
        """выводит сумму x и y"""
        return x + y

    test_my_function_ok(1, 2)
    captured = capsys.readouterr()

    assert captured.out in "test_my_function_ok ок\n"


def test_log_neget(capsys: Any) -> None:
    @log()
    def test_my_function_ok(x: int, y: int) -> int:
        """выводит сумму x и y"""
        return x + y

    test_my_function_ok(1, "w")
    captured = capsys.readouterr()

    assert captured.out == "test_my_function_ok error: <class 'TypeError'>.Inputs: (1, 'w'), {}\n"


def test_log_accepted_file() -> None:

    @log("..\\mylog.txt")
    def test_my_function_ok(x: int, y: int) -> int:
        """выводит сумму x и y"""
        return x + y

    test_my_function_ok(1, 2)
    with open("..\\mylog.txt", "r", encoding="utf-8") as file:
        content = file.read()
        assert "test_my_function_ok ок" in content


def test_log_feling_file() -> None:
    @log("..\\mylog.txt")
    def test_my_function_ok(x: int, y: int) -> int:
        """выводит сумму x и y"""
        return x + y

    test_my_function_ok(1, "D")
    with open("..\\mylog.txt", "r", encoding="utf-8") as file:
        content = file.read()
        assert "test_my_function_ok error: <class 'TypeError'>.Inputs: (1, 'D'), {}" in content
