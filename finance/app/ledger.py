from .transaction import Transaction

class Ledger:
    def __init__(self):
        self.transactions: list[Transaction] = []
    def __iter__(self):
            return iter(self.transactions)
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
    def income_amounts(self):

        return [
            transaction.amount
            for transaction in self.transactions if transaction.transaction_type == "income"
        ]
    def has_expense_over(self, minimum):
        return any(
            transaction.transaction_type == "expense"
            and transaction.amount > minimum
            for transaction in self.transactions
        )
    def sorted_transactions(self):
        return sorted(
            self.transactions,
            key=lambda transaction: transaction.amount,
            reverse=True
        )
    def expenses_over(self, minimum):
        for transaction in self.transactions:
            if transaction.transaction_type == "expense" and transaction.amount > minimum:
                yield transaction

ledger=Ledger()
ledger.add_transaction(Transaction(200, "income"))
ledger.add_transaction(Transaction(400, "income"))
ledger.add_transaction(Transaction(50, "expense"))
ledger.add_transaction(Transaction(100, "income"))
print(ledger.income_amounts())
print(ledger.has_expense_over(60))
print(ledger.sorted_transactions())

for transaction in ledger.expenses_over(40):
    print(transaction)