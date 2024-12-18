import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.tasks import list_task
from utils.index import print_tasks

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_new_task_menu():

    clear_terminal()

    print("Enter 'back' in any input to return to main menu \n")
    
    task_title = input("Enter the task title: ")
    if task_title == "back":
        return "back"
    
    while len(task_title) <= 0:
        clear_terminal()
        task_title = input("Please provide a valid task title: ")

    task_description = input("Enter a task description please: ")
    if task_description == "back":
        return "back"

    task_finished = input("Is this task finished? (Empty and n/N is No, any other will be Yes): ")
    if task_finished == "back":
        return "back"
    
    task_finished = False if task_finished == 'n' or task_finished == 'N' else len(task_finished) > 0
    
    return {
        'task_title': task_title, 
        'task_description': task_description, 
        'task_finished': task_finished
    }

def select_one_task_menu(user_id = None):

    clear_terminal()

    print("Enter 'back' in any input to return to main menu \n")

    if user_id is not None:
        list_task_respones = list_task(user_id)
        if list_task_respones['success']:
            print_tasks(list_task_respones['data'])
    
    task_id = input("Enter the id of the task you wanna select: ")
    if task_id == "back":
        return "back"
    
    while len(task_id) <= 0:
        clear_terminal()
        task_id = input("Please provide a valid task id: ")

    return task_id

def update_task_menu(current_task):

    clear_terminal()

    print("Enter 'back' in any input to return to main menu \n")

    print(f"""
        Current task:
          Title: {current_task['title']}
          Description: {current_task['description']}
          Finished: {current_task['finished']}
    \n""")
    
    task_title = input("Enter the new task title (empty = no modification): ")
    if task_title == "back":
        return "back"
    
    task_title = current_task["title"] if len(task_title.strip()) == 0 else task_title
    
    task_description = input("Enter a task description please (empty = no modification): ")
    if task_description == "back":
        return "back"
    
    task_description = current_task["description"] if len(task_description.strip()) == 0 else task_description

    task_finished = input("Is this task finished? (empty = no modification, n/N = no, any other will be true): ")
    if task_finished == "back":
        return "back"
    
    task_finished = current_task["finished"] if len(task_finished.strip()) == 0 else (task_finished != "n" and task_finished != "N")
    
    return {
        'task_title': task_title, 
        'task_description': task_description, 
        'task_finished': task_finished
    }
