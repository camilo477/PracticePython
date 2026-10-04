# Exercise 1 — Decorator básico
# Crea:
# @log_operationdef
#  calculate_total(amounts):
#     return sum(amounts)


# log_operation debe imprimir:
# Starting operation

# antes de ejecutar la función y:
# Operation finished

# después.
# Debe conservar correctamente el valor
# retornado por calculate_total().
# Usa:
# amounts = [100, 200, 300]


# Resultado final esperado:
# Starting operation
# Operation finished
# 600

# Usa *args, **kwargs y @wraps.
from functools import wraps

def log_operation(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Starting operation")
        result = function(*args, **kwargs)
        print("Operation finished")
        return result
    return wrapper
        

@log_operation
def calculate_total(amounts):
    return sum(amounts)

amounts = [100, 200, 300]

print(calculate_total(amounts))