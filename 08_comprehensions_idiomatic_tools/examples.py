transactions = [
    {"type": "income", "category": "salary", "amount": 2500},
    {"type": "expense", "category": "food", "amount": 120},
    {"type": "expense", "category": "transport", "amount": 80},
    {"type": "expense", "category": "food", "amount": 50},
]

#Podemos obtener únicamente los gastos:

expenses = [
    transaction
    for transaction in transactions
    if transaction["type"] == "expense"
]

#Las categorías únicas:

categories = {
    transaction["category"]
    for transaction in transactions
}

#Comprobar si hay algún gasto mayor a 100:

has_large_expense = any(
    transaction["type"] == "expense"
    and transaction["amount"] > 100
    for transaction in transactions
)

#Comprobar que todos los montos sean positivos:

all_valid = all(
    transaction["amount"] > 0
    for transaction in transactions
)

#Y ordenar por amount:

ordered_transactions = sorted(
    transactions,
    key=lambda transaction: transaction["amount"]
)

