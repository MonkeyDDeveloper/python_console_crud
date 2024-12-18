import os,sys 
from email_validator import validate_email, EmailNotValidError

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.users import add_user, exists_email, login_user

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def valid_email(email):
    try:

        validate_email(email)

        check_email_in_db_response = exists_email(email)

        if check_email_in_db_response["success"] is False:
            raise Exception(f"There was an error consulting if the email exists in db {check_email_in_db_response['data']}")
    
        if check_email_in_db_response["data"] > 0:
            raise Exception("This email already exists, please use another one.")

        return True

    except EmailNotValidError:

        clear_terminal()

        print("The provided email is not valid.")

        return False

    except Exception as e:

        clear_terminal()

        print(f"There was an error processing the email. {str(e)}")

        return False

def no_auth_menu():

    available_options = set(["1", "2", "3"])
    
    menu = """\n
        1. Login
        2. Register
        3. Exit
    """
    option_selected = None
    
    while option_selected is None:
        
        print(menu)
        
        input_provided = input("What do you want to do?: ")
        
        if input_provided not in available_options:
            clear_terminal()
            print("\n Not valid option.")
            continue

        option_selected = input_provided

        break

    return option_selected

def auth_menu():

    available_options = set(["1", "2", "3", "4", "5"])
    
    menu = """\n
        1. See your tasks
        2. Add new task
        3. Update one task
        4. Delete a task
        5. Log out
    """
    option_selected = None
    
    while option_selected is None:
        
        print(menu)
        
        input_provided = input("What do you want to do?: ")
        
        if input_provided not in available_options:
            clear_terminal()
            print("\n Not valid option.")
            continue

        option_selected = input_provided

        break

    return option_selected

def login():
    
    clear_terminal()

    print("Enter 'back' to return to main menu")

    email = input("Enter your email: ")
    if email == "back":
        return "back"

    password = input("Enter your password: ")
    if password == "back":
        return "back"
    
    login_response = login_user(email, password)

    return login_response

def register():
    
    clear_terminal()

    print("Enter 'back' in any input to return to main menu \n")
    
    name = input("Enter your name: ")
    if name == "back":
        return "back"
    
    while len(name) <= 0:
        clear_terminal()
        name = input("Please provide a valid name: ")

    email = input("Enter an email please: ")
    if email == "back":
        return "back"

    is_valid_email = valid_email(email)

    while is_valid_email == False:

        email = input("Enter an email please: ")
        is_valid_email = valid_email(email)

    password = input("Enter your password please: ")
    if password == "back":
        return "back"

    add_user_response = add_user(name, email, password)

    return add_user_response

    

