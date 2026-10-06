import pytest
from banking import withdraw

def test_withdraw_reduces_balance():
    result = withdraw(1000, 200)

    assert result == 800


def test_withdraw_all_balance():
    result = withdraw(1000, 1000)

    assert result == 0


def test_withdraw_rejects_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)


def test_withdraw_rejects_insufficient_funds():
    with pytest.raises(ValueError):
        withdraw(1000, 1500)


def test_withdraw_rejects_zero():
    with pytest.raises(ValueError):
        withdraw(1000, 0)