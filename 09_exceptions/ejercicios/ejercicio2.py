# Ejercicio 2 — raise y validaciones
# Crea:
# withdraw(balance, amount)


# Requisitos:
# - si amount no es int ni float → TypeError;
# - si amount <= 0 → ValueError;
# - si amount > balance → ValueError;
# - si es válido → devuelve el nuevo balance;
# - no modifica ninguna variable global.
# Luego prueba al menos estos casos:
# withdraw(1000, 200)withdraw(1000, -50)withdraw(1000, "200")withdraw(1000, 1500)


# Quiero que tú decidas qué mensajes poner en cada excepción.

def withdraw(balance, amount):

    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be int or float")
    if amount <= 0:
        raise ValueError("amount must be greater than 0")
    if amount > balance:
        raise ValueError("amount cannot be greater than balance")
    
    balance = balance - amount
    return balance

tests = [
    (1000, 200),
    (1000, -50),
    (1000, "200"),
    (1000, 1500),
]
for balance, amount in tests:
    try:
        result = withdraw(balance, amount)
        print(result)

    except TypeError as error:
        print(error)

    except ValueError as error:
        print(error)