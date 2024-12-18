from psycopg2 import extras, connect
from dotenv import load_dotenv
import os

load_dotenv("db.env")

conn = None
cur = None

def list_task(user_id):
    try:

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.DictCursor)

        list_tasks_by_user_query = "SELECT id, title, description, finished FROM tasks WHERE user_id = %s"

        cur.execute(list_tasks_by_user_query, (user_id,))

        query_result = cur.fetchall()

        return {
            'success': True,
            'data': query_result
        }

    except Exception as e:

        print(f"There was an error listing the tasks in db. {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }

    finally:

        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()

def select_one_task(task_id):
    try:

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        select_one_task_query = "SELECT * FROM tasks WHERE id = %s"

        cur.execute(select_one_task_query, (task_id,))

        task_found = cur.fetchone()

        return {
            'success': True,
            'data': task_found
        }

    except Exception as e:

        print(f"Errror consulting for a specific task {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }
    
    finally:

        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close() 

def add_task(user_id, title, description, finished):
    try:

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        add_new_task_query = "INSERT INTO tasks (user_id, title, description, finished) VALUES (%s, %s, %s, %s) RETURNING id"

        cur.execute(add_new_task_query, (user_id, title, description, finished))

        conn.commit()

        query_result = cur.fetchone()

        return {
            'success': True,
            'data': query_result["id"]
        }

    except Exception as e:

        print(f"There was an error adding the task in db. {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }

    finally:

        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()

def update_task(task_id, title, description, finished):
    try:

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        update_task_query = "UPDATE tasks SET title = %s, description = %s, finished = %s WHERE id = %s RETURNING id"

        cur.execute(update_task_query, (title, description, finished, task_id))

        conn.commit()

        query_result = cur.fetchone()

        return {
            'success': True,
            'data': query_result["id"]
        }

    except Exception as e:

        print(f"There was an error updating the task in db. {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }

    finally:

        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()

def delete_task(task_id):
    try:

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        delete_task_query = "DELETE FROM tasks WHERE id = %s RETURNING id"

        cur.execute(delete_task_query, (task_id,))

        conn.commit()

        query_result = cur.fetchone()

        return {
            'success': True,
            'data': query_result["id"]
        }

    except Exception as e:

        print(f"There was an error deleting the task in db. {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }

    finally:

        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()