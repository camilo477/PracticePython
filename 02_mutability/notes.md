¿Qué pasa si dos variables referencian el mismo objeto y ese objeto puede modificarse?

numbers = [1, 2]

other = numbers

other.append(3)

numbers ──┐
          ├──→ [1, 2]
other ────┘

cuando se hace algo al objeto modificable cambia el objeto

hacer esto other.append(3) hara que esto suceda:

numbers ──┐
          ├──→ [1, 2, 3]
other ────┘

tipos mutables usados hasta ahora:

list
dict
set

inmutables:

int
float
str
bool
tuple

importante, esto backup = transactions no copia la lista

esto si la copia backup = transactions.copy()

Entonces:

transactions =[100, 200]

backup = [100, 200]

transactions == backup  # True
transactions is backup  # False

al hacer copias de una lista con elementos dentro
la lista es diferente pero las listas contienen objeto compartido

ejemplo:

accounts = [
    {"name": "Savings", "balance": 1000}
]

backup = accounts.copy()

accounts ──→ lista A ──┐
                       ├──→ mismo dict
backup ────→ lista B ──┘

a esto se le llama shadow copy

una deep copy es una copia tanto del objeto mutable como de los objetos
dentro de este

copia = copy.deepcopy(original)

original ──→ lista A ──→ dict A

copia ─────→ lista B ──→ dict B