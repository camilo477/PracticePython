def calculate_income(transactions):
    result = 0
    for transaction in transactions:
        if transaction > 0:
            result += transaction
    return result

def calculate_expenses(transactions):
    result = 0
    for transaction in transactions:
        if transaction < 0:
            result += transaction
    return result * -1

def calculate_balance(transactions):
    income = calculate_income(transactions)
    expenses = calculate_expenses(transactions)
    result = income - expenses
    return result

if __name__ == "__main__":
    test_transactions = [1000, -200, 500]

    print(calculate_income(test_transactions))

    print(calculate_expenses(test_transactions))

    print(calculate_balance(test_transactions))

