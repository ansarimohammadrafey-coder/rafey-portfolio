# To-Do List Project
# Created by Rafey

tasks = []


def add_task():
    task = input("Enter your task: ")

    tasks.append(task)

    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)

            print(f"Deleted: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice. Try again.")


main()