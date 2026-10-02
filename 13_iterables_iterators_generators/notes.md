13 — Iterables, Iterators and Generators

La idea general es entender cómo funciona realmente un for por debajo y cómo podemos procesar datos de forma perezosa, uno por uno, sin cargar todo en memoria.

iterable
↓ iter()
iterator
↓ next()
valor
↓ next()
valor
↓ ...
StopIteration

1. Iterable vs Iterator

Un iterable es un objeto que se puede recorrer.

list
tuple
set
dict
str
range

Un iterator:
- produce valores uno por uno;
- recuerda su posición;
- se consume;
- implementa el protocolo de iteración.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20

2. Dos iteradores sobre el mismo iterable son independientes

numbers = [10, 20, 30]

iterator1 = iter(numbers)
iterator2 = iter(numbers)

print(next(iterator1))  # 10
print(next(iterator1))  # 20

print(next(iterator2))  # 10

3. Qué hace realmente un for

for number in numbers:
    print(number)

es conceptualmente esto:

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
    except StopIteration:
        break

    print(number)

4. Un iterator se consume

numbers = [10, 20, 30]

iterator = iter(numbers)

for number in iterator:
    print(number)

luego de nuevo

for number in iterator:
    print(number)

la segunda vuelta no imprime nada.

Porque el iterator ya fue consumido.

5. Generators

Un generator es una forma cómoda de crear iterators. se define como funcion noraml pero usa yield

ejemplo

def generate_numbers():
    yield 10
    yield 20
    yield 30

generator = generate_numbers()

el cuerpo de la función todavía no se ejecuta completamente. Obtienes un objeto generator.

print(type(generator)) da <class 'generator'>

print(next(generator)) si da 10 ejecuta yield 10 Después la función se pausa, 
se puede poner otro next(generator) y dara 20

6. yield vs return

def get_number():
    return 10
    return 20

la funcion nunca llega a 20

Con yield:

def get_numbers():
    yield 10
    yield 20

con llamadas sucesivas de next da 10 y 20

7. Estado interno del generator

def countdown(start):
    while start > 0:
        yield start
        start -= 1

counter = countdown(3)

print(next(counter))  # 3
print(next(counter))  # 2
print(next(counter))  # 1

8. El for funciona perfectamente con generators

for number in countdown(3):
    print(number)

da 
3
2
1

El for internamente va pidiendo valores con next() hasta recibir StopIteration.

9. Generator expressions

asi como existe

squares = [
    number ** 2
    for number in range(5)
]

tambien hay

squares = (
    number ** 2
    for number in range(5)
)

[ ... ] → list
( ... ) → generator expression

La lista crea todos los resultados inmediatamente, El generator los produce cuando se necesitan.

10. Lazy evaluation

no calcules el siguiente valor hasta que alguien lo pida.

generator = (
    number ** 2
    for number in range(1_000_000)
)

No crea una lista con un millón de resultados de golpe.
Solo guarda el estado necesario para ir generándolos.
Por eso generators pueden ahorrar mucha memoria.

11. List vs Generator

numbers = [number for number in range(1_000_000)]

crea todos los enteros en memoria.

numbers = (number for number in range(1_000_000)) los crea uno a uno

12. Generator consumido

Esto es uno de los errores más comunes.

generator = (
    number
    for number in [10, 20, 30]
)

print(list(generator))

produce [10, 20, 30]

pero luego print(list(generator)) da [] porque ya fue consumido.
se debe crear otro generador

13. __iter__() en nuestras clases

class Account:
    def __init__(self):
        self.transactions = []

se añade esto

def __iter__(self):
    return iter(self.transactions)

asi se puede hacer esto

for transaction in account:
    print(transaction)

en ves de 

for transaction in account.transactions:
    print(transaction)

implementacion:
return iter(self.transactions)

14. __iter__() no significa necesariamente que la clase sea su propio iterator

Hay una diferencia.
Puedes tener:
class Account:    def __iter__(self):
        return iter(self.transactions)

Account es iterable.
Pero no es necesariamente el iterator.
El iterator real es:
iter(self.transactions)

15. Iterator personalizado con __next__

class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value

uso:

Uso:
counter = Counter(3)
    for value in counter:
        print(value)


produce:
1
2
3

Aquí:
__iter__()→ devuelve el iterator__next__()→ produce el siguiente valor


Y como Counter es su propio iterator:
return self

16. Generator para filtrar transacciones

def amounts_over(transactions, minimum):
    for transaction in transactions:
        if transaction.amount > minimum:
            yield transaction.amount

uso 
for amount in amounts_over(transactions, 200):
    print(amount)

el generador no necesita coontruir toda la lista [500, 1000, 3000, ...]

va encontrando uno valido y lo entrega con yield