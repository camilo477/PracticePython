# Tienes la misma lista:
# transactions = [500, -120, 300, -80, 1000]
# Quiero que la recorras usando:
# enumerate(transactions)
# y que imprimas:
# 0 -> 500
# 1 -> -120
# 2 -> 300
# 3 -> -80
# 4 -> 1000

transactions = [500, -120, 300, -80, 1000]

for index, transaction in enumerate(transactions):
    print(f"{index} -> {transaction}")