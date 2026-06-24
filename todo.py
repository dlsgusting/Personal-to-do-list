import json
from pathlib import Path

running = True

task_list = []


file_path = Path(__file__).parent / "tasks.json"



def choose_action():
    print("\n")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete or incomplete")
    print("4. Delete task")
    print("5. Exit")

    valid = [1,2,3,4,5]

    while True:
        try:
            action = int(input())

            if action in valid:
                break
            else:
                print("Not a valid action, choose again")

        except ValueError:
            print("Please enter a valid action number.")

    return action

def view_task():
    if not task_list:
        print("You don't have any tasks")
        return

    for i, task in enumerate(task_list):
        if task["completed"] == False:
            print(f"{i + 1}. [ ] {task['title']}")
        else:
            print(f"{i + 1}. [x] {task['title']}")

def add_task():
    
    view_task()
    print("Enter the task name or type cancel to go back")
    name = input().strip()

    while not name:
        print("Task name cannot be empty, enter again or type cancel to go back")
        name = input().strip()

    if name.lower() == "cancel":
        return
    new_dict = {"title" : name, "completed" : False}
    task_list.append(new_dict)

def mark_task():
    if not task_list:
        print("You don't have any tasks")
        return
    view_task()
    print("Enter the number of the task you wish to mark or type -1 to exit")
    while True:
        try:
            task_num = int(input())
            task_num2 = task_num - 1
            if task_num == -1:
                return
            elif task_num2 < len(task_list) and task_num2 >= 0:
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
        num = task_list[task_num2]
        num["completed"] = True
    else:
        num = task_list[task_num2]
        num["completed"] = False

def delete_task():
    if not task_list:
        print("You don't have any tasks")
        return
    view_task()
    print("Which task would you like to delete or type -1 to exit")
    while True:
        try:
            task_num = int(input())
            task_num2 = task_num - 1
            if task_num == -1:
                return
            elif task_num2 < len(task_list) and task_num2 >= 0:
                break
            else:
                print("Not a valid task number")

        except ValueError:
            print("Please enter a valid task number.")
    del task_list[task_num2]

def exit_menu():
    global running
    running = False

actions = {
    1: view_task,
    2: add_task,
    3: mark_task,
    4: delete_task,
    5: exit_menu
}
    
try:
    with open(file_path, "r") as file:
        task_list = json.load(file)
except FileNotFoundError:
    task_list = []

    with open(file_path, "w") as file:
        json.dump(task_list, file, indent=4)

while running:

    selected = choose_action()
    actions[selected]()

    with open(file_path, "w") as file:
        json.dump(task_list, file, indent=4)
