# Ejercicio — Dictionaries

# Tienes estas transacciones:

# transactions = [
#     {"type": "income", "category": "salary", "amount": 2500},
#     {"type": "expense", "category": "food", "amount": 120},
#     {"type": "expense", "category": "transport", "amount": 80},
#     {"type": "expense", "category": "food", "amount": 50},
# ]

# Haz un programa que:

# imprima el amount de la primera transacción;
# cambie el amount de transport de 80 a 90;
# agregue "description": "Monthly salary" a la primera transacción;
# compruebe si "description" existe en la segunda transacción;
# use .get() para intentar obtener "description" de la segunda transacción con valor por defecto "No description";
# construya un diccionario totals_by_category que termine así:
# {
#     "salary": 2500,
#     "food": 170,
#     "transport": 90
# }
# recorra totals_by_category con .items() e imprima:
# salary -> 2500
# food -> 170
# transport -> 90


transactions = [
    {"type": "income", "category": "salary", "amount": 2500},
    {"type": "expense", "category": "food", "amount": 120},
    {"type": "expense", "category": "transport", "amount": 80},
    {"type": "expense", "category": "food", "amount": 50},
]


print(transactions[0]["amount"])

transactions[2]["amount"] = 90

transactions[0]["description"] = "Monthly salary"

print("description" in transactions[1])

print(transactions[1].get("description", "No description"))


totals_by_category = {}

for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]
    totals_by_category[category] = totals_by_category.get(category, 0) + amount

for i in totals_by_category.items():

    print(f"{i[0]} -> {i[1]}")

