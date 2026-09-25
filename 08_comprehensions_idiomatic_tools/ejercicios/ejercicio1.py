# Tienes:
# transactions = [500, -120, 300, -80, 1000]


# Crea usando comprehensions:
# 1. incomes con solo los positivos.
# 2. expenses con solo los negativos pero convertidos a positivos.
# Resultado esperado conceptualmente:
# incomes# [500, 300, 1000]expenses# [120, 80]

transactions = [500, -120, 300, -80, 1000]

incomes = [
    transaction
    for transaction in transactions if transaction >= 0
    
]

print(incomes)

expenses = [
    transaction * -1
    for transaction in transactions if transaction < 0
]

print(expenses)