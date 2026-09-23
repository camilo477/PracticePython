import copy


account = {
    "owner": "Camilo",
    "transactions": [500, -100]
}

same_account = account #aqui se apunta al mismo diccionario
shallow_account = account.copy() #aqui se copia el diccionario
deep_account = copy.deepcopy(account) #aqui se copia el diccionario con deepcopy

same_account["transactions"].append(-50)
print("same account", same_account)
shallow_account["transactions"].append(200)
print("shallow_account", shallow_account)
shallow_account["owner"] = "camila"
print(deep_account)

print(same_account is shallow_account) #false
print(same_account is deep_account) #false
print(shallow_account is deep_account) #false
#son diferentes objetos

print(same_account["owner"] is shallow_account["owner"]) #true, si son el mismo objeto
print(same_account["owner"] is deep_account["owner"]) #true, aqui
#hay trampa y es porque los string son inmutables, por eso si
#cambia algun valor en same o shallowpara deep no cambiara pero para los otros si

"""
dict A["owner"] ─────┐
dict B["owner"] ─────┼──→ "Camilo"
dict C["owner"] ─────┘

dict A["transactions"] ──┐
dict B["transactions"] ──┴──→ lista A

dict C["transactions"] ─────→ lista B
"""

#como los diccionarios de same_account y shallow_account apuntan 
#al mismo objeto al cambiar uno cambia el otro, pero no es el mismo
#diccionario
#deep_account si es una copia profunda por lo que no apunta al mismo objeto 
#su diccionario