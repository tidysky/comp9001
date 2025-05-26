
tasks = []

def get_next_task_id(tasks):
    if tasks:
        return max(task["id"] for task in tasks) + 1
    else:
        return 1

def add_task(tasks, description):
    task_id = get_next_task_id(tasks)
    task = {"id": task_id, "description": description, "status": "pending"}
    tasks.append(task)
    print(f"Task '{description}' added with ID {task_id}")


def modify_task(tasks, task_id_input, new_description):
    for task in tasks:
        if task["id"] == task_id_input:
            task["description"] = new_description
            print(f"Task ID {task_id_input} modified.")
            return
    print("Task not found.")

def remove_task(tasks, task_id_input):
    new_tasks = [task for task in tasks if task["id"] != task_id_input]
    if len(new_tasks) != len(tasks):
        print(f"Task ID {task_id_input} removed.")
    else:
        print("Task not found.")
    return new_tasks

def mark_finished(tasks, task_id_input):
    for task in tasks:
        if task["id"] == task_id_input:
            task["status"] = "completed"
            print(f"Task ID {task_id_input} marked as completed.")
            return
    print("Task not found.")

def show_all(tasks):
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
    print()

def show_completed(tasks):
    print("\nCompleted Tasks:")
    found = False
    for task in tasks:
        if task["status"] == "completed":
            print(f"ID: {task['id']} | Description: {task['description']}")
            found = True
    if not found:
        print("No completed tasks yet.")
    print()

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Modify Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Show Completed Tasks")
        print("6. Show All Tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(tasks, description)

        elif choice == "2":
            task_id_input = int(input("Enter task ID to modify: "))
            new_description = input("Enter new description: ")
            modify_task(tasks, task_id_input, new_description)

        elif choice == "3":
            task_id_input = int(input("Enter task ID to remove: "))
            tasks = remove_task(tasks, task_id_input)

        elif choice == "4":
            task_id_input = int(input("Enter task ID to mark as completed: "))
            mark_finished(tasks, task_id_input)

        elif choice == "5":
            show_completed(tasks)

        elif choice == "6":
            show_all(tasks)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

