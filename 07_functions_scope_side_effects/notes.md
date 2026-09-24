1. ¿Qué problema resuelve una función?
Una función permite agrupar lógica bajo un nombre para:
- evitar repetir código;
- dividir problemas grandes;
- reutilizar comportamiento;
- probar partes del programa por separado;
- expresar mejor la intención del código.

balance = 1000
amount = 200

if amount > 0:
    balance += amount

print(balance)

aqui deposatiraiamos veinte veces haceidno lo mismo 20 veces, entonces se usa una funcion

def deposit(balance, amount):
    return balance + amount

2. Definir una función

sintaxis 

def greet():
    print("Hello")

pare ejecutarla es con greet()

3. Parámetros y argumentos

se le pueden pasar parametros y argumentos a una funcion

parámetro
→ nombre definido en la función

argumento
→ valor que envío al llamar la función

def deposit(amount):
    print(amount)

deposit(500)

4. Argumentos posicionales

se pasan por posicion

def transaction(transaction_type, amount):
    print(transaction_type, amount)

los recibe en orden transaction("income", 500)

5. Keyword arguments

se le puede especificar el nombre y el orden deja de importar

transaction(
    amount=500,
    transaction_type="income"
)

6. Mezclar positional y keyword

regla, posicionales primero keyword despues, por eso esto no sirve

transaction(transaction_type="income", 500)

porque primero ve la posicion

7. Parámetros por defecto

def create_transaction(amount, description=None):
    print(amount, description)

create_transaction(500)

usara
amount = 500
description = None

si se le pone no usara el predeterminado create_transaction(500, "Salary")

IMPORTANTE Un parámetro obligatorio debe ir antes de uno con valor por defecto

incorrecto:
def transaction(description=None, amount):
    ...

8. return

return devuelve un resultado al lugar desde donde llamaste la función.

9. return termina la función

si un returne termina en fasle termina la funcion inmediatamente

10. Función sin return

def greet():
    print("Hello")

result = greet()

da resultado None

11. print() vs return

print()
→ mostrar información

return
→ entregar un resultado al código que llamó la función

12. Devolver múltiples valores

def calculate_summary():
    income = 2000
    expenses = 800

    return income, expenses

result = calculate_summary()
print(result)

da (2000, 800) una tuple

13. Scope

Desde qué partes del programa puedo acceder a un nombre?

def calculate():
    total = 500
    print(total)

total existe solo dentro de la funcion

currency = "COP"

def show_currency():
    print(currency)

existe global se puede usar dentro de las funciones

LEGB

L → Local
E → Enclosing
G → Global
B → Built-in

asi busca python nombres

esto no modifica el balance global crea uno local

balance = 1000

def deposit():
    balance = 1500

deposit()

print(balance)

muestra 1000

esto si modifica el global

balance = 1000

def deposit():
    global balance
    balance = 1500


14. Pasar objetos a funciones

def show(data):
    print(data)

numbers = [1, 2]

show(numbers)

numbers ──┐
          ├──→ [1, 2]
data ─────┘

data referencia el mismo objeto que numbers

por eso si se hace append data.append(3) dentro de la funcion numbers tambien referencia el objeto y queda [1,2,3]

reasignar no es lo mismo

def replace_transactions(transactions):
    transactions = [500]

aqui la variable transactions ya referencia otro objeto

15. Side effects

Un side effect ocurre cuando una función modifica algo fuera de su resultado de retorno.

esto es un side effect
def add_transaction(transactions):
    transactions.append(500)

file.write(...) esto tambien

16. Composición de funciones

Una función puede usar el resultado de otra.

ejemplo:

def calculate_income(transactions):
    return sum(transactions)

def calculate_tax(income):
    return income * 0.19

income = calculate_income([1000, 500])
tax = calculate_tax(income)

17. Responsabilidad única

Una función debería tener una responsabilidad clara.

18. Guard clauses

en vez de 

def withdraw(balance, amount):
    if amount > 0:
        if amount <= balance:
            return balance - amount

se usa 

def withdraw(balance, amount):
    if amount <= 0:
        return balance

    if amount > balance:
        return balance

    return balance - amount

asi los casos invalidos salen pronto

19. None como sentinel

Aquí None significa:
no me enviaron una lista.

Por eso comprobamos:

if transactions is None:

y no:

if not transactions: