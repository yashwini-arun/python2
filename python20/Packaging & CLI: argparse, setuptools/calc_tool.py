# file: calc_tool.py
import argparse

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Division by zero"

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("operation", choices=["add","sub","mul","div"], help="Operation")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    args = parser.parse_args()

    ops = {"add": add, "sub": sub, "mul": mul, "div": div}
    print(f"Result: {ops[args.operation](args.x, args.y)}")

if __name__ == "__main__":
    main()
