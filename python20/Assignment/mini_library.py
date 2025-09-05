import argparse
import json
import os

FILE = "library.json"

def load_library():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(FILE, "w") as f:
        json.dump(library, f, indent=4)

def add_book(title, author):
    library = load_library()
    library.append({"title": title, "author": author})
    save_library(library)
    print(f'Added "{title}" by {author}')

def list_books():
    library = load_library()
    if not library:
        print("Library is empty")
    else:
        for i, book in enumerate(library, 1):
            print(f'{i}. {book["title"]} by {book["author"]}')

def remove_book(index):
    library = load_library()
    if 0 <= index < len(library):
        removed = library.pop(index)
        save_library(library)
        print(f'Removed "{removed["title"]}"')
    else:
        print("Invalid book index")

def main():
    parser = argparse.ArgumentParser(description="Mini Library CLI")
    parser.add_argument("action", choices=["add", "list", "remove"])
    parser.add_argument("args", nargs="*", help="Arguments for action")

    parsed = parser.parse_args()

    if parsed.action == "add":
        if len(parsed.args) < 2:
            print("Usage: add <title> <author>")
        else:
            title = parsed.args[0]
            author = " ".join(parsed.args[1:])
            add_book(title, author)

    elif parsed.action == "list":
        list_books()

    elif parsed.action == "remove":
        if not parsed.args:
            print("Usage: remove <index>")
        else:
            try:
                index = int(parsed.args[0]) - 1
                remove_book(index)
            except ValueError:
                print("Index must be a number")

if __name__ == "__main__":
    main()
