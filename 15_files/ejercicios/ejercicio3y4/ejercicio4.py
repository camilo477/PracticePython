# Exercise 4 — Integrador
# Crea:
# add_transaction(transaction)


# Debe:
# 1. cargar las transacciones actuales desde JSON;
# 2. agregar una instancia Transaction;
# 3. guardar nuevamente todas.
# Después:
# add_transaction(    Transaction(        amount=2500,        transaction_type="income",        description="Salary"    ))


# y:
# add_transaction(    Transaction(        amount=120,        transaction_type="expense",        description="Internet"    ))


# Después carga el archivo y recorre los objetos Transaction.
# Este ejercicio reproduce exactamente el flujo real:
# persistencia
# → cargar
# → objetos Python
# → modificar estado
# → serializar
# → guardar


import json
from dataclasses import asdict, dataclass


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

def add_transaction(transaction, path) -> None:
    transactions = load_transactions(path)

    transactions.append(transaction)

    save_transactions(transactions, path)

add_transaction(
    Transaction(
        amount=120,
        transaction_type="expense",
        description="Internet"
    ),
    "ejemplo.json"
)

add_transaction(
    Transaction(
        amount=2500,
        transaction_type="income",
        description="Salary"
    ),
    "ejemplo.json"
)