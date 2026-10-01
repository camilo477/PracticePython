# Exercise 3 — Typing
# Escribe anotaciones correctas para estas funciones:
# calculate_total(...)find_transaction(...)add_category(...)


# Con estas intenciones:
# calculate_total
# → recibe list[float]
# → devuelve float

# find_transaction
# → recibe list[Transaction] y un índice int
# → devuelve Transaction o None

# add_category
# → recibe set[str] y str
# → no necesita devolver nada

# No quiero implementación complicada. 
# El objetivo es que tú escribas correctamente los tipos.

from dataclasses import dataclass
from typing import ClassVar, Literal

TransactionType = Literal["income", "expense"]

@dataclass
class Transaction:
    ALLOWED_TYPES: ClassVar[tuple[str, ...]] = (
        "income",
        "expense"
    )

    amount: float
    transaction_type: TransactionType
    description: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.amount, (int, float)):
            raise TypeError("Amount must be numeric")

        if self.amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if self.transaction_type not in self.ALLOWED_TYPES:
            raise ValueError("Invalid transaction type")

def calculate_total(amount: list[float]) -> float:
    return sum(amount)

def find_transaction(transactions: list[Transaction], 
                     index: int) -> Transaction | None:
    try:
        return transactions[index]
    except IndexError:
        return None


def add_category(categories: set[str], category: str) -> None:
    categories.add(category)
