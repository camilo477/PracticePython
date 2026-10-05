# Exercise 2 — CSV
# Crea:
# data/transactions.csv

# con header:
# type,amount

# Crea dos funciones:
# save_transactions(transactions, path)
# load_transactions(path)


# Para este ejercicio transactions será:
# [    {"type": "income", "amount": 500},
#     {"type": "expense", "amount": 100},]


# save_transactions():
# - usa csv.DictWriter;
# - usa writeheader();
# - usa writerows().
# load_transactions():
# - usa csv.DictReader;
# - convierte amount a float;
# - devuelve una lista de diccionarios.
# No uses split(",").

import csv
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
path = Path("data") / "transactions.csv"

fieldnames = ["type", "amount"]

transactions = [{"type": "income", "amount": 500},
    {"type": "expense", "amount": 100},]

def save_transactions(transactions, path):
    needs_header = not path.exists() or path.stat().st_size == 0
    with open(path, "a", newline="") as file:
        writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )
        if needs_header:
            writer.writeheader()
        writer.writerows(transactions)
    
def load_transactions(path):
    result = []
    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            result.append(row)
    return result

save_transactions(transactions, path)
print(load_transactions(path))
    
