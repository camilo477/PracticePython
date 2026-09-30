Error típico: olvidar self

class Account:
    def deposit(amount):
        ...

otro error:

class Account:
    def __init__(self, balance):
        balance = balance

falta el self, seria self.balance = balance