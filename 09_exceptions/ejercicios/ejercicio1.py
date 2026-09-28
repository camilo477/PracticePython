# Ejercicio 1 — Conversión robusta
# Tienes:
# values = ["500", "hello", "300", "", "-100"]


# Crea una función:
# parse_amounts(values)


# Debe:
# - recorrer values;
# - intentar convertir cada elemento a float;
# - si ocurre ValueError, imprimir:
# Invalid amount: <valor>

# - continuar procesando los demás valores;
# - guardar solamente las conversiones correctas;
# - devolver la lista final.
# Resultado esperado conceptualmente:
# [500.0, 300.0, -100.0]


# Aquí practicarás:
# for
# try/except
# continue natural del loop
# return
# ValueError

values = ["500", "hello", "300", "", "-100"]

def parse_amounts(values):
    new_values = []
    for value in values:
        try:
            new_value = float(value)
        except ValueError:
            print(f"Invalid amount: {value}")
            continue
        new_values.append(new_value)
    return new_values

print(parse_amounts(values))