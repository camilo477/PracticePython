# Partimos de:
# transactions = [500, -100]


# Crea dos funciones.
# La primera:
# add_transaction_mutating(transactions, amount)
# Debe agregar amount usando append(), modificando la lista recibida.

# La segunda:
# add_transaction_pure(transactions, amount)
# debe:
# - NO modificar transactions;
# - crear una nueva lista, que sea copia de la original;
# - agregar amount a esa nueva lista;
# - devolverla.

# Después prueba algo conceptualmente así:
# transactions = [500, -100]
# # llamada función que muta...print(transactions)
# # llamada función que no muta...print(transactions)print(new_transactions)

transactions = [500, -100]

def add_transaction_mutating(transactions, amount):
    transactions.append(amount)
    return transactions

def add_transaction_pure(transactions, amount):
    transactions_copy = transactions.copy()
    transactions_copy.append(amount)
    return transactions_copy

print(add_transaction_mutating(transactions, 50))

print(add_transaction_pure(transactions, 60))

