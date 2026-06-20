running = True

task1 = {"title": "example", "completed": False}
task2 = {"title": "example", "completed": False}
task_list = [task1, task2]

def view():
    for task in task_list:
        print(task)
        print("\n")

while running:
    view()
    running = False


