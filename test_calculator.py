# test_calculator_pytest.py

from calculator import sum_numbers

def test_sum_numbers():
    assert sum_numbers(5, 7) == 12
    assert sum_numbers(-1, 1) == 0
    assert sum_numbers(-1, -1) == -2
