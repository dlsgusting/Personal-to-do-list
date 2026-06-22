running = True

task1 = {"title": "example", "completed": False}
task2 = {"title": "example", "completed": False}
task_list = [task1, task2]



def choose_action():
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    valid = [1,2,3,4,5]
    action = int(input())
    while action not in valid:
        print("Not a valid action, choose again")
        action = int(input())
    return action

def view_task():
    for task in task_list:
        print(task)
        print("\n")

actions = {
    1: view_task
    # 2: add_task,
    # 3: mark_task,
    # 4: delete_task,
    # 5: exit_menu
}

while running:
    selected = choose_action()
    actions[selected]()

    running = False


