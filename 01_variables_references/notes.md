Que es una variable?

Una variable no es el objeto, es decir es un numbre que referencia a un objeto

por ejemplo:

balance = 500

balance es la variable

esto es util porque varias variables pueden llamar al mismo objeto

ejemplo:

balance = 500
other_balance = balance

balance ───────┐
               ├────→ 500
other_balance ─┘

Reasignacion es  cambia a que referencia una variable, por ejemplo

balance = 500

balance = 900

no cambia 500, cambia a que referencia "balance"

Los nombres pueden cambiar de tipo

value = 100
value = "hello"
value = [1, 2, 3]

para consultar el tipo de una variable es con type()

ejemplo:

type(value)

Referencias:

al hacer esto

def show_balance(balance):
    print(balance)

amount = 500
show_balance(amount)

tanto amount como balance apuntan al mismo objeto

diferencia entre == y is, == es para saber si tienen el mismo valor pero is es para saber si es exactamente el mismo objeto

