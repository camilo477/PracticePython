class Account:

    def __init__(self, name):
        self.transactions = []
        self.name = name
        


account1 = Account("Savings")
account2 = Account("Checking")

account1.transactions.append(500)

print(account1.transactions)
print(account2.transactions)

print(account1.transactions is account2.transactions)