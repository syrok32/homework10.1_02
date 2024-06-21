from functools import wraps
from typing import Any, Callable


def log(filename: Any | None = None) -> Any:
    """Возвращает логирвание в файл или консоль"""

    def decorator(func: Callable[[Any], str | None]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            try:
                if func(*args, **kwargs):
                    if filename:
                        with open(filename, "w", encoding="utf-8") as file:
                            file.write(f"{func.__name__} ок")
                    else:
                        print(f"{func.__name__} ок")

            except Exception as error:

                if filename:
                    with open(filename, "w", encoding="utf-8") as file:

                        file.write(f"{func.__name__} error: {type(error)}.Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {type(error)}.Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    """выводит сумму x и y"""
    return x + y


my_function(1, 2)
