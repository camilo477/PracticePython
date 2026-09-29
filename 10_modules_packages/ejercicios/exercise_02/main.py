from finance import deposit, withdraw

try:
    print(deposit(1000, 500))
    print(withdraw(1000, 200))
    print(withdraw(1000, 1500))
except (TypeError, ValueError) as e:
    print(f"No se pudo hacer la transaccion {e}")