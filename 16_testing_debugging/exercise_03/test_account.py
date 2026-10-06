import pytest

from account import Account


def test_deposit_increases_balance():
    account = Account(1000)

    account.deposit(500)

    assert account.balance == 1500


def test_deposit_rejects_zero():
    account = Account(1000)

    with pytest.raises(ValueError):
        account.deposit(0)


def test_withdraw_reduces_balance():
    account = Account(1000)

    account.withdraw(200)

    assert account.balance == 800


def test_withdraw_all_balance_is_allowed():
    account = Account(1000)

    account.withdraw(1000)

    assert account.balance == 0


def test_withdraw_more_leaves_it_intact():
    account = Account(1000)

    with pytest.raises(ValueError):
        account.withdraw(1200)

    assert account.balance == 1000