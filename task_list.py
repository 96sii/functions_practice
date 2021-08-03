

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]




def is_task_complete(list, input):
    completed_tasks =[]
    for task in list:
        if task["completed"] == input:
            completed_tasks.append(task["description"])
    return completed_tasks

# #TASK 1: Print a list of uncompleted list
# for task in list:
#     if task["completed"] == False:
#         print("Not completed: " + task["description"])



# #TASK 2: Print a list of completed list
# for task in list:
#     if task["completed"] == True:
#         print("Completed: " + task["description"])


# #TASK 3: Print a list of all task descriptions
# for task in list:
#     print(task["description"])
def task_description(list):
    task_descriptions = []
    for task in list:
        task_descriptions.append(task["description"])
    return task_descriptions

# #TASK 4: Print a list of where time_taken is at least a given time
# for task in list:
#     if task["time_taken"] > 20:
#         print(task["description"])
def time_taken(list, number):
    time_more_than_20 = []
    for task in list:
        if task["time_taken"] >= number:
            time_more_than_20.append(task["description"])
    return time_more_than_20

#TASK 5: Print any task with a given description
def print_task(list, description):
    for task in list:
        if task["description"].lower() == description.lower():
            return (task)
    return ("This task isn't on the list.")

def mark_as_complete(list, description):
    for task in list:
        if task["description"].lower() == description.lower():
            task["completed"] = True
            return "Task completed"

def add_task(list, description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken
    list.append(task)
    

def print_menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

while(True):
    print_menu()
    user_select = input("Please enter a number ")
    if user_select.lower() == "q":
        break
    elif user_select == '1':
        print(task_description(tasks))
    elif user_select == '2':
        print(is_task_complete(tasks, False))
    elif user_select == '3':
        print(is_task_complete(tasks,True))
    elif user_select == '4':
        task_complete_user = input("Please enter which task was completed")
        print(mark_as_complete(tasks, task_complete_user))
    elif user_select == '5':
        user_task_time = input("Please enter a time ")
        print(time_taken(tasks, int(user_task_time)))
    elif user_select == '6':
        user_description = input("Please enter the task description ")
        print(print_task(tasks, user_description))
    elif user_select == '7':
        user_append_description = input("Please enter the task ")
        user_append_time = input("How long does this task take ")
        add_task(tasks,user_append_description,user_append_time)
    
    



