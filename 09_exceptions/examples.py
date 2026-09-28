# Ejemplo completo 1 — parsear una transacción

def parse_amount(value):
    try:
        amount = float(value)
    except ValueError:
        print("Invalid amount")
        return None

    return amount

parse_amount("120.50")

# float()
# ↓
# funciona
# ↓
# return 120.5

parse_amount("hello")

# float()
# ↓
# ValueError
# ↓
# except
# ↓
# return None

# Ejemplo completo 2 — validación con raise

def withdraw(balance, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be numeric")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount

# validar tipo
# ↓
# validar valor
# ↓
# validar regla de negocio
# ↓
# realizar operación

try:
    balance = withdraw(1000, 1200)
except (TypeError, ValueError) as error:
    print(error)