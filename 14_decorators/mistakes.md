1. Ejecutar la función al decorar

Incorrecto:

return wrapper()

2. Ejecutar la función al pasarla

incorrecto:

decorator(my_function())

correcto:

decorator(my_function)

3. Olvidar devolver wrapper

def decorator(function):
    def wrapper():
        ...

sin

return wrapper

devuelve None

4. Wrapper demasiado específico

def wrapper(amount):

solo funciona con ciertas firmas.

Si el decorator pretende ser genérico:

def wrapper(*args, **kwargs):

5. Olvidar @wraps

El código puede funcionar, pero:
nombre
docstring
metadata

pueden quedar como los de wrapper.

