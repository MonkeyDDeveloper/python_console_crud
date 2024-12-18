from database.index import conn, cur
from authentication.index import no_auth_menu, register, login, auth_menu
from menus.index import add_new_task_menu, select_one_task_menu, update_task_menu
from database.tasks import list_task, add_task, select_one_task, update_task, delete_task
from utils.index import clear_terminal, print_tasks

clear_terminal()

keep_going = True

no_auth_actions = {
    "LOGIN": "1",
    "REGISTER": "2",
    "EXIT": "3"
}
no_auth_action = ""

auth_actions = {
    "LIST": "1",
    "CREATE": "2",
    "UPDATE": "3",
    "DELETE": "4",
    "OUT": "5"
}
auth_action = ""

logged_user = None

if conn is not None and cur is not None:

    if __name__ == "__main__":

        while keep_going:

            while logged_user is None:
            
                no_auth_action = no_auth_menu()

                if no_auth_action == no_auth_actions["EXIT"]:
                    clear_terminal()
                    print("Bay bay!")
                    keep_going = False
                    break

                if no_auth_action == no_auth_actions["REGISTER"]:
                    clear_terminal()
                    register_response = register()
                    if register_response == "back":
                        continue
                    if register_response["success"] is False:
                        clear_terminal()
                        print("There was an error creating the new user, try again please.")
                        continue
                    clear_terminal()
                    new_user_id = register_response["data"]
                    print(f"User {new_user_id} created successfully!")

                if no_auth_action == no_auth_actions["LOGIN"]:
                    clear_terminal()
                    login_response = login()
                    if login_response == "back":
                        continue
                    if login_response["success"] is False:
                        clear_terminal()
                        print(f"There was an error login into your account, please try again. {login_response['data']}")
                        continue
                    logged_user = login_response["data"]
                    no_auth_action = no_auth_actions["EXIT"]

            while logged_user is not None:

                auth_action = auth_menu()

                if auth_action == auth_actions["LIST"]:
                    clear_terminal()
                    list_response = list_task(logged_user["id"])
                    if not list_response["success"]:
                        clear_terminal()
                        print(f"There was an error listing your tasks. {list_response['data']}")
                        continue
                    all_tasks = list_response['data']
                    print_tasks(all_tasks)
                    

                if auth_action == auth_actions["CREATE"]:
                    clear_terminal()
                    add_task_menu_response = add_new_task_menu()
                    if add_task_menu_response == "back":
                        continue
                    add_task_in_db_response = add_task(logged_user["id"], add_task_menu_response["task_title"], add_task_menu_response["task_description"], add_task_menu_response["task_finished"])
                    if add_task_in_db_response["success"] == False:
                        clear_terminal()
                        print(f"There was an error creating the new task, try again please. {str(add_task_in_db_response['data'])}")
                        continue
                    clear_terminal()
                    new_taks_id = add_task_in_db_response["data"]
                    print(f"Task {new_taks_id} created successfully!")

                if auth_action == auth_actions["UPDATE"]:
                    clear_terminal()
                    task_to_update_id = select_one_task_menu(user_id=logged_user["id"])
                    task_in_db = select_one_task(task_to_update_id)
                    if task_in_db["success"] == False:
                        clear_terminal()
                        print("No tasks found with provided id.")
                        continue
                    new_task_information = update_task_menu(task_in_db["data"])
                    updated_task_response = update_task(task_to_update_id, new_task_information["task_title"], new_task_information["task_description"], new_task_information["task_finished"])
                    if updated_task_response["success"] == False:
                        clear_terminal()
                        print(f"There was an error updating the task, try again please. {str(updated_task_response['data'])}")
                        continue
                    clear_terminal()
                    updated_task_id = updated_task_response["data"]
                    print(f"Task {updated_task_id} updated successfully!")

                if auth_action == auth_actions["DELETE"]:
                    clear_terminal()
                    task_to_delete_id = select_one_task_menu(user_id=logged_user["id"])
                    task_in_db = select_one_task(task_to_delete_id)
                    if task_in_db["success"] == False:
                        clear_terminal()
                        print("No tasks found with provided id.")
                        continue
                    delete_task_response = delete_task(task_to_delete_id)
                    if delete_task_response["success"] == False:
                        clear_terminal()
                        print(f"There was an error deleting the task, try again please. {str(delete_task_response['data'])}")
                        continue
                    clear_terminal()
                    delete_task_id = delete_task_response["data"]
                    print(f"Task {delete_task_id} deleted successfully!")
                
                if auth_action == auth_actions["OUT"]:
                    clear_terminal()
                    print("Logged out")
                    logged_user = None
else:
    print("No conn, or no cur is available.")