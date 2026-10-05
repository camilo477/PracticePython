- Confundir dump y dumps

json.dump(data, file)
necesita el archivo.

Si haces: json.dump(data)

te dirá que falta fp.

Mientras: json.dumps(data)

devuelve un str.

- json.loads() no modifica el string
esto:
json.loads(json_text)
devuelve un objeto Python.

Si no guardas el resultado:

json.loads(json_text)

print(type(json_text))

json_text sigue siendo str.

- Llamar load_transactions() varias veces

Esto fue importante:
add_transaction(load_transactions(), new_transaction)save_transactions(load_transactions())


No es la misma lista.
Cada llamada vuelve a leer el archivo y crea nuevos objetos en memoria.
Mejor:
transactions = load_transactions()add_transaction(transactions, new_transaction)save_transactions(transactions)


Así mantienes referencia a la misma lista modificada.

- Mezclar dict y Transaction

Evita terminar con:

[
    Transaction(...),
    Transaction(...),
    {"amount": 500}
]

- asdict() demasiado pronto

No conviertas una Transaction a dict apenas la creas si quieres trabajar internamente con objetos.

