import time
import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def timed(func):
    """Decorator to log execution time of any function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {(end - start):.4f} seconds")
        return result
    return wrapper

# Example usage
@timed
def slow_function(n):
    """Simulates a slow task."""
    time.sleep(n)
    return f"Finished after {n} seconds"

print(slow_function(2))
print(slow_function(1))
