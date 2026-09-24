# 1. for

transactions = [500, -100, 300]

for transaction in transactions:
    print(transaction)

# transaction = 500
# ↓
# ejecuta el bloque

# transaction = -100
# ↓
# ejecuta el bloque

# transaction = 300
# ↓
# ejecuta el bloque

# 2. range

for i in range(5):
    print(i)

# da 
# 0
# 1
# 2
# 3
# 4

#enumerate()

transactions = [500, -100, 300]

for index, transaction in enumerate(transactions):
    print(index, transaction)

"""
da
0 500
1 -100
2 300
"""

#while

balance = 500

while balance > 0:
    print(balance)
    balance -= 100

"""
da
500 > 0 → sí
400 > 0 → sí
300 > 0 → sí
200 > 0 → sí
100 > 0 → sí
0 > 0   → no
"""
#membership in

categories = ["food", "rent", "transport"]

print("food" in categories)

#da True

#continue

transactions = [500, -100, 300]

for transaction in transactions:
    if transaction < 0:
        continue

    print(transaction)

# da 500
#    300