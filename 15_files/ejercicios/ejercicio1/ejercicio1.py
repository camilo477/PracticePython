# Exercise 1 — Archivo de texto + errores
# Crea:
# data/amounts.txt

# con:
# 500
# hello
# 300
# -100

# Crea:
# load_amounts(path)


# Debe:
# - usar Path;
# - abrir con encoding="utf-8";
# - leer línea por línea;
# - convertir cada línea a float;
# - si una línea produce ValueError, mostrar:Invalid amount: <valor>
  
#   y continuar;
# - devolver solo los valores válidos.
# Si el archivo no existe:
# Amounts file not found

# y devuelve [].
from pathlib import Path

path = Path("data") / "amounts.txt"

with open(path, "w", encoding="utf-8") as file:
        file.write("500\n")
        file.write("hello\n")
        file.write("300\n")
        file.write("-100\n")

def load_amounts(path):
    lista = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    lista.append(float(line))
                except ValueError:
                    print("Invalid amount: " + line.strip())
    except FileNotFoundError:
        print("Amounts file not found")
        return []
    return lista

print(load_amounts(path))