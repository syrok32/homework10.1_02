from src.logger_logging import setup_logging

logger = setup_logging()


def summ_two_num(num1: int, num2: int) -> int:
    """возврощает сумму двух чисел"""
    logger.info("успешно")
    return num1 + num2
