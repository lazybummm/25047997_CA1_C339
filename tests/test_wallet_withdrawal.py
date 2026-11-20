
from wallet_withdrawal import withdraw


def test_W01_normal_withdrawal():
    assert withdraw(1000, 300) == 700


def test_W02_exact_balance():
    assert withdraw(1000, 1000) == 0


import pytest


def test_W03_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(500, 600)


def test_W04_zero_amount():
    with pytest.raises(ValueError):
        withdraw(1000, 0)


def test_W05_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)


def test_W06_negative_balance():
    with pytest.raises(ValueError):
        withdraw(-100, 50)


def test_W07_zero_balance():
    with pytest.raises(ValueError):
        withdraw(0, 100)


def test_W08_minimum_withdrawal():
    assert withdraw(1, 1) == 0


def test_W09_string_balance():
    with pytest.raises(TypeError):
        withdraw("1000", 100)


def test_W10_float_amount():
    with pytest.raises(TypeError):
        withdraw(1000, 10.5)
