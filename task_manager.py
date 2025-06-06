import argparse
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List

DATA_FILE = Path('tasks.json')

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False


def load_tasks() -> List[Task]:
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return [Task(**t) for t in data]
    return []


def save_tasks(tasks: List[Task]):
    with open(DATA_FILE, 'w') as f:
        json.dump([asdict(t) for t in tasks], f, indent=2)


def add_task(description: str):
    tasks = load_tasks()
    next_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id=next_id, description=description)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task {task.id}: {task.description}")


def list_tasks(show_all: bool = True):
    tasks = load_tasks()
    for task in tasks:
        status = '✓' if task.completed else ' '
        print(f"[{status}] {task.id}: {task.description}")


def complete_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            save_tasks(tasks)
            print(f"Marked task {task_id} as completed")
            return
    print(f"Task {task_id} not found")


def delete_task(task_id: int):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t.id != task_id]
    if len(new_tasks) != len(tasks):
        save_tasks(new_tasks)
        print(f"Deleted task {task_id}")
    else:
        print(f"Task {task_id} not found")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple Daily Task Manager")
    sub = parser.add_subparsers(dest='command', required=True)

    add = sub.add_parser('add', help='Add a new task')
    add.add_argument('description', help='Task description')

    sub.add_parser('list', help='List all tasks')

    complete = sub.add_parser('complete', help='Mark task as completed')
    complete.add_argument('id', type=int, help='Task ID')

    delete = sub.add_parser('delete', help='Delete a task')
    delete.add_argument('id', type=int, help='Task ID')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'complete':
        complete_task(args.id)
    elif args.command == 'delete':
        delete_task(args.id)


if __name__ == '__main__':
    main()
