# Exercise 3 — JSON + dataclass
# Crea:
# @dataclassclass Transaction:
#     amount: float
#     transaction_type: str
#     description: str | None = None


# Crea:
# load_transactions(path)
#  -> list[Transaction]save_transactions(transactions, path) -> None


# load_transactions():
# archivo JSON
# ↓
# json.load()
# ↓
# list[dict]
# ↓
# Transaction(**item)
# ↓
# list[Transaction]

# Debe manejar:
# FileNotFoundError → []
# JSONDecodeError → []

# save_transactions():
# list[Transaction]
# ↓
# asdict()
# ↓
# list[dict]
# ↓
# json.dump()

# Usa:
# indent=4ensure_ascii=Falseencoding="utf-8"
import json
from dataclasses import dataclass, asdict



@dataclass
class Transaction:
    amount: float
    transaction_type: str
    description: str | None = None

def load_transactions(path) -> list[Transaction]:
    result = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                transaction = Transaction(**item)
                result.append(transaction)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return result

def save_transactions(transactions, path) -> None:
    datos = []
    with open(
        path, "w",
        encoding="utf-8") as file:
        for transaction in transactions:
            datos.append(asdict(transaction))
        json.dump(
            datos,
            file,
            indent=4,
            ensure_ascii=False
        )

transactions = [
    Transaction(500, "income", "Salary"),
    Transaction(100, "expense", "Food"),
]

save_transactions(transactions, "ejemplo.json")

loaded_transactions = load_transactions("ejemplo.json")

print(loaded_transactions)