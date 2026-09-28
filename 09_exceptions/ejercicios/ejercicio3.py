# Ejercicio 3 — Exceptions integradas
# Tienes:
# transactions = [    {"amount": "500"},    {"amount": "hello"},    {},    {"amount": "300"},]


# Crea una función:
# calculate_total(transactions)


# Debe:
# - recorrer todas las transacciones;
# - obtener "amount" de cada diccionario;
# - convertirlo a float;
# - si falta "amount", capturar KeyError;
# - si el valor no puede convertirse, capturar ValueError;
# - imprimir un mensaje diferente para cada error;
# - continuar procesando las siguientes transacciones;
# - acumular solamente las válidas;
# - devolver el total.
# El resultado final debería ser:
# 800.0

# Porque solo son válidos:
# 500 + 300

# La estructura mental que quiero que uses es:
# for cada transaction
#     ↓
#     try
#         obtener amount
#         convertir a float
#         acumular
#     ↓
#     except KeyError
#         manejar esa transacción
#     ↓
#     except ValueError
#         manejar esa transacción
#     ↓
# siguiente iteración

# Importante: el try/except debe estar dentro del for, para que una transacción mala no detenga todas las demás.

transactions = [
    {"amount": "500"},
    {"amount": "hello"},
    {},
    {"amount": "300"},
]

def calculate_total(transactions):
    result = 0
    for transaction in transactions:
        try:
            result += float(transaction["amount"]) 
        except KeyError:
            print("falta amount")
        except ValueError:
            print("el valor no puede convertirse")
    return result
print(calculate_total(transactions))