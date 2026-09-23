Listas:

una lista es una coleccion cone stas propiedades:
- ordenada;
- mutable;
- indexada;
- puede contener valores repetidos;
- puede contener objetos de distintos tipos.

ejemplo:

transactions = [500, -100, 250, -50]

índice:      0     1     2     3
valor:      500  -100   250   -50

transactions[0]   # 500
transactions[2]   # 250

tambien hay indices negativos:

transactions[-1]  # -50
transactions[-2]  # 250

  0      1      2      3
 500   -100    250    -50
 -4     -3     -2     -1

 si se intenta acceder a una posicion que no existe
 manda IndexError

 2. Modificar elementos

al ser mutables esto cambiaria el valor 

 transactions[1] = -120

3. append()

es para agregar al final de una lista un elemento

4. extend()

esto es para varios elementos

esto añadiria como 1 solo elemento
transactions.append([100, 200])

[500, -100, [100, 200]]

esto transactions.extend([100, 200]) los añade

[500, -100, 100, 200]

5. insert()

se usa para insertar un elemento en una posicion, primero la posicion luego
lo que se quiere añadir

transactions.insert(1, 700)
posición 1
valor 700

ejemplo:

[500, -100, 250] quedaria como [500, 700, -100, 250]

6. Eliminar elementos

elimina objetos con .remove y el objeto, por ejemplo transactions.remove(-100)

pop() elimina el ultimo objeto sin argumento, con argumento elimina el del indice transaction = transactions.pop(1)

7. len() 

se usa para saber cuandos elementos hay

ejemplo:
transactions = [500, -100, 250]

len(transactions)  # 3

8. Membership

es para saber si algo esta dentro, por ejemplo

500 in transactions o 999 not in transactions

devuelve booleano

9. Slicing

sirve para obtener partes de una lista

por ejemplo:
numbers = [10, 20, 30, 40, 50]
numbers[1:4]
da como resultado [20, 30, 40]

otros usos
numbers[:3]
[10, 20, 30]

numbers[2:]
[30, 40, 50]

numbers[-2:]
[40, 50]

tambien se usa numbers[start:stop:step]

ejemplo:
numbers[::2]
[10, 30, 50]

y eso numbers[::-1] da la lista en orden inverso

10. Ordenar listas

sort() modifica la lista existente pero ordered = sorted(numbers)
crea una nueva lista ordenada

numbers = [3, 1, 2]

ordered = sorted(numbers)

queda

numbers → [3, 1, 2]
ordered → [1, 2, 3]

11. Listas anidadas

una lista puede contener otras listas 

ejemplo
accounts = [
    ["Savings", 1000],
    ["Checking", 500]
]

accounts[0] da como resultado ["Savings", 1000]

accounts[0][1] da 1000


