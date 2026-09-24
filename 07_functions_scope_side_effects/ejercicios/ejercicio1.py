# Haz una función:
# calculate_summary(transactions)


# Recibirá:
# transactions = [500, -120, 300, -80, 1000]


# Debe calcular y devolver tres valores:
# total_income
# total_expenses
# balance

# Reglas:
# - positivos → income;
# - negativos → expenses;
# - total_expenses quiero que sea positivo, por ejemplo 200, no -200;
# - balance = income - expenses.
# Ejemplo esperado:
# income, expenses, balance = calculate_summary(transactions)


# No uses:
# sum()

transactions = [500, -120, 300, -80, 1000]

def calculate_summary(transactions):
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction >= 0:
            total_income += transaction
        elif transaction < 0:
            total_expenses -= transaction
    balance = total_income - total_expenses
    return total_income, total_expenses, balance

print (calculate_summary(transactions))