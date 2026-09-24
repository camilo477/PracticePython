# Primero no ejecutes este código. Predice qué va a pasar:

# def add_category(category, categories=[]):
#     categories.append(category)
#     return categories


# first = add_category("food")
# second = add_category("transport")

# print(first)
# print(second)
# print(first is second)

# Quiero que respondas primero:
# 1. ¿Qué crees que imprime first?
# 2. ¿Qué crees que imprime second?
# 3. ¿first is second será True o False?
# 4. ¿Por qué?
# Después ejecútalo y compara con tu predicción.
# Luego corrige la función para evitar el problema usando este patrón:
# def add_category(category, categories=None):    ...


# Requisitos de la versión corregida:
# - si no se pasa categories, debe crear una lista nueva;
# - agregar category;
# - devolver la lista;
# - dos llamadas independientes como:
# first = add_category("food")second = add_category("transport")


# deben producir listas independientes.

#1. firs imprime food, transport
#2. second imprime food, transport
#3. es true
#4. porque categories=[] crea una lista y esa queda creada

# first ──────┐
#             ├──→ ["food", "transport"]
# second ─────┘

def add_category(category, categories=None):
    if categories is None:
        categories = []
    categories.append(category)
    return categories


first = add_category("food")
second = add_category("transport")

print(first)
print(second)
print(first is second)