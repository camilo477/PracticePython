04 — Dictionaries

Un dict guarda datos en pares:

clave → valor

para acceder a los valores

account = {
    "owner": "Camilo",
    "balance": 1200,
    "active": True
}

print(account["owner"]) da Camilo
print(account["balance"]) da 1200

Otra forma de acceder:
account.get("balance")

los diccionarios son mutables, para editar uno es asi

account["balance"] = 1500 cambia lo que hay en balance a 1500

se puede crear una nueva clave si no existe

account["currency"] = "COP"

clave existente → actualizar
clave inexistente → crear

Eliminar claves

del account["active"]

o con pop()

currency = account.pop("currency"), con pop devuelve el valor

ejemplo:

account = {
    "owner": "Camilo",
    "currency": "COP"
}

currency = account.pop("currency") devuelve "COP" y account ya no tiene "currency".

Membership con diccionarios

"balance" in account comprueba claves, no valores.

buscar por valor dara error, para eso se usa 1200 in account.values()


keys(), values(), items()

account.keys(), muestra las llaves

account.values() muestra los valores

account.items() muestra ambas claves y valores

Diccionarios anidados

account = {
    "owner": "Camilo",
    "balance": 1200,
    "transactions": [
        {"type": "income", "amount": 500},
        {"type": "expense", "amount": 100}
    ]
}

account["transactions"] da la lista
[
    {"type": "income", "amount": 500},
    {"type": "expense", "amount": 100}
]

account["transactions"][1] da {"type": "expense", "amount": 100}

account["transactions"][1]["amount"] dara 100
 
Acumulación con diccionarios

para pasar de:

transactions = [
    {"category": "food", "amount": 100},
    {"category": "transport", "amount": 50},
    {"category": "food", "amount": 80},
]

a 

{
    "food": 180,
    "transport": 50
}

el patron mental es

por cada transacción
↓
obtener categoría
↓
mirar cuánto llevamos acumulado
↓
sumar amount

totals.get(category, 0)

totals[category] = totals.get(category, 0) + amount

recuerda que get totals.get(category, 0) devuelve 0 como valor por defecto

Claves válidas

para ser una clave debe ser estos objetos

str
int
float
tuple (si contiene elementos hashables)




