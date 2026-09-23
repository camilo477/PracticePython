# Tienes:

# transactions = [
#     ("income", 2500),
#     ("expense", 120),
#     ("expense", 80),
#     ("income", 500),
# ]

# y:

# january_categories = {"food", "rent", "transport"}

# february_categories = {"food", "health", "transport"}

# Tu programa debe:

# tomar la primera tuple y desempaquetarla en transaction_type y amount;
# imprimir ambos valores;
# recorrer transactions desempaquetando directamente cada tuple;
# construir un set llamado transaction_types con todos los tipos encontrados, sin duplicados;
# imprimir la intersección de las categorías de enero y febrero;
# imprimir la unión;
# imprimir las categorías que están en enero pero no en febrero;
# imprimir la diferencia simétrica.

transactions = [
    ("income", 2500),
    ("expense", 120),
    ("expense", 80),
    ("income", 500),
]

january_categories = {"food", "rent", "transport"}

february_categories = {"food", "health", "transport"}

transaction_type , amount = transactions[0]

print(transaction_type, amount)

transaction_types = set()

for transaction in transactions:
    transaction_type , amount = transaction
    print(transaction_type, amount)
    transaction_types.add(transaction_type)

print(transaction_types)

print("interseccion: " , january_categories & february_categories)
print("union: " , january_categories | february_categories)
print("en enero pero no en febrero: ", january_categories - february_categories)
print("diferencia simetrica: ", january_categories ^ february_categories)


