
import pytest
from wallet_affordability import can_afford


def test_A01_balance_greater_than_price():
    assert can_afford(1000, 500) is True


def test_A02_balance_equal_to_price():
    assert can_afford(1000, 1000) is True


def test_A03_balance_less_than_price():
    assert can_afford(500, 1000) is False


def test_A04_zero_price():
    assert can_afford(1000, 0) is True


def test_A05_zero_balance_and_price():
    assert can_afford(0, 0) is True


def test_A06_zero_balance_positive_price():
    assert can_afford(0, 100) is False


def test_A07_negative_balance():
    with pytest.raises(ValueError):
        can_afford(-100, 50)


def test_A08_negative_price():
    with pytest.raises(ValueError):
        can_afford(1000, -50)


def test_A09_string_balance():
    with pytest.raises(TypeError):
        can_afford("1000", 500)


def test_A10_float_price():
    with pytest.raises(TypeError):
        can_afford(1000, 50.5)
