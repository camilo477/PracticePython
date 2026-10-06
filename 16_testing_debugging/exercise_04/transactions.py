import json
from dataclasses import asdict, dataclass


@dataclass
class Transaction:
    amount: float
    transaction_type: str


def save_transactions(transactions, path) -> None:
    data = [asdict(transaction) for transaction in transactions]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)