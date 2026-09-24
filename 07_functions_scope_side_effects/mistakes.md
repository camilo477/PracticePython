esto es para ejecutar una funcion greet(), pero esto es para referenciarla greet

Error muy común: olvidar return

def calculate_total(values):
    total = sum(values)

result = calculate_total([100, 200])

da None

porque falto el return total

1. Error 1 — olvidar llamar la función

result = calculate_total

no la ejecuta

2. Error 2 — olvidar return

def calculate_total(values):
    total = sum(values)

devuelve none

3. Error 3 — confundir print y return

def calculate():
    print(500)

no te permite usar 500 como resultado. solo lo imprime

4. Error 4 — orden de argumentos

transfer(500, "checking", "savings")

puede ser válido para Python y conceptualmente estar mal si confundiste posiciones.

5. Error 5 — modificar mutable sin darte cuenta

def process(items):
    items.append(...)

estás cambiando la lista original.

6. Error 6 — usar global para todo

global balance

puede hacer difícil seguir cómo cambia el estado.

7. Error 7 — mutable defaults

def function(items=[]):

esto crea un nuevo objeto

uando Python ejecuta la definición de la función, crea una lista nueva [].
El problema es que esa lista se crea una sola vez, no una vez por llamada