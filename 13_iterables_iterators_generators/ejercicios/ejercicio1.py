# Exercise 1 — iter() / next()
# Tienes:
# transactions = [500, -100, 300]


# Haz lo siguiente:
# 1. crea un iterator con iter();
# 2. usa next() tres veces e imprime los resultados;
# 3. intenta un cuarto next();
# 4. captura StopIteration y muestra:
# No more transactions

# Después explica:
# - si transactions cambió;
# - qué objeto estaba recordando la posición.

transactions = [500, -100, 300]

iterator = iter(transactions)

print(next(iterator))

print(next(iterator))

print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("No more transactions")