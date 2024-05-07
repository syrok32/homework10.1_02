import pytest
from src.widget import mask_card_and_check, time_correct


@pytest.mark.parametrize(
    "initial, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_card_and_check(initial, expected_result):
    assert mask_card_and_check(initial) == expected_result


def test_time_correct():
    assert time_correct("2018-07-11T02:26:18.671407") == "11.07.2018"
