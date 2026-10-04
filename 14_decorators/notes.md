14 — Decorators
La idea principal es:
Un decorator recibe una función y devuelve otra función que añade comportamiento alrededor de la original.

Normalmente sirve para reutilizar comportamiento transversal como:
logging
validaciones
permisos
medición de tiempo
reintentos
caché
autenticación

def greet(name):
    return f"Hello {name}"

usar greet es la funcion como objeto

greet("Camilo") lo ejecuta

other = greet

print(other("Camilo"))

esta bien

una funcion puede devolver otra funcion

def outer():
    def inner():
        return "Hello"

    return inner

1. Decorator básico

teniendo 
def deposit(amount):
    return f"Deposited {amount}"

queremos imprimir algo antes y depsues de ejecutarla, podemos crear:

def log_execution(function):
    def wrapper(amount):
        print("Starting operation")

        result = function(amount)

        print("Operation finished")

        return result

    return wrapper

y aplicamos esto

@log_execution
def deposit(amount):
    return f"Deposited {amount}"

con esto print(deposit(500))
da 
Starting operation
Operation finished
Deposited 500

esto es porque esto
@log_execution
def deposit(amount):
    ...
es esto
def deposit(amount):
    return f"Deposited {amount}"


deposit = log_execution(deposit)

¿Qué hace wrapper?

aqui
def log_execution(function):
    def wrapper(amount):
        print("Starting operation")

        result = function(amount)

        print("Operation finished")

        return result

    return wrapper


@log_execution
def deposit(amount):
    return f"Deposited {amount}"

es esto

wrapper(500)
↓
print antes
↓
function(500)
    ↓
    deposit original
↓
guardar result
↓
print después
↓
return result

2. El problema de parámetros diferentes: *args y **kwargs

Nuestro primer wrapper solo aceptaba:
def wrapper(amount):

pero con funciones asi
def deposit(amount):
    ...

def transfer(amount, origin, destination):
    ...

def create_transaction(amount, description=None):
    ...

Un decorator reutilizable no debería conocer exactamente todos los parámetros posibles.

para eso se usa 

*args
**kwargs

def log_execution(function):
    def wrapper(*args, **kwargs):
        print("Starting operation")

        result = function(*args, **kwargs)

        print("Operation finished")

        return result

    return wrapper

*args captura argumentos posicionales en una tuple:
args == (500, "Savings", "Checking")

**kwargs captura argumentos con nombre en un dict:

kwargs == {
    "amount": 500,
    "origin": "Savings",
    "destination": "Checking"
}

function(*args, **kwargs) los vuelve a desempaquetar para llamar a la función original.

para el return se usa esto

result = function(*args, **kwargs)
return result
recuerda el return

o directamente: return function(*args, **kwargs)

3. functools.wraps

con from functools import wraps

@wraps(function) preserva metadata de la función original como:

__name__
__doc__

4. Decorators con parámetros

@repeat(3)
def greet(name):
    print(f"Hello {name}")

Aquí el decorator necesita recibir primero: 3

por eso hay tres niveles

def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator

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
def greet(name):
    print(f"Hello {name}")

