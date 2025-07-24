import json
import os


TASK_FILE = "tasks.json"



def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []



def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)



def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")



def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added!")



def complete_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 0 < choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



def delete_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 0 < choice <= len(tasks):
            tasks.pop(choice - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
