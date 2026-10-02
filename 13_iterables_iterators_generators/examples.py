def positive_amounts(transactions):
    for amount in transactions:
        if amount > 0:
            yield amount


transactions = [500, -100, 300, -50]

generator = positive_amounts(transactions)

print(next(generator))
# 500

print(next(generator))
# 300

for amount in positive_amounts(transactions):
    print(amount)