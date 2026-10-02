# Exercise 4 — Integración con clases
# Reutiliza una versión sencilla de:
# @dataclass
# class Transaction:
#     amount: float
#     transaction_type: str


# y:
# class Account:


# Account debe tener:
# self.transactions: list[Transaction]


# Añade:
# def __iter__(self):


# para que puedas hacer:
# for transaction in account:    print(transaction)


# Después crea otro método:
# amounts_over(minimum)


# que sea generator y haga yield de los amounts superiores al mínimo.
# Por ejemplo:
# for amount in account.amounts_over(200):
#     print(amount)

from dataclasses import dataclass


@dataclass
class Transaction:
    amount: float
    transaction_type: str

class Account:
    def __init__(self, transactions: list[Transaction]):
        self.transactions = transactions 
    def __iter__(self):
        return iter(self.transactions)
    def amounts_over(self,  minimum):
        for transaction in self.transactions:
            if transaction.amount > minimum:
                yield transaction.amount

transaction1 = Transaction(100, "expense")
transaction2 = Transaction(500, "income")
transaction3 = Transaction(300, "expense")

account = Account([
    transaction1,
    transaction2,
    transaction3
])

for amount in account.amounts_over(200):
    print(amount)