from src.masks import mask_card, mask_check


def test_mask_card(card: str) -> None:
    assert mask_card(card) == "7000 79** **** 6361"


def test_mask_check(check: str) -> None:
    assert mask_check(check) == "**4305"
