"""
Tienes:

transactions = [500, -120, 300, -80, 1000]

Tu programa debe:

imprimir la primera y la última transacción;
agregar 250 al final;
agregar [-50, -30] como dos transacciones independientes, no como una lista anidada;
cambiar -120 por -150 usando un índice;
eliminar -80 por valor;
eliminar la última transacción y guardar el valor eliminado en removed_transaction;
imprimir las primeras tres transacciones usando slicing;
crear una nueva lista ordenada sin modificar el orden de transactions;
imprimir ambas listas para demostrarlo;
imprimir cuántas transacciones quedan.
"""

transactions = [500, -120, 300, -80, 1000]

print("primera transaccion: ",transactions[0])
print("ultima transaccion: ",transactions[-1])

transactions.append(250)

transactions.extend([-50, -30])

transactions[1] = -150

transactions.remove(-80)

removed_transaction = transactions.pop()

print(transactions[0:3])

sorted_transaction = sorted(transactions)
print("lista ordenada",sorted_transaction)
print("lista original", transactions)

print(len(transactions))
