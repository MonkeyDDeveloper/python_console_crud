import os
from prettytable import PrettyTable

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tasks(tasks):
    tasks_table = PrettyTable()
    tasks_table.field_names = "id,title,description,finished".split(",")
    for task in tasks:
        tasks_table.add_row(task)
    print(tasks_table)