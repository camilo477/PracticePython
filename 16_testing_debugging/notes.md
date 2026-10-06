16 — Testing & Debugging
La idea general es separar dos problemas:

Testing
→ comprobar automáticamente que el código hace lo que esperamos

Debugging
→ investigar por qué el código NO está haciendo lo que esperamos

1. assert
La forma más básica de comprobar algo en Python es:
assert expresion

ejemplo:

def calculate_balance(income, expenses):
    return income - expenses


assert calculate_balance(1000, 300) == 700

con true no pasa nada, con false, python manda AssertionError

se le puede añadir un mensaje:

assert calculate_balance(1000, 300) == 700, "Incorrect balance"

2. Pytest

estructura sencilla

project/
├── calculations.py
└── tests/
    └── test_calculations.py

en calculations.py:

def calculate_balance(income, expenses):
    return income - expenses

en tests/test_calculations.py:

from calculations import calculate_balance


def test_calculate_balance():
    result = calculate_balance(1000, 300)

    assert result == 700

se ejecuta python -m pytest

3. Arrange — Act — Assert

Arrange
→ preparar datos

Act
→ ejecutar lo que quiero probar

Assert
→ comprobar resultado

ejemplo:

def test_withdraw():
    # Arrange
    balance = 1000
    amount = 200

    # Act
    result = withdraw(balance, amount)

    # Assert
    assert result == 800

4. Casos normales, límites y errores

Caso normal

withdraw(1000, 200)
→ 800

Boundary / límite

withdraw(1000, 1000)
→ 0

Caso inválido

withdraw(1000, -50)
→ ValueError

5. Probar excepciones con pytest.raises

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount

en pytest

import pytest


def test_withdraw_rejects_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)

tambien se puede inspeccionar el mensaje:
def test_withdraw_rejects_insufficient_funds():
    with pytest.raises(ValueError) as error:
        withdraw(1000, 1500)

    assert str(error.value) == "Insufficient funds"

6. Parametrización

parametrizar varias pruebas

import pytest


@pytest.mark.parametrize(
    "income, expenses, expected",
    [
        (1000, 200, 800),
        (500, 100, 400),
        (300, 300, 0),
    ],
)
def test_calculate_balance(income, expenses, expected):
    result = calculate_balance(income, expenses)

    assert result == expected

7. Testing de clases

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

se puede probar

def test_deposit_updates_balance():
    account = Account(1000)

    account.deposit(500)

    assert account.balance == 1500

8. Fixtures

Si varios tests necesitan crear lo mismo:
account = Account(1000)

puedes usar una fixture:

import pytest


@pytest.fixture
def account():
    return Account(1000)

def test_deposit(account):
    account.deposit(500)

    assert account.balance == 1500


def test_withdraw(account):
    account.withdraw(200)

    assert account.balance == 800

9. Testing de archivos con tmp_path

tmp_path que te da un directorio temporal para pruebas.

ejemplo:

def test_save_transactions(tmp_path):
    path = tmp_path / "transactions.json"

    save_transactions([], path)

    assert path.exists()

evita escribir archivos reales mientras ejecutas tests.

10. Debugging

Un buen proceso es:

1. reproducir
2. leer error/traceback
3. aislar
4. formular hipótesis
5. inspeccionar estado
6. corregir causa
7. volver a probar

11. Leer un traceback

ejemplo:
def divide(a, b):
    return a / b


def calculate():
    return divide(10, 0)


calculate()

daria:

Traceback (most recent call last):
  File "main.py", line 8, in <module>
    calculate()

  File "main.py", line 5, in calculate
    return divide(10, 0)

  File "main.py", line 2, in divide
    return a / b

ZeroDivisionError: division by zero

Una estrategia útil:
Empieza por el final:
ZeroDivisionError: division by zero

Luego la línea más cercana al origen:

return a / b

Y después subes por la cadena:

calculate()
↓
divide()
↓
error

12. breakpoint()
Python incluye:
breakpoint()


Ejemplo:
def calculate_balance(income, expenses):    breakpoint()    return income - expenses


Al ejecutar, Python pausa ahí y abre el debugger.
Puedes inspeccionar:
income
expenses
type(income)

13. Comandos básicos de pdb

n
→ next line

s
→ step into function

c
→ continue

p variable
→ print variable

q
→ quit