def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount