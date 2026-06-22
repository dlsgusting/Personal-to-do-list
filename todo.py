import sys

running = True

task1 = {"title": "Wash the dishes", "completed": True}
task2 = {"title": "Do my homework", "completed": False}
task_list = [task1, task2]



def choose_action():
    print("\n")
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
    if not task_list:
        print("You don't have any tasks")
        return

    for i, task in enumerate(task_list):
        if task["completed"] == False:
            print(f"{i + 1}. [ ] {task["title"]}")
        else:
            print(f"{i + 1}. [x] {task["title"]}")

def add_task():
    view_task()
    print("Enter the task name or type cancel to go back")
    name = input()
    if name.lower() == "cancel":
        return
    else: 
        new_dict = {"title" : name, "completed" : False}
        task_list.append(new_dict)

def mark_task():
    view_task()
    print("Enter the number of the task you wish to mark or type -1 to exit")
    while True:
        try:
            task_num = int(input())
            task_num2 = task_num - 1
            if task_num == -1:
                return
            elif task_num2 < len(task_list):
                break
            else:
                print("Not a valid task number")

        except ValueError:
            print("Please enter a valid task number.")

    valid_mark = ["completed", "incomplete"]
    print(f"Do you wish to mark task {task_num2} as complete or incomplete? Enter completed/incomplete")
    mark_status = input().lower()

    while mark_status not in valid_mark:
        print("Not a valid answer, enter again.")
        mark_status = input().lower()

    if mark_status == "completed":
        num = task_list[task_num2]
        num["completed"] = True
    else:
        num = task_list[task_num2]
        num["completed"] = False

def delete_task():
    view_task()
    print("Which task would you like to delete or type -1 to exit")
    while True:
        try:
            task_num = int(input())
            task_num2 = task_num - 1
            if task_num == -1:
                return
            elif task_num2 < len(task_list):
                break
            else:
                print("Not a valid task number")

        except ValueError:
            print("Please enter a valid task number.")
    del task_list[task_num]

def exit_menu():
    sys.exit()

actions = {
    1: view_task,
    2: add_task,
    3: mark_task,
    4: delete_task,
    5: exit_menu
}

while running:
    selected = choose_action()
    actions[selected]()

    # running = False


