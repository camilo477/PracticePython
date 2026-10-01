# Exercise 2 — field(default_factory=...)
# Crea:
# @dataclassclass BudgetCategory:


# Campos:
# name: str
# limit: float
# expenses: list[float]

# expenses debe empezar como una lista nueva para cada instancia usando:
# field(default_factory=list)


# Añade:
# add_expense(amount)get_total_spent()get_remaining()


# Reglas:
# - limit > 0;
# - expense > 0;
# - cada instancia debe tener su propia lista.
# Prueba con dos categorías para demostrar independencia.

from dataclasses import dataclass, field


@dataclass
class BudgetCategory:
    name: str
    limit: float
    expenses: list[float] = field(default_factory=list)
    def __post_init__(self) -> None:
        if self.limit <= 0:
            raise ValueError("limit debe ser mayor que 0")
    def add_expense(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount para expense debe ser mayor que 0")
        self.expenses.append(amount)
    def get_total_spent(self) -> float:
        return sum(self.expenses)
    def get_remaining(self) -> float:
        return self.limit - self.get_total_spent()

category1 = BudgetCategory("camilo", 700)
category2 = BudgetCategory("diana", 1000)

print(category1.expenses)
print(category2.expenses)

print(category1.expenses is category2.expenses)

    