08 — Comprehensions e Idiomatic Tools

los comprehensions e idiomatic tools sirven para escribir python de manera mas expresiva , usar contrucciones que expresen la intencion de manera clara

Comprehensions: list, dict y set

Una comprehension permite construir una colección nueva recorriendo otra colección.

transactions = [100, 200, 300]

doubled = [amount * 2 for amount in transactions]

da [200, 400, 600]

se puede tambien filtrar

transactions = [500, -100, 300, -50]

income = [amount for amount in transactions if amount > 0]

da [500, 300]

Dict comprehension
Misma idea, pero construyendo un diccionario:

categories = ["food", "rent", "transport"]

limits = {
    category: 0
    for category in categories
}

da

{
    "food": 0,
    "rent": 0,
    "transport": 0
}

Set comprehension
Construye un set:

transactions = [
    {"category": "food"},
    {"category": "transport"},
    {"category": "food"},
]

categories = {
    transaction["category"]
    for transaction in transactions
}

da 

{"food", "transport"}

Como es un set, los duplicados desaparecen.


2. enumerate() y zip()

Cuando necesitas índice + valor:

for index, transaction in enumerate(transactions):
    ...

da

(0, elemento)
(1, elemento)
(2, elemento)

for number, transaction in enumerate(transactions, start=1):
    print(number, transaction)

da
1 ...
2 ...
3 ...

zip() sirve para recorrer varias colecciones en paralelo.

categories = ["food", "rent", "transport"]
limits = [300, 800, 150]

for category, limit in zip(categories, limits):
    print(category, limit)

da

("food", 300)
("rent", 800)
("transport", 150)

result = dict(zip(categories, limits))

da

{
    "food": 300,
    "rent": 800,
    "transport": 150
}

Si las colecciones tienen diferente longitud zip() termina cuando se acaba la más corta.

3. any(), all(), sum(), min(), max() y sorted()

any()
Pregunta:
¿Hay al menos un elemento verdadero?

values = [False, False, True]

any(values) # true

transactions = [500, 300, -100, 200]

has_expenses = any(
    amount < 0
    for amount in transactions
)

all()

es todos cumplen?

transactions = [100, 200, 300]

all(amount > 0 for amount in transactions) # true

sum()

amounts = [500, 300, 200]

total = sum(amounts) # da 1000

min() y max()

amounts = [500, 120, 900]

min(amounts)
# 120

max(amounts)
# 900

sorted()

numbers = [3, 1, 2]

ordered = sorted(numbers)

sorted devuelve otra lista

numbers → [3, 1, 2]
ordered → [1, 2, 3]

numbers.sort() muta la lista original

4. LAMBDA

queresmos ordenar objetos más complejos con key

sorted(
    transactions,
    key=lambda transaction: transaction["amount"]
)

entonces aqui que pasa

Una lambda es una función pequeña anónima.

def double(number):
    return number * 2

es lo mismo que

lambda number: number * 2

lambda resulta especialmente útil como función pequeña pasada a otra función.

en la de arriba esta:

sorted(
    transactions,
    key=lambda transaction: transaction["amount"]
)

hace esto

Transaction A
↓ lambda
2500

Transaction B
↓ lambda
100

Transaction C
↓ lambda
80

↓
ordena usando esos valores