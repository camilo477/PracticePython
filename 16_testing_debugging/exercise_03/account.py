class Account:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount