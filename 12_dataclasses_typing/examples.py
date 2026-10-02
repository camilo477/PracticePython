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

# @dataclass
# → genera estructura repetitiva

# typing
# → comunica tipos esperados

# Literal
# → restringe intención del tipo

# ClassVar
# → regla compartida

# __post_init__
# → valida realmente en runtime