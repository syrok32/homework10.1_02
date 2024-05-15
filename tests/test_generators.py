from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(list_info_card: list) -> None:
    generator = filter_by_currency(list_info_card, filter_currency="USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_transaction_descriptions(list_info_card: list) -> None:
    generator = transaction_descriptions(list_info_card)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"


def test_card_number_generator() -> None:
    generator = card_number_generator(a=1, b=5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
