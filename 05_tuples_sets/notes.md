1. — Tuples

Una tuple se parece a una lista, pero es inmutable.

account = ("Savings", 1200)

account[0]  # "Savings"
account[1]  # 1200

pero no se puede hacer account[1] = 1500 porque es inmutable

2. Desempaquetado

Una de las cosas más importantes de tuples:

transaction = ("income", 500)

transaction_type, amount = transaction

transaction_type  # "income"
amount             # 500

un tuple sigue siendo mutable en ciertas cosas, por ejemplo si tiene dentro una lista esta lista puede cambiar por ejemplo se le puede añadir cosas

data = ([100, 200], "income")

data[0] = [300]
# error

data[0].append(300) da ([100, 200, 300], "income")

05 — Sets

transaction_types = set()

Un set es una colección que tiene principalmente estas características:

no admite duplicados;
no se usa por posición;
es mutable;
es muy útil para membership y operaciones de conjuntos.

Ejemplo:

categories = {
    "food",
    "transport",
    "food",
    "rent"
}

esto da {"food", "transport", "rent"}

esto es util para eliminar duplicados, por ejemplo

categories = ["food", "food", "rent", "food"]

unique_categories = set(categories)

no se accede por indice ya que un set no tienen posicion

3. Agregar y eliminar

categories.add("health")

categories.remove("food")

existe categories.discard("food"), con remove si no existe da error, con discard no pasa nada

4. Membership

suele ser eficiente la comprobacion de algo dentro de un set

"food" in categories

5. Operaciones de conjuntos

january = {"food", "rent", "transport"}

february = {"food", "health", "transport"}

intersaccion = &

january & february da {"food", "transport"}

tambien sirve january.intersection(february)



Unión

january | february da {"food", "rent", "transport", "health"}

tambien january.union(february)


Diferencia

january - february da {"rent"}


Diferencia simétrica, Lo que está en uno u otro, pero no en ambos:

january ^ february da {"rent", "health"}