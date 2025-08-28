import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") == role:
                logging.info(f"Access granted to {user['name']}")
                return func(user, *args, **kwargs)
            logging.error("Access denied!")
        return wrapper
    return decorator

@require_role("admin")
def delete_record(user, record_id):
    return f"{user['name']} deleted record {record_id}"

print(delete_record({"name": "Alice", "role": "admin"}, 101))
print(delete_record({"name": "Bob", "role": "guest"}, 102))
