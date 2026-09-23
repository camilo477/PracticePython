ten en cuenta que cada parte del diccionario se puede recorrer como una lista con .items, es decir

ejemplo.items(): {
    "amount": 2550 
}

for i in ejemplo:
    i[0] -> es "amount"
    i[1] -> es 2550

en este caso i se vuelve una tupla

sin items recorre es las claves

ejemplo: {
    "amount": 2550 
}

for i in ejemplo:
    i -> es amount
    i[0] -> es a
    

normalmente se desempaqueta asi:

for key, value in example.items():
    print(key)
    print(value)

