class Transaction:
    ALLOWED_TYPES = {"income", "expense"}

    def __init__(self, amount, transaction_type):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if transaction_type not in self.ALLOWED_TYPES:
            raise ValueError("Invalid transaction type")

        self.amount = amount
        self.transaction_type = transaction_type

    def __repr__(self):
        return (
            f"Transaction("
            f"amount={self.amount}, "
            f"transaction_type={self.transaction_type!r}"
            f")"
        )


class Account:
    def __init__(self, name, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.name = name
        self._balance = balance
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        transaction = Transaction(amount, "income")

        self._balance += amount
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")

        transaction = Transaction(amount, "expense")

        self._balance -= amount
        self.transactions.append(transaction)

# Account
# ├── estado propio
# ├── estado protegido
# ├── métodos
# └── contiene Transaction

# Transaction
# ├── valida su propio estado
# └── representa una operación

