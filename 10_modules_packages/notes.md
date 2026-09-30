La idea general es organizar código para no terminar con aplicaciones gigantes en un solo archivo.

Un paquete agrupa varios módulos:

finance/
├── __init__.py
├── calculations.py
└── validators.py

ejemplo al

para llamarlos es asi

from calculations import calculate_balance

o con alias

import calculations as calc

tambien se puede esto, pero es mejor llamar funcion por funcion

from calculations import *

from calculations import calculate_balance, calculate_tax

import calculations calculations → módulo

from calculations import calculate_balance calculate_balance → función


asi es que

import calculations

calculate_balance(...)

no sirve, seria:

calculations.calculate_balance(...)

python ejecuta un modulo al importarlo

entonces

# calculations.py

print("Loading calculations")


def calculate_balance(income, expenses):
    return income - expenses

# main.py

import calculations

cuando se ejecute main.py saldra

Loading calculations

1. __name__ y __main__
Cada módulo tiene una variable especial:

python calculations.py

__name__ == "__main__"

si se hace
import calculations

desde otro archivo: calculations.__name__

sale calculations

esto

def calculate_balance(income, expenses):
    return income - expenses


if __name__ == "__main__":
    print(calculate_balance(2000, 500))

Ejecuta esta parte solamente si este archivo fue ejecutado directamente, no si fue importado.

2. Packages

tenemos

ejercicios/
├── main.py
└── finance/
    ├── __init__.py
    ├── calculations.py
    └── validators.py

en
# finance/calculations.py

def calculate_balance(income, expenses):
    return income - expenses

y en # finance/validators.py

def validate_amount(amount):
    return amount > 0

desde main se llama asi 
from finance.calculations import calculate_balance
from finance.validators import validate_amount

3. __init__.py

Tradicionalmente __init__.py indica que una carpeta es un package de Python.
También puede definir qué queremos exponer como API pública del paquete.

ejemplo

# finance/__init__.py

from .calculations import calculate_balance
from .validators import validate_amount

se puede hacer 

from finance import calculate_balance, validate_amount

en ves de 

from finance.calculations import calculate_balance
from finance.validators import validate_amount

4. Imports absolutos y relativos

Dentro de un package puedes usar imports absolutos:

from finance.validators import validate_amount

o relativos:

from .validators import validate_amount

El punto significa que es el paquete

doble punto es package padre ..

5. -m

python archivo.py
→ ejecuta un archivo directamente

python -m package.module
→ ejecuta un módulo respetando su package

