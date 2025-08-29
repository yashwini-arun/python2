import time
from functools import wraps


# ---------------- BankAccount ----------------
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


# ---------------- Flatten ----------------
def flatten(nested):
    """
    Flatten a nested list into a single list.
    Example: [1, [2, [3, 4]], 5] -> [1, 2, 3, 4, 5]
    """
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


# ---------------- Timed Decorator ----------------
def timed(func):
    """Decorator to measure execution time of a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        wrapper.last_runtime = end - start
        return result
    return wrapper
