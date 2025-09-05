# file: todo_cli.py
import argparse, json, os

TODO_FILE = "todo.json"

def load_tasks():
    return json.load(open(TODO_FILE)) if os.path.exists(TODO_FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(TODO_FILE, "w"), indent=2)

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do App")
    parser.add_argument("action", choices=["add","list"])
    parser.add_argument("task", nargs="?", help="Task description")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.action == "add" and args.task:
        tasks.append(args.task); save_tasks(tasks); print("Task added!")
    else:
        print("Tasks:"); [print(f"{i+1}. {t}") for i, t in enumerate(tasks)]

if __name__ == "__main__":
    main()
