import time
from app import BankAccount, flatten, timed

# -------- BankAccount Tests --------
def test_initial_balance():
    acc = BankAccount("Alice", 100)
    assert acc.get_balance() == 100

def test_negative_initial_balance():
    try:
        BankAccount("Bob", -50)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_deposit_valid():
    acc = BankAccount("Charlie", 200)
    assert acc.deposit(100) == 300

def test_deposit_invalid():
    acc = BankAccount("Dana", 100)
    try:
        acc.deposit(-20)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_withdraw_valid():
    acc = BankAccount("Eve", 500)
    assert acc.withdraw(200) == 300

def test_withdraw_insufficient():
    acc = BankAccount("Frank", 100)
    try:
        acc.withdraw(200)
        assert False, "Expected ValueError"
    except ValueError:
        pass

# -------- Flatten Tests --------
def test_flatten_simple():
    assert list(flatten([1, 2, 3])) == [1, 2, 3]

def test_flatten_nested():
    assert list(flatten([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]

def test_flatten_empty():
    assert list(flatten([])) == []

def test_flatten_with_strings():
    assert list(flatten(["a", ["b", ["c"]]])) == ["a", "b", "c"]

# -------- Decorator Tests --------
@timed
def slow_function():
    time.sleep(0.05)
    return "done"

def test_timed_decorator_runs():
    result = slow_function()
    assert result == "done"
    assert slow_function.last_runtime >= 0.05  # should take at least 0.05s

if __name__ == "__main__":
    test_initial_balance()
    test_negative_initial_balance()
    test_deposit_valid()
    test_deposit_invalid()
    test_withdraw_valid()
    test_withdraw_insufficient()
    test_flatten_simple()
    test_flatten_nested()
    test_flatten_empty()
    test_flatten_with_strings()
    test_timed_decorator_runs()
    print("All tests passed.")