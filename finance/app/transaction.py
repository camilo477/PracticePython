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
            raise TypeError("amount must be int o float")
        if self.amount <= 0:
            raise ValueError("Amount can't be less or equal to 0")
        if self.transaction_type not in self.ALLOWED_TYPES:
            raise ValueError("transaction type must be income or expense")

