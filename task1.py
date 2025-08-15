tasks = []

def show_menu():
    print("1 - Add Task")
    print("2 - View Tasks")
    print("3 - Update Task")
    print("4 - Delete Task")
    print("5 - Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({'task': task, 'done': False})

def view_tasks():
    for i, t in enumerate(tasks):
        status = 'Done' if t['done'] else 'Not Done'
        print(f"{i+1}. {t['task']} [{status}]")

def update_task():
    view_tasks()
    idx = int(input("Task number to update: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]['task'] = input("New task: ")
        done = input("Is it done? (y/n): ")
        tasks[idx]['done'] = True if done.lower() == 'y' else False

def delete_task():
    view_tasks()
    idx = int(input("Task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)

while True:
    show_menu()
    choice = input("Choose: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
