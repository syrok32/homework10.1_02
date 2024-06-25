import logging
from logging import Logger


def setup_logging() -> Logger:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("example.log", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
