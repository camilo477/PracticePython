# Exercise 1 — Clase básica
# En tu carpeta de ejercicios crea una clase:
# Account


# Debe tener:
# name
# balance

# y:
# deposit(amount)withdraw(amount)


# Reglas:
# - saldo inicial no puede ser negativo;
# - deposit() solo acepta montos mayores que 0;
# - withdraw() solo acepta montos mayores que 0;
# - no puedes retirar más del saldo disponible;
# - los métodos deben modificar el balance;
# - usa excepciones apropiadas.
# Prueba con dos cuentas diferentes para demostrar que sus estados son independientes.
# No uses @property todavía.

class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("el balance inicial no puede ser negativo")
        self.name =name
        self.balance = balance
    def deposit(self, amount):
        self.validation(amount)
        self.balance += amount
        
    def withdraw(self, amount):
        self.validation(amount)
        if amount > self.balance:
              raise ValueError("la cantidad a retirar no puede ser mayor al balance")
        self.balance -= amount
    
    def validation(self, amount):
         if amount <= 0:
            raise ValueError("amount debe ser mayor que 0")

account1= Account("primero", 2000)
account2= Account("segundo", 500)



try:
    account1.deposit(200)
    print(account1.balance)
except ValueError as e:
    print(f"error, {e}" )
try:
    account2.withdraw(600)
    print(account2.balance)
except ValueError as e:
    print(f"error, {e}" )


