# Exercise 2 — Generator con yield
# Crea:
# positive_transactions(transactions)


# que reciba:
# [500, -100, 300, -50, 1000]


# y usando yield produzca solamente:
# 500
# 300
# 1000

# No construyas una lista dentro del generator.
# Después recórrelo con:
# for transaction in ...

transactions = [500, -100, 300, -50, 1000]

def positive_transactions(transactions):
    for transaction in transactions:
        if transaction > 0:
            yield transaction


for generator in positive_transactions(transactions):
    print(generator)