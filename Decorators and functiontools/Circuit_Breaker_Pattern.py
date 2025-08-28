import logging, random
from functools import wraps

logging.basicConfig(level=logging.INFO)

def circuit_breaker(max_failures=2):
    def decorator(func):
        failures = {"count": 0}
        @wraps(func)
        def wrapper(*a, **k):
            if failures["count"] >= max_failures:
                logging.error("Circuit open - blocking calls")
                return None
            try:
                return func(*a, **k)
            except Exception as e:
                failures["count"] += 1
                logging.warning(f"Failure {failures['count']}: {e}")
        return wrapper
    return decorator

@circuit_breaker(max_failures=2)
def unstable_service():
    if random.randint(0, 1):
        raise ValueError("Service crash")
    return "Service OK"

print(unstable_service())
print(unstable_service())
print(unstable_service())
