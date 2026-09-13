# ==========================================
# 🐍 SIMPLE PYTHON ALL-IN-ONE LEARNING APP
# Everything is written inside this SINGLE file!
# ==========================================

# We store our tasks in a list
tasks = []

def show_tasks():
    print("\n--- YOUR TO-DO LIST ---")
    if len(tasks) == 0:
        print("No tasks added yet!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("-----------------------\n")

def add_task():
    new_task = input("Enter a new task: ").strip()
    if new_task != "":
        tasks.append(new_task)
        print(f"✅ Added: '{new_task}'\n")
    else:
        print("⚠️ Task cannot be empty!\n")

def remove_task():
    show_tasks()
    if len(tasks) > 0:
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"🗑️ Removed: '{removed}'\n")
            else:
                print("⚠️ Invalid task number!\n")
        except ValueError:
            print("⚠️ Please enter a valid number!\n")

# Main menu loop
while True:
    print("=== MY PYTHON APP ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter option (1-4): ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("\n👋 Goodbye! Happy learning Python!")
        break
    else:
        print("\n⚠️ Invalid option! Please choose 1, 2, 3, or 4.\n")
