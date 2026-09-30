11 — Classes and Composition

Una clase nos permite definir un tipo de objeto que mantiene estado y tiene comportamiento relacionado con ese estado.

Con una clase podemos expresar:

Account
├── estado
│   ├── name
│   └── balance
│
└── comportamiento
    ├── deposit()
    └── withdraw()

1. Clase, instancia

una clase es la definicio del tipo

class Account:
    pass

una instancia e sun objeto creado a partir de la clase:

account1 = Account()
account2 = Account()

account1 is account2
# False

2. __init__

Normalmente queremos que cada instancia empiece con un estado:

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

account1 = Account("Savings", 1000)
account2 = Account("Checking", 500)

self representa la instancia sobre la que se trabaja

esto account1.deposit(500) es igual conceptualmente a Account.deposit(account1, 500)

3. Métodos, estado y responsabilidad

Una clase tiene sentido cuando hay comportamiento directamente relacionado con su estado.

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

Aquí la clase protege reglas relacionadas con una cuenta:

Account
↓
conoce su balance
↓
sabe cómo depositar
↓
sabe cómo retirar

4. Guard clauses

Los métodos suelen quedar más claros validando primero:

def withdraw(self, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > self.balance:
        raise ValueError("Insufficient funds")

    self.balance -= amount

en vez de 

def withdraw(self, amount):
    if amount > 0:
        if amount <= self.balance:
            self.balance -= amount

5. Atributos de instancia vs atributos de clase

Atributo de instancia

class Account:
    def __init__(self, name):
        self.name = name

Cada instancia puede tener un valor diferente:

account1.name → "Savings"
account2.name → "Checking"

Atributo de clase

Ese atributo pertenece a la clase y puede compartirse:

account1.currency
account2.currency
Account.currency

TRAMPA MUTALBE:

class Account:
    transactions = []

    def __init__(self, name):
        self.name = name

account1 = Account("Savings")
account2 = Account("Checking")

account1.transactions.append(500)

account2.transactions también puede ver 500.

Porque existe una sola lista en la clase.

se debe manejar asi:

class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = []

6. Composición: objetos que contienen otros objetos

Supón una clase:

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

Y una cuenta:

class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = []

Una cuenta puede contener objetos Transaction:

transaction = Transaction(500, "income")

account.transactions.append(transaction)

7. Referencias entre objetos

Cuando haces:

transaction = Transaction(500, "income")
account.transactions.append(transaction)

la lista guarda una referencia al objeto transaction.

conceptualmente

transaction ─────────────┐
                         ├──→ Transaction(...)
account.transactions[0] ─┘

8. Encapsulación, _balance, @property

self._balance

significa este atributo se considera interno; no deberías modificarlo directamente desde afuera salvo que tengas una razón.

ejemplo

class Account:
    def __init__(self, balance):
        self._balance = balance

tecnicamente se puede account._balance = -100000

Python no lo bloquea.
Pero el _ comunica:
usa la interfaz pública de la clase.

@property
Podemos permitir lectura controlada:

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

desde afuera print(account.balance)

9. Setter

Si quieres permitir asignación controlada:

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value

entonces

account.balance = 500

ejecuta el setter 

y
account.balance = -100

lanza ValueError.

10. __repr__ y __str__

transaction = Transaction(500, "income")

Sin personalización:

print(transaction)
da
<__main__.Transaction object at 0x...>

__str__ Busca una representación legible para humanos:

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type}: {self.amount}"

print(transaction)

da: income: 500

__repr__ Busca una representación útil para desarrolladores/debugging:

def __repr__(self):
    return (
        f"Transaction("
        f"amount={self.amount}, "
        f"transaction_type={self.transaction_type!r}"
        f")"
    )

puede mostrar 

Transaction(amount=500, transaction_type='income')

Una regla simplificada:
__str__
→ humano

__repr__
→ desarrollador/debugging

Una clase empieza a tener más sentido cuando existen:

estado persistente
+
comportamiento relacionado con ese estado
+
reglas/invariantes

Ejemplo:

Account
→ name
→ balance
→ transactions
→ deposit()
→ withdraw()