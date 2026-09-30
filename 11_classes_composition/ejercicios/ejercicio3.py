# Exercise 3 — Encapsulation + @property
# Ahora toma exactamente tus clases actuales.
# En Account, cambia:
# self.balance = balance

# por un atributo interno:
# self._balance = balance

# A partir de ahí, dentro de Account, deposit() y withdraw() 
# deben trabajar con:
# self._balance

# No con self.balance.
# Después crea una property:
# @propertydef balance(self):    ...

# para que desde afuera siga funcionando:
# account = Account("Savings", 2000)print(account.balance)

# y obtengas:
# 2000

# Pero no hagas setter todavía.
# Quiero que entiendas esta separación:
# afuera de Account
# ↓
# account.balance
# ↓
# property
# ↓
# self._balance

# dentro de Account
# ↓
# self._balance

# El objetivo es empezar a tener una interfaz pública (balance) 
# separada del estado interno (_balance).

class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("el balance inicial no puede ser negativo")
        self.name =name
        self._balance = balance
        self.transactions = []
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        self.validation(amount)
        transaction = Transaction(amount, "income")
        self.transactions.append(transaction)
        self._balance += amount
        
    def withdraw(self, amount):
        self.validation(amount)
        if amount > self._balance:
              raise ValueError("la cantidad a retirar no puede ser mayor al balance")
        transaction = Transaction(amount, "expense")
        self.transactions.append(transaction)
        self._balance -= amount
        
    def validation(self, amount):
         if amount <= 0:
            raise ValueError("amount debe ser mayor que 0")

class Transaction:
    def __init__(self, amount, transaction_type):
        if amount <= 0:
            raise ValueError("amount debe ser mayor que 0")
        if transaction_type not in ["income", "expense"]:
            raise ValueError("transactionn_type debe ser income o expense")
        self.amount = amount
        self.transaction_type = transaction_type
    def __repr__(self):
        return(
            f"Transaction("
            f"amount={self.amount}, "
            f"transaction_type={self.transaction_type!r}"
            f")"
        )

account = Account("Savings", 2000)

print(account.balance)