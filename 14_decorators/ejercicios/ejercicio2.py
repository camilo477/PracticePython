# Exercise 2 — Decorator con parámetros
# Crea:
# @repeat(3)def show_transaction(amount):    print(f"Transaction: {amount}")


# Debe imprimir tres veces:
# Transaction: 500

# Requisitos:
# - repeat(times) recibe el número;
# - debe haber tres niveles;
# - usa @wraps;
# - wrapper debe aceptar *args, **kwargs.
# No copies el ejemplo anterior literalmente: intenta reconstruir
#  mentalmente:
# repeat(times)
# → decorator(function)
# → wrapper(*args, **kwargs)

from functools import wraps

def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator
          

@repeat(3)
def show_transaction(amount):
        print(f"Transaction: {amount}")

show_transaction(500)