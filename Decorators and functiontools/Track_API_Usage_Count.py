import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def count_calls(func):
    func.calls = 0
    @wraps(func)
    def wrapper(*a, **k):
        func.calls += 1
        logging.info(f"{func.__name__} called {func.calls} times")
        return func(*a, **k)
    return wrapper

@count_calls
def get_user(user_id):
    return f"Fetched user {user_id}"

print(get_user(101))
print(get_user(102))
