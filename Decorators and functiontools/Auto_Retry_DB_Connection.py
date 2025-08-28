import logging, random
from functools import wraps

logging.basicConfig(level=logging.INFO)

def db_retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except ConnectionError:
                logging.warning(f"DB connection failed. Retry {i+1}")
        logging.error("All retries failed")
    return wrapper

@db_retry
def connect_db():
    if random.randint(0, 1):
        raise ConnectionError("DB not reachable")
    return "DB connected successfully"

print(connect_db())
