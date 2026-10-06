import pytest
from main import withdraw

@pytest.mark.parametrize(
    "balance, amount, expected",
    [
        (1000, 200, 800),
        (500, 100, 400),
        (300, 300, 0),
        (2000, 500, 1500),
    ],
)
def test_withdraw_valid_cases(balance, amount, expected):
    result = withdraw(balance, amount)

    assert result == expected