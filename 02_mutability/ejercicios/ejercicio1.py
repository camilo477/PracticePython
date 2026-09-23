"""
Crea una lista original que contenga un diccionario 
con una cuenta y saldo. Haz una copia con .copy(). 
Modifica el saldo desde la copia y demuestra con print() y is que:

las listas son objetos distintos;
el diccionario interno sigue siendo el mismo objeto;
el cambio del saldo aparece en ambas.
"""

original = [
    {
        "amount":200,
        "name":"camilo"
    }
]

copia = original.copy()

copia[0]["amount"] = 150

print(original is copia) #da false porque no son el mismo objeto

print(original[0] is copia[0]) #da true porque el diccionario si es el mismo

print("original: ",original[0]["amount"])
print("copia: ",copia[0]["amount"])

