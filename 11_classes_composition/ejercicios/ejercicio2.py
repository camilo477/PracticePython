# Exercise 2 — Composición con Transaction
# Ahora crea una clase:
# Transaction

# con:
# amount
# transaction_type

# Reglas:
# - amount debe ser mayor que 0;
# - transaction_type solo puede ser "income" o "expense".
# Luego modifica Account para que cada instancia tenga:
# self.transactions = []

# Cuando hagas:
# account.deposit(500)

# debe ocurrir:
# validar monto
# ↓
# aumentar balance
# ↓
# crear Transaction(500, "income")
# ↓
# agregarla a self.transactions

# Y con:
# account.withdraw(200)

# debe crear:
# Transaction(200, "expense")

# Finalmente, añade a Transaction un:
# __repr__()

# para que al hacer:
# print(account.transactions)

# veas algo útil, por ejemplo:
# [Transaction(amount=500, transaction_type='income'),
#  Transaction(amount=200, transaction_type='expense')]

class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("el balance inicial no puede ser negativo")
        self.name =name
        self.balance = balance
        self.transactions = []
    def deposit(self, amount):
        self.validation(amount)
        transaction = Transaction(amount, "income")
        self.transactions.append(transaction)
        self.balance += amount
        
    def withdraw(self, amount):
        self.validation(amount)
        if amount > self.balance:
              raise ValueError("la cantidad a retirar no puede ser mayor al balance")
        transaction = Transaction(amount, "expense")
        self.transactions.append(transaction)
        self.balance -= amount
        
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

account1= Account("primero", 2000)
account1.withdraw(200)
account1.deposit(2300)
print(account1.transactions)
