# Ahora quiero que reemplaces varios tests válidos
#  repetitivos por un solo test parametrizado.
# Casos:
# balance | amount | expected
# 1000    | 200    | 800
# 500     | 100    | 400
# 300     | 300    | 0
# 2000    | 500    | 1500

# Debes usar:
# @pytest.mark.parametrize(...)


# y crear un único test:
# def test_withdraw_valid_cases(...):    ...


# Dentro solo debes:
# 1. llamar withdraw(balance, amount);
# 2. guardar el resultado;
# 3. comprobarlo con assert.
# Los tests de errores:
# withdraw(1000, -100)withdraw(1000, 1500)


# déjalos separados por ahora.

def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount