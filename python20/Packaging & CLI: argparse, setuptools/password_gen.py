import random
import string
import sys

def generate_password(length: int) -> str:
    """Generate a secure random password with given length."""
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Characters to use
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure password has at least 1 lowercase, 1 uppercase, 1 digit, 1 symbol
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill remaining length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 password_gen.py <length>")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
        pwd = generate_password(length)
        print(f"Generated Password: {pwd}")
    except ValueError:
        print("Please enter a valid number for length.")
