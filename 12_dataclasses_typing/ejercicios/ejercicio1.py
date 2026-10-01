# Exercise 1 — Convertir Transaction a dataclass
# Toma tu clase Transaction del módulo anterior y 
# conviértela a dataclass.
# Debe tener:
# amount: float
# transaction_type
# description opcional

# Usa:
# TransactionType = Literal["income", "expense"]


# y:
# transaction_type: TransactionType


# Requisitos runtime en __post_init__():
# - amount debe ser int o float;
# - amount > 0;
# - tipo permitido "income" o "expense".
# Define también:
# ALLOWED_TYPES


# como ClassVar.
# No escribas manualmente:
# __init____repr__


# porque queremos que lo haga dataclass.
# Prueba al menos:
# Transaction(500, "income")
# Transaction(100, "expense", "Food")
# Transaction(-100, "expense")
# Transaction(100, "invalid")

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
    
    def __post_init__(self):
        if not isinstance(self.amount,(int,float)):
            raise TypeError("amount debe ser int o float")
        if self.amount <= 0:
            raise ValueError("amount debe ser mayor que 0")
        if self.transaction_type not in self.ALLOWED_TYPES:
            raise ValueError("transaction_type debe estar en los tipos permitidos")

try:
    Transaction(500, "income")
except (TypeError, ValueError) as e:
    print(f"error, {e}")
try:
    Transaction(100, "expense", "Food")
except (TypeError, ValueError) as e:
    print(f"error, {e}")
try:
    Transaction(-100, "expense")
except (TypeError, ValueError) as e:
    print(f"error, {e}")
try:
    Transaction(100, "invalid")
except (TypeError, ValueError) as e:
    print(f"error, {e}")