hay que tener cuidado entre
shadow copy copy() y deepcopy()

shadow copy hace copia de por ejemplo la lista
pero no de los elementos dentro, es decir estos elementos 
van a seguir apuntando al elemento original

el deepcopy si hace copia de ambos




deepcopy tiene algo, Los objetos inmutables, como los str, pueden seguir siendo compartidos incluso después de hacer un deepcopy().

los str al ser inmutables puede pasar que un diccionario 
tenga 2 variables, crear una deepcopy
y al hacer dict_original["ejemplo"] is deepcopy["ejemplo"]
de true, pero al momento de cambiar de dict_original este ejemplo en
deepcopy no cambie

Esto ocurre porque no estamos modificando el string "Camilo" —los strings son inmutables—, sino reasignando la clave "owner" de deep_copy para que referencie otro objeto.