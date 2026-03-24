# Python Project: To-Do List (Command Line App)
# Build a simple to-do list app in the terminal that lets users add, view, and remove tasks.

# Create an Empty Task List 
# Define Menu Options
# includes :
# - Lists  
# - Loops  
# - Functions  
# - User input handling
# - Simple CRUD operations

tasks = []

def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    #  Add Task
    if choice == '1':
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            print(" Task added!")
        else:
            print(" Task cannot be empty.")

    #  View Tasks
    elif choice == '2':
        if not tasks:
            print(" No tasks yet.")
        else:
            print(" Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Remove Task
    elif choice == '3':
        if not tasks:
            print(" No tasks to remove.")
            continue

        try:
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f" Removed: {removed}")
            else:
                print(" Invalid number.")
        except ValueError:
            print(" Please enter a valid number.")

    # Exit
    elif choice == '4':
        print(" Exiting To-Do App.")
        break

    else:
        print(" Invalid choice.")