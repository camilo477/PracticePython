def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("amount debe ser int o float")
    if amount <= 0:
        raise ValueError("amount debe ser mayor que 0")
    