# Simple To-Do List Program for Beginners
# Learning Concepts: Lists, Loops, Functions, and User Input

# 1. We create an empty list to store our tasks
tasks = []

def show_tasks():
    """Function to display all tasks in the list."""
    if len(tasks) == 0:
        print("\nYour task list is empty!")
    else:
        print("\n--- YOUR TASKS ---")
        # enumerate gives us the item number starting from 1
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    print()

def add_task():
    """Function to add a new task."""
    new_task = input("Enter a new task: ")
    if new_task.strip() != "":
        tasks.append(new_task)
        print(f"'{new_task}' added successfully!\n")
    else:
        print("Task cannot be empty!\n")

def remove_task():
    """Function to remove a task by its number."""
    show_tasks()
    if len(tasks) > 0:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"'{removed}' has been removed!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

# Main program loop
while True:
    print("=== SIMPLE TO-DO APP ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("\nThank you for using the To-Do app! Goodbye!")
        break
    else:
        print("\nInvalid choice! Please choose 1, 2, 3, or 4.\n")
