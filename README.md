# Daily Task Manager

This is a simple command-line application for managing daily tasks.

## Requirements

* Python 3.8 or newer

## Usage

Add a task:

```bash
python task_manager.py add "Buy groceries"
```

List tasks:

```bash
python task_manager.py list
```

Mark a task as completed:

```bash
python task_manager.py complete 1
```

Delete a task:

```bash
python task_manager.py delete 1
```

Tasks are stored in `tasks.json` in the current directory.
