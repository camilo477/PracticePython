15 — Files
La idea principal es persistencia.

1. Abrir, leer y escribir archivos

La función básica es:

open(...)

ejemplo: file = open("transactions.txt", "r")

pero normalmente no usamos esta forma directamente, porque luego tendríamos que recordar:

file.close()

es mejor

with open("transactions.txt", "r") as file:
    content = file.read()

file no es una palabra especial. Es simplemente una variable que referencia el objeto archivo abierto.
with open("transactions.txt", "r") as archivo: tambien sirve

2. Modos r, w, a

- r leer:

Sirve para leer.

- w write:

Si no existe lo crea

Si ya existe BORRA el contenido anterior empieza desde cero

- a append:

Si no existe lo crea

Si ya existe mantiene el contenido y escribe al final

3. Leer todo vs línea por línea

with open("transactions.txt", "r") as file:
    content = file.read()

read() carga todo el contenido como un str.

with open("transactions.txt", "r") as file:
    for line in file:
        print(line)

El archivo es iterable y vas procesando una línea a la vez.

4. strip()

strip() elimina whitespace de los extremos, incluyendo saltos de línea.

5. write()

with open("transactions.txt", "w") as file:
    file.write("income,500\n")

Si haces:
file.write("income,500")
file.write("expense,100")

dara income,500expense,100

por eso se puede usar \n 
file.write("income,500\n")

6. Manejo de errores al leer archivos

try:
    with open("transactions.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Transactions file not found")

para que una linea "mala" no detenga lo siguiente, se usa

try:
    with open(...) as file:
        for line in file:
            try:
                ...
            except ValueError:
                ...
except FileNotFoundError:
    ...

7. pathlib

En vez de usar strings por todas partes: "data/transactions.json"

se usa:

from pathlib import Path

path = Path("data") / "transactions.json"

El operador / aquí significa combinar partes de una ruta.

8. Crear carpetas

data_dir = Path("data")

data_dir.mkdir(exist_ok=True)

Si ya existe, exist_ok=True evita FileExistsError.

para rutas anidadas:

Path("data/finance/reports").mkdir(
    parents=True,
    exist_ok=True
)

9. Comprobar existencia

path.exists() da true o false

10. Tamaño del archivo

path.stat().st_size devuelve el tamaño en bytes

sirve para saber si esta vacio

if path.stat().st_size == 0:
    ...

11. Inspeccionar rutas

path = Path("data/reports/monthly_transactions.csv")

se puede usar

path.name → "monthly_transactions.csv"

path.parent → Path("data/reports")

path.suffix → ".csv"

path.stem → "monthly_transactions"

12. Ruta relativa, absoluta y cwd

Path.cwd() devuelve el current working directory.

mientras que path.resolve() convierte/resuelve una ruta a una ruta absoluta.

allgo asi

cwd
/home/project

path
data/transactions.json

resolve()
↓
/home/project/data/transactions.json

13. CSV

CSV es útil para datos tabulares.

type,amount
income,500
expense,100

con import csv

csv.reader

import csv

with open("transactions.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

una fila income,500 se vuelve en ["income", "500"]

csv.DictReader

with open("transactions.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["type"])
        print(row["amount"])

lo vuelve en {
    "type": "income",
    "amount": "500"
}

csv.DictWriter

para escribir

fieldnames = ["type", "amount"]

with open("transactions.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "type": "income",
        "amount": 500
    })

resulta en 

type,amount
income,500

writerow() vs writerows()

una fila:

writer.writerow({
    "type": "income",
    "amount": 500
})

varias:

transactions = [
    {"type": "income", "amount": 500},
    {"type": "expense", "amount": 100},
]

writer.writerows(transactions)

- newline=""

Cuando usamos csv, normalmente:
open(..., newline="")
porque dejamos que el módulo csv controle correctamente los saltos de línea.

14. JSON

JSON sirve mejor cuando los datos tienen estructura.

[
    {
        "type": "income",
        "amount": 2500
    },
    {
        "type": "expense",
        "amount": 100
    }
]

15. dump() y load()

import json

data = {
    "type": "income",
    "amount": 500
}

with open(
    "transaction.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(data, file)

Python dict/list
↓ json.dump()
archivo JSON

para leer:

with open(
    "transaction.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

archivo JSON
↓ json.load()
Python dict/list

16. dumps() y loads()

Aquí la s significa que trabajan con strings.

- json_text = json.dumps(data)

json_text es:

str

hace

Python
↓ json.dumps()
str JSON

- python_data = json.loads(json_text)

hace

str JSON
↓ json.loads()
Python

17. JSON legible

json.dump(
    data,
    file,
    indent=4,
    ensure_ascii=False
)

indent=4 hace el archivo más legible.
ensure_ascii=False permite guardar caracteres como:
á
é
ñ
y se abre con encoding="utf-8"


18. Encoding

with open(
    path,
    "r",
    encoding="utf-8"
) as file:


19. JSON inválido

{
    "amount": 500,
}

esa ultima coma hace el JSON invalido
entonces
json.load(file)

lanza json.JSONDecodeError

try:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

except FileNotFoundError:
    print("File not found")

except json.JSONDecodeError:
    print("Invalid JSON")

20. No todo Python es serializable a JSON

esto funciona:

dict
list
str
int
float
bool
None

esto no
data = {
    "categories": {"food", "rent"}
}

primero se convierte
list(categories)

21. Dataclasses y JSON

@dataclass
class Transaction:
    amount: float
    transaction_type: str

da objetos Transaction(...)

JSON no sabe qué significa tu clase. Entonces usamos:

from dataclasses import asdict

transaction_dict = asdict(transaction)

22. ¿CSV o JSON?

CSV
→ datos tabulares
→ filas/columnas
→ Excel/spreadsheets
→ simple para grandes tablas

JSON
→ estructura jerárquica
→ listas/dicts anidados
→ APIs
→ configuración
→ objetos más complejos
