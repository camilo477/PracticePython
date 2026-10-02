12 — Dataclasses and Typing

dataclass
→ reducir código repetitivo en clases que principalmente almacenan datos

typing
→ documentar qué tipos esperamos recibir y devolver

1. Dataclasses
Antes, una clase simple como Transaction podría verse así:

class Transaction:
    def __init__(self, amount, transaction_type, description):
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description

    def __repr__(self):
        return (
            f"Transaction("
            f"amount={self.amount!r}, "
            f"transaction_type={self.transaction_type!r}, "
            f"description={self.description!r}"
            f")"
        )
    
Con dataclass:

from dataclasses import dataclass


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    description: str

Python genera automáticamente varias cosas, incluyendo principalmente:

__init__
__repr__
__eq__

objeto principalmente de datos
→ considerar dataclass

objeto con comportamiento/estado complejo
→ clase normal puede ser mejor

2. __post_init__

Una dataclass genera el __init__, pero todavía podemos validar los datos inmediatamente después de construirla mediante:

def __post_init__(self):

ejemplo

from dataclasses import dataclass


@dataclass
class Transaction:
    amount: float
    transaction_type: str

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be greater than 0")

3. ClassVar

from typing import ClassVar


@dataclass
class Transaction:
    ALLOWED_TYPES: ClassVar[tuple[str, ...]] = (
        "income",
        "expense"
    )

    amount: float
    transaction_type: str
4. field()

dataclasses.field() permite controlar cómo se comporta un campo.

@dataclass
class AccountData:
    transactions: list[Transaction] = field(default_factory=list)

default_factory=list significa:
crea una lista nueva para cada instancia.

repr=False para ocultar algo del repr automatico que hace dataclass

init=False Puedes evitar que un campo sea argumento del constructor

@dataclass
class AccountSummary:
    income: float
    expenses: float
    balance: float = field(init=False)

5. Typing

esto def deposit(amount: float) -> float:

indica:
amount
→ esperamos float

-> float
→ esperamos devolver float

no obliga es solo para informar en codigo

Tipos básicos

name: str
age: int
amount: float
active: bool

def calculate_total(amounts: list[float]) -> float:
    return sum(amounts)

6. Colecciones tipadas

Lista:
transactions: list[Transaction]

Diccionario:
balances: dict[str, float]


Set:
categories: set[str]


Tuple de longitud conocida:
coordinates: tuple[float, float]


Tuple con cantidad variable de strings:
allowed_types: tuple[str, ...]


Ese ... significa:
puede contener cualquier cantidad de elementos, pero todos son str.

7. None y unions

description: str | None


Eso significa:
description puede ser:
str
O
None

Pero esto:
description: str | None

Si quieres que además sea opcional al construir:
description: str | None = None

8. Literal

Desde typing podemos restringir la intención:

from typing import Literal


transaction_type: Literal["income", "expense"]

Podemos crear un alias:
TransactionType = Literal["income", "expense"]


y reutilizarlo:
@dataclassclass Transaction:    amount: float    transaction_type: TransactionType

