# file: json_pretty.py
import argparse, json

def pretty_print(file):
    with open(file) as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))

def main():
    parser = argparse.ArgumentParser(description="Pretty print JSON files")
    parser.add_argument("file", help="Path to JSON file")
    args = parser.parse_args()
    try:
        pretty_print(args.file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
