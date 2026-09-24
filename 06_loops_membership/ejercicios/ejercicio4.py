# Tienes:
# transactions = [500, 300, 1000, 2000, 150]
# Quiero que hagas un for que:

# recorra las transacciones;
# encuentre la primera transacción mayor a 900;
# la imprima;
# use break para terminar el loop inmediatamente.

# El resultado debería ser:
# 1000
# y no debería llegar a imprimir 2000.

transactions = [500, 300, 1000, 2000, 150]

for transaction in transactions:
    if transaction > 900:
        print(transaction)
        break
