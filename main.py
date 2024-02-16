import json

# Data file path
data_file = "todo_list.json"


def load_data():
    """Loads the to-do list data from the file."""
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    """Saves the to-do list data to the file."""
    with open(data_file, "w") as f:
        json.dump(data, f)


def list_tasks(data):
    """Prints the to-do list with task numbers and completion status."""
    for i, task in enumerate(data):
        print(f"{i+1}. {task['description']}" +
              (" (Completed)" if task['completed'] else ""))


def add_task(description):
    """Adds a new task to the list."""
    data.append({"description": description, "completed": False})
    save_data(data)


def delete_task(task_number):
    """Deletes a task from the list by its number."""
    if 1 <= task_number <= len(data):
        data.pop(task_number - 1)
        save_data(data)
    else:
        print("Invalid task number.")


def mark_completed(task_number):
    """Marks a task as completed by its number."""
    if 1 <= task_number <= len(data):
        data[task_number - 1]["completed"] = True
        save_data(data)
    else:
        print("Invalid task number.")


# Main program loop
data = load_data()
while True:
    print("\nTo-Do List:")
    list_tasks(data)
    print("\nCommands:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as completed")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        add_task(description)
    elif choice == "2":
        try:
            task_number = int(input("Enter task number: "))
            delete_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "3":
        try:
            task_number = int(input("Enter task number: "))
            mark_completed(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
