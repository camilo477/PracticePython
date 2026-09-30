from .validators import validate_amount


def calculate_deposit(balance, amount):
    validate_amount(amount)

    return balance + amount