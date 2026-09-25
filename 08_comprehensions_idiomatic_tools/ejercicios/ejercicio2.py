# Ejercicio 2 — any, all, sorted, min, max
# Tienes:
# transactions = [
#     {"type": "income", "amount": 2500},
#     {"type": "expense", "amount": 120},
#     {"type": "expense", "amount": 80},
#     {"type": "income", "amount": 500},
# ]


# Haz lo siguiente:
# 1. Usa any() para comprobar si existe al menos una transacción "expense".
# 2. Usa all() para comprobar que todos los amount sean mayores que 0.
# 3. Crea ordered_transactions ordenando de menor a mayor por "amount"
# con sorted() y lambda.
# 4. Crea ordered_descending de mayor a menor.
# 5. Construye una colección con solo los amounts y usa min() y max()
# para obtener el menor y el mayor.
# No uses loops manuales para resolver esos cinco puntos.

transactions = [
    {"type": "income", "amount": 2500},
    {"type": "expense", "amount": 120},
    {"type": "expense", "amount": 80},
    {"type": "income", "amount": 500},
]

expense = any(
    transaction["type"] == "expense"
    for transaction in transactions
)
print(expense)

bigger_than_0 = all(
    transaction["amount"] > 0
    for transaction in transactions
)

print(bigger_than_0)

ordered_transactions = sorted(
    transactions,
    key = lambda transaction: transaction["amount"]
)

print(ordered_transactions)

ordered_descending = sorted(
    transactions, reverse=True,
    key = lambda transaction: transaction["amount"]
)

print(ordered_descending)

amounts = [
    transaction["amount"]
    for transaction in transactions
]

min_amount = min(
    amounts
)
max_amount = max(
    amounts
)
