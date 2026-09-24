# Tienes este set:
# allowed_categories = {
#     "salary",
#     "food",
#     "transport"
# }
# Primero crea:
# category = "food"
# y comprueba con in si está permitido.
# Después cambia a:
# category = "gaming"
# y usando not in, imprime:
# Invalid category
# si no pertenece al set.

allowed_categories = {
    "salary",
    "food",
    "transport"
}

category = "food"

print(category in allowed_categories)

category = "gaming"

if category not in allowed_categories:
    print("Invalid category")