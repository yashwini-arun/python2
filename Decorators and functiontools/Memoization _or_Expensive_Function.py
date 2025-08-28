import logging, time
from functools import lru_cache, wraps

logging.basicConfig(level=logging.INFO)

def log(func):
    @wraps(func)
    def wrapper(*a, **k):
        logging.info(f"Running {func.__name__}")
        return func(*a, **k)
    return wrapper

@log
@lru_cache(maxsize=5)
def fibonacci(n):
    time.sleep(0.5)
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
