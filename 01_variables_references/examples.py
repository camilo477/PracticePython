balance = 1000
available = balance

balance = 750

print(balance)
print(available)

print(balance == available)
print(balance is available)

"""
- el primer print da 750 porque balance cambio a 750

- el segundo da 1000 porque available apunto a 1000 y no cambio

- el tercero va a dar false porque balance ahora es 
750 y available 1000

- el cuarto false porque balance ya no referencia 
el mismo objeto que available
"""

a = "python"
b = a
a = "django"

print(a)
print(b)

"""
-el print(a) va a ser "django" porque cambio su
referencia al objeto "django"

-el print(b) va a ser "python" porque referencia el mismo
objeto que a antes que este cambiara que es "python"
"""
