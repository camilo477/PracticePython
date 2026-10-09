from app import Transaction
import pytest 


def test_valid_income():
    transaction=Transaction(500, "income")

    assert transaction == Transaction(amount=500, transaction_type='income', description=None)

def test_valid_expense_description():
    transaction=Transaction(120, "expense", "Internet")

    assert transaction == Transaction(amount=120, transaction_type='expense', description="Internet")

@pytest.mark.parametrize(
        "amount",
        [
            0,-120,
        ]
)

def test_amount_equal_0_and_negative(amount):

    with pytest.raises(ValueError):
        Transaction(amount, "income")

def test_amount_invalid_type():
    
    with pytest.raises(TypeError):
        Transaction("120", "income")

def test_transaction_type_invalid_value():
    
    with pytest.raises(ValueError):
        Transaction(120, "example")

def test_transaction_without_description():

    transaction=Transaction(amount=120, transaction_type="expense")
    
    assert transaction == Transaction(amount=120, transaction_type='expense', description=None)
    