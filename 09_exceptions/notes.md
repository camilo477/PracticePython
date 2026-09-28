09 — Exceptions

Una excepción representa una situación anormal que interrumpe el flujo normal del programa.

1. try / except y excepciones específicas

amount = int(input("Amount: "))
si se introduce un string por ejemplo, dara ValueError

se maneja asi:

try:
    amount = int("hello")
except ValueError:
    print("Invalid amount")

except solo ocurre si dentro del try ocurre una excepcion

excepciones comunes:

ValueError
→ tipo correcto, valor inválido

TypeError
→ operación con tipo incorrecto

KeyError
→ clave inexistente en dict

IndexError
→ índice inexistente

ZeroDivisionError
→ división entre cero

FileNotFoundError
→ archivo inexistente

Capturar varias excepciones

try:
    value = transactions[index]
    amount = int(value)

except IndexError:
    print("Invalid index")

except ValueError:
    print("Invalid amount")

o agrupandolas:

try:
    ...
except (IndexError, ValueError):
    print("Invalid data")

2. Obtener información de la excepción

se guardan objetos en la excepcion

try:
    amount = int("hello")
except ValueError as error:
    print(error)

error contiene la excepción concreta que ocurrió.

3. else y finally

try
except
else
finally

else se ejecuta solamente si el try terminó sin excepción.

finally
se ejecuta ocurra o no una excepción.

try:
    amount = int(value)
except ValueError:
    print("Invalid amount")
finally:
    print("Operation finished")

4. raise: lanzar tus propias excepciones

No solamente capturamos excepciones. También podemos decidir que una situación inválida debe producir una.

ejemplo:
def deposit(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    return amount

5. Propagación de excepciones

Una función no tiene que capturar todas las excepciones que puedan ocurrir dentro de ella.

Muchas veces es mejor permitir que una capa superior decida qué hacer.

6. El try debe ser lo más estrecho razonablemente posible

solo meter lo que se quiere controlar

