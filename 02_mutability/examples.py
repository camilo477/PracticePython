transactions = [100, 200]

backup = transactions

backup.append(300)

print(transactions)
print(backup)
print(transactions is backup)

"""
esto print(transactions) imprime [100, 200, 300] 
esto print(backup) imprime [100, 200, 300] 
esto print(transactions is backup) true porque ambos apuntan al mismo objeto
"""

accounts = [
    {"name": "Main", "balance": 1000}
]

backup = accounts.copy()

backup[0]["balance"] = 500

print(accounts)
print(backup)

print(accounts is backup)
print(accounts[0] is backup[0])

"""
se crean dos listas distintas, 
pero ambas contienen referencia al mismo diccionario interno.

el primer print print(accounts) 
va a imprimir [ {"name": "Main", "balance": 1000} ] 

el segundo print print(backup) imprime 
la copia [ {"name": "Main", "balance": 1000} ] 

el tercer print print(accounts is backup) dara 
false porque no estan apuntando al mismo objeto 

el cuarto print print(accounts[0] is backup[0]) 
si es el mismo objeto dara true

accounts ──→ lista A ──┐
                       ├──→ mismo dict {"name": "Main", "balance": 500}
backup ────→ lista B ──┘
"""