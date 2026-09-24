# Tienes:

# transactions = [500, -120, 300, -80, 1000]

# Escribe un programa que:

# recorra las transacciones;
# si una transacción es negativa, use continue;
# imprima solamente las positivas;
# vaya acumulando las positivas en una variable total_income;
# al final imprima total_income.

transactions = [500, -120, 300, -80, 1000]

total_income = 0

for transaction in transactions:
    if transaction < 0:
        continue
    print (transaction)
    total_income += transaction
print(total_income)
