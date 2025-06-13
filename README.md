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

---

## Meta Ad Creative Generator

This script generates simple Meta ad creatives from a CSV file containing business details.

### Usage

Prepare a CSV file with the following headers:

```
business,product,description,audience,offer,cta
```

Run the generator:

```bash
python meta_ad_generator.py input.csv output.csv
```

The output CSV will contain all original columns plus a `creative` column with the generated ad text.
