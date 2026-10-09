from .transaction import Transaction
class Ledger:
    def __init__(self):
        self.transactions: list[Transaction] = []
    def add_transaction(self, transaction: Transaction) -> None:
        if transaction.transaction_type == "income":
            self.transactions.append(transaction)
        else:
            if transaction.amount > self.get_balance():
                raise ValueError("expense can't be more than balance")
            self.transactions.append(transaction)
    def get_total_income(self):
        result = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                result += transaction.amount
        return result
    def get_total_expenses(self):
        result = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                result += transaction.amount
        return result
    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

ledger1 = Ledger()
ledger1.add_transaction(Transaction(500, "income"))
ledger1.add_transaction(Transaction(500, "expense"))

print(ledger1.get_total_expenses())
print(ledger1.get_balance())
print(ledger1.transactions)
