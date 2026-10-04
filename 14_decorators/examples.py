from functools import wraps


def minimum_amount(minimum):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            amount = kwargs.get("amount")

            if amount is not None and amount < minimum:
                raise ValueError(
                    f"Amount must be at least {minimum}"
                )

            return function(*args, **kwargs)

        return wrapper

    return decorator



def log_method(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished {function.__name__}")

        return result

    return wrapper


class Account:
    def __init__(self, balance):
        self.balance = balance

    @log_method
    def deposit(self, amount):
        self.balance += amount
        return self.balance




def log_execution(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Starting {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished {function.__name__}")

        return result

    return wrapper


@log_execution
def deposit(balance, amount):
    return balance + amount


result = deposit(1000, 500)

print(result)