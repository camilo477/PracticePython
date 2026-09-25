# Ejercicio 3 — zip() + enumerate()
# Tienes:
# categories = ["food", "rent", "transport"]limits = [300, 800, 150]
# Haz tres cosas:
# 1. Usa zip() para imprimir:
# food -> 300
# rent -> 800
# transport -> 150

# 2. Construye un diccionario usando:
# dict(...)

# y zip(), de forma que obtengas:
# {    "food": 300,    "rent": 800,    "transport": 150}

# 3. Recorre después ese diccionario usando:
# enumerate(..., start=1)

# junto con .items() para imprimir:
# 1. food -> 300
# 2. rent -> 800
# 3. transport -> 150

categories = ["food", "rent", "transport"]
limits = [300, 800, 150]

for category, limit in zip(categories, limits):
    print(f"{category} -> {limit}")

transactions = dict(zip(categories, limits))

        
print (transactions)

for number, (category, limit) in enumerate(transactions.items(), start=1):
    print(number, category, "->", limit)
