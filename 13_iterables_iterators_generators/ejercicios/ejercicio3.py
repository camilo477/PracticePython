# Exercise 3 — Estado del generator
# Crea:
# countdown(start)


# con yield.
# Por ejemplo:
# generator = countdown(3)


# Después usa manualmente:
# next(generator)


# para obtener:
# 3
# 2
# 1

# Luego captura el StopIteration.
# Quiero que expliques dónde queda guardado conceptualmente el valor de start entre cada next().

def countdown(start):
    current = start
    for _ in range(start):
        yield current
        current -= 1


generator = countdown(3)

print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print("se paro no hay mas")