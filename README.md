# 📝 Python Task Manager CLI

A lightweight, zero-dependency command-line Task Manager built using pure Python standard libraries.

## 🚀 Features

- **Zero Dependencies**: Uses standard Python libraries (`json`, `datetime`, `unittest`).
- **Data Persistence**: Tasks are saved automatically in `tasks.json`.
- **Task Management**: Add, view, filter, search, complete, and delete tasks.
- **Priority & Status Tracking**: Categorize tasks by `Low`, `Medium`, or `High` priority, and track status (`Pending` vs `Completed`).
- **Automated Testing**: Comprehensive unit test suite included.

## 📁 Project Structure

```
python/
├── main.py                     # Main CLI entry point
├── tasks.json                  # Data storage (auto-generated)
├── task_manager/
│   ├── __init__.py             # Package init
│   ├── models.py               # Task data class
│   ├── storage.py              # Storage & persistence manager
│   └── cli.py                  # Terminal UI & menu logic
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py    # Unit tests
└── README.md                   # Project documentation
```

## 🛠️ Usage

### Run the Application

```bash
python main.py
```

### Run Unit Tests

```bash
python -m unittest discover tests
```
