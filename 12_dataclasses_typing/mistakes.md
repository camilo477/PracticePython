Error común: creer que typing valida

Error común: mutable default en dataclass
No:
@dataclassclass Account:    transactions: list = []


Además, dataclasses modernas directamente suelen rechazar ciertos defaults mutables precisamente para evitar este bug.
Correcto:
transactions: list[Transaction] = field(    default_factory=list)

Error común: usar Any
Existe:
from typing import Any


y:
value: Any


significa prácticamente:
no estoy restringiendo/informando el tipo.

A veces es necesario, pero abusar de Any elimina gran parte del valor del typing.
En nuestro aprendizaje:
evita Any salvo que realmente tengas una razón.

Error común: dataclass para todo
Por ejemplo:
@dataclassclass Account:    ...


no está automáticamente mal.
Pero si necesitas:
- propiedad controlada;
- comportamiento importante;
- invariantes;
- cambios de estado muy regulados;
una clase tradicional puede ser más clara.
dataclass no significa “clase mejor”.
Significa:
clase orientada principalmente a almacenar datos con menos boilerplate.