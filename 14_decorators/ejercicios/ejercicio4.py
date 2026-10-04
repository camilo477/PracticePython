# Exercise 4 — Validación parametrizable
# Cuando los tres anteriores estén claros, hacemos uno más interesante:
# @validate_amount(minimum=100)def deposit(...):


# y:
# @validate_amount(maximum=600)def withdraw(...):


# El mismo decorator debe poder recibir:
# minimum
# maximum

# opcionales y validar antes de ejecutar la función original.

from functools import wraps


def validate_amount(minimum=None, maximum=None):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if "amount" in kwargs:
                amount = kwargs["amount"]
            else:
                amount = args[1]
            if minimum is not None and amount < minimum:
                raise ValueError(f"amount no puede ser menor a {minimum}")
            if maximum is not None and amount > maximum:
                raise ValueError(f"amount no puede ser mayor a {maximum}")
            return function(*args, **kwargs)
        return wrapper
    return decorator


balance = 100    

@validate_amount(minimum=100)
def deposit(balance, amount):
    balance += amount
    return balance

@validate_amount(maximum=600)
def withdraw(balance, amount):
    balance -= amount
    return balance
try:
    print(deposit(balance, 1000))
except ValueError as e:
    print(e)

try:
    print(withdraw(balance, 601))
except ValueError as e:
    print(e)