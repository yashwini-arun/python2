# file: text_search.py
import argparse

def search_in_file(file, word):
    with open(file) as f:
        lines = f.readlines()
    return [i+1 for i,l in enumerate(lines) if word in l]

def main():
    parser = argparse.ArgumentParser(description="Search word in file")
    parser.add_argument("file", help="File path")
    parser.add_argument("word", help="Word to search")
    args = parser.parse_args()

    try:
        result = search_in_file(args.file, args.word)
        print(f"Found at lines: {result}" if result else "Not found")
    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    main()
