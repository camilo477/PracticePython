06 — Loops y Membership

loop repite una opreacion

membreship comprueba si algo pertenece a una coleccion

1. for

sirve para recorrer un iterable.

2. rangue()

cuando quiera repetir usando un rango de numero

por ejemplo usar esto
range(2, 6)

representa 2, 3, 4, 5

y esto

range(0, 10, 2)

0, 2, 4, 6, 8

range(start, stop, step)

esto funciona

transactions = [500, -100, 300]

for i in range(len(transactions)):
    print(transactions[i])

pero mejor asi:

for transaction in transactions:
    print(transaction)

4. enumerate()

Si necesitas posición + valor

Mentalmente enumerate() produce pares:

for index, transaction in enumerate(transactions):
    print(index, transaction)

5. while

Repite mientras una condición sea verdadera.

balance = 500

while balance > 0:
    print(balance)
    balance -= 100

diferencia
for
→ recorro algo

while
→ repito mientras una condición se cumpla

6. Membership: in

Membership significa comprobar pertenencia.

devuelve bool

categories = ["food", "rent", "transport"]

print("food" in categories)

da true

sirve con strings tambien

"py" in "python" da true

aqui

account = {
    "owner": "Camilo",
    "balance": 1000
}

"balance" in account

comprueba claves no valores

7. not in

es lo contrario a in , verifica si no esta dentro de 

8. continue

significa:

No sigas ejecutando esta iteración. Pasa a la siguiente.

Ejemplo:

transactions = [500, -100, 300]

for transaction in transactions:
    if transaction < 0:
        continue

    print(transaction)

Cuando llega a:

-100

ocurre

transaction < 0
↓
continue
↓
salta el resto de esta vuelta
↓
pasa a 300

da 500
300

9. break

termina completamente el loop.

transactions = [500, 300, 1000, 2000]

for transaction in transactions:
    if transaction > 900:
        print(transaction)
        break

Encuentra:

1000

y termina.

Nunca llega a procesar 2000.

10. Acumuladores

Un acumulador guarda un resultado que va creciendo.

transactions = [100, 200, 300]

total = 0

for transaction in transactions:
    total += transaction

11. Contadores

Muy parecido, pero en vez de sumar valores, contamos cuántas veces ocurre algo.