running = True

task1 = {"title": "example", "completed": False}
task2 = {"title": "example", "completed": False}
task_list = [task1, task2]



def choose_action():
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete or incomplete")
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

def add_task():
    print("Enter the task name")
    name = input()
    new_dict = {"title" : "name", "completed" : False}
    task_list.append(new_dict)

def mark_task():
    print("Enter the number of the task you wish to mark")
    while True:
        try:
            task_num = int(input()) - 1

            if task_num <= len(task_list):
                break
            else:
                print("Not a valid task number")

        except ValueError:
            print("Please enter a valid task number.")

    valid_mark = ["completed", "incomplete"]
    print(f"Do you wish to mark task {task_num} as complete or incomplete? Enter completed/incomplete")
    mark_status = input().lower()

    while mark_status not in valid_mark:
        print("Not a valid answer, enter again.")
        mark_status = input().lower()

    if mark_status == "completed":
        num = task_list[task_num]
        num["completed"] = True
    else:
        num = task_list[task_num]
        num["completed"] = False

actions = {
    1: view_task,
    2: add_task,
    3: mark_task
    # 4: delete_task,
    # 5: exit_menu
}

while running:
    selected = choose_action()
    actions[selected]()

    # running = False


