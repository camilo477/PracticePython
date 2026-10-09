from app import Ledger, Transaction
import pytest 

def test_empty_ledger():
    ledger = Ledger()
    assert ledger.transactions == []
    assert ledger.get_balance() == 0

def test_add_income():
    ledger = Ledger()
    transaction = Transaction(200, "income")

    ledger.add_transaction(transaction)
    assert len(ledger.transactions) == 1
    assert ledger.transactions[0] == transaction
    assert ledger.get_balance() == 200

def test_add_valid_expense():
    ledger = Ledger()
    transaction = Transaction(200, "income")
    ledger.add_transaction(transaction)

    transaction_expense = Transaction(100,"expense")
    ledger.add_transaction(transaction_expense)

    assert ledger.transactions[1] == transaction_expense
    assert ledger.get_balance() == 100


def test_get_total_income():
    ledger = Ledger()
    transactions = [
        200,100,86,60
    ]
    for transaction in transactions:
        new_transaction = Transaction(transaction, "income")
        ledger.add_transaction(new_transaction)
    ledger.add_transaction(Transaction(20, "expense"))
    assert ledger.get_total_income() ==  446


def test_get_total_expense():
    ledger = Ledger()
    transactions = [
        200,100,86,60
    ]
    ledger.add_transaction(Transaction(1000, "income"))
    for transaction in transactions:
        new_transaction = Transaction(transaction, "expense")
        ledger.add_transaction(new_transaction)
    
    assert ledger.get_total_expenses() ==  446


def test_get_balance():
    ledger = Ledger()
    transacions_incomes = [
        100,200,100,50
    ]
    transacions_expenses = [
        10,20,10,30
    ]
    for income_amount, expense_amount in zip(
        transacions_incomes,
        transacions_expenses
    ):
        income_transaction = Transaction(income_amount, "income")
        expense_transaction = Transaction(expense_amount, "expense")
        ledger.add_transaction(income_transaction)
        ledger.add_transaction(expense_transaction)

    assert ledger.get_balance() == 380

def test_expense_equal_to_balance_is_allowed():
    ledger = Ledger()
    ledger.add_transaction(Transaction(500, "income"))
    ledger.add_transaction(Transaction(500, "expense"))
    assert ledger.get_balance() == 0

def test_expense_greater_than_balance_raises_value_error():
    ledger = Ledger()
    ledger.add_transaction(Transaction(500, "income"))
    with pytest.raises(ValueError):
        ledger.add_transaction(Transaction(501, "expense"))

def test_rejected_expense_does_not_modify_ledger():
    ledger = Ledger()
    transaction = Transaction(500, "income")
    ledger.add_transaction(transaction)
    with pytest.raises(ValueError):
        ledger.add_transaction(Transaction(501, "expense"))
    assert ledger.get_balance() == 500
    assert ledger.transactions == [transaction]
