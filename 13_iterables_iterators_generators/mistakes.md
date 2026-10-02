Errores importantes
Confundir iterable con iterator
Una lista:
numbers = [1, 2, 3]


es iterable.
next(numbers)


da error:
TypeError

porque la lista no es el iterator.

Primero:
iterator = iter(numbers)next(iterator)

Esperar que un iterator se reinicie
iterator = iter(numbers)list(iterator)list(iterator)


la segunda vez estará vacío.
Usar generator si necesitas reutilizar resultados muchas veces
Si vas a hacer:
recorrer
indexar
volver a recorrer
calcular len

quizá necesitas una lista.
Convertir inmediatamente a list sin necesidad
generator = ...results = list(generator)


es válido, pero si haces eso siempre pierdes parte del beneficio del lazy evaluation.
Confundir yield con return
yield pausa.
return termina.
Meter yield accidentalmente en una función
En cuanto una función contiene un yield, Python la trata como generator function.
Ejemplo:
def example():    if False:        yield 1    return 10


Llamar:
example()


no devuelve directamente 10; devuelve un generator.
Esto puede sorprender si no sabes que existe yield dentro.

