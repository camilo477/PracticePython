import pytest, json
from transactions import Transaction, save_transactions

transactions = [
    Transaction(500, "income"),
    Transaction(100, "expense")
]

expected = [
    {
        "amount": 500,
        "transaction_type": "income"
    },
    {
        "amount": 100,
        "transaction_type": "expense"
    }
]

def test_save_json(tmp_path):
    path = tmp_path / "transactions.json"

    assert not path.exists()

    save_transactions(transactions, path)

    assert path.exists()

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == expected



    