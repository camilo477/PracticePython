"""
Ejercicio — Variables y referencias

Crea un programa que haga lo siguiente:

Crea una variable original_balance con valor 1200.
Crea una variable copied_balance que referencie el mismo objeto que original_balance.
Reasigna original_balance a 900.
Imprime ambas variables.
Comprueba con == si tienen el mismo valor.
Comprueba con is si referencian el mismo objeto.
Después crea una variable third_balance que referencie el mismo objeto que copied_balance.
Imprime:
third_balance
third_balance == copied_balance
third_balance is copied_balance
"""

original_balance = 1200
copied_balance = original_balance

original_balance = 900

print("original_balance", original_balance)
print("copied_balance", copied_balance)

print("original_balance == copied_balance", original_balance == copied_balance)
print("original_balance is copied_balance", original_balance is copied_balance)

third_balance = copied_balance

print("third_balance", third_balance)

print("third_balance == copied_balance", third_balance == copied_balance)
print("third_balance is copied_balance", third_balance is copied_balance)