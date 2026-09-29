from .validators import validate_amount


def deposit(balance, amount):
    validate_amount(amount)
    result = balance + amount
    return result

def withdraw(balance, amount):
    validate_amount(amount)
    if amount > balance:
        raise ValueError("amount no puede ser mayor que balance")
    result = balance - amount
    return result

if __name__ == "__main__":
    print(deposit(1000, 500))
    print(withdraw(1000, 200))