# Exercise 3 — Decorator en métodos
# Crea:
# class Account:


# con:
# deposit(amount)withdraw(amount)


# y un decorator:
# @log_method


# que imprima el nombre del método antes de ejecutarlo:
# Calling deposit

# o:
# Calling withdraw

# Usa:
# function.__name__


# El decorator debe funcionar para ambos métodos sin saber
# explícitamente su firma.

from functools import wraps


def log_method(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling{function.__name__}")
        return function(*args, **kwargs)
    return wrapper

class Account:
    def __init__(self, balance):
        self.balance = balance

    @log_method
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    @log_method
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

account1 = Account(1000)

print(account1.deposit(100))
