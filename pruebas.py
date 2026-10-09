

class Account:
    def __init__ (self, name, balance, transactions):
        self.name = name
        self.balance = balance
        self.transactions = transactions

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type