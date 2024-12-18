from psycopg2 import extras, connect
from dotenv import load_dotenv
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.passwords import encrypt_password, test_password

load_dotenv("db.env")

conn = None
cur = None

def login_user(email, password):
    try:

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        find_by_email_query = "SELECT * FROM users WHERE email = %s"

        cur.execute(find_by_email_query, (email,))

        find_by_email_response = cur.fetchone()

        if find_by_email_response is None:
            raise Exception("No users found with provided email.")
        
        correct_password = test_password(password, find_by_email_response["password"])
        
        if not correct_password["success"]:
            raise Exception(correct_password["data"])
        
        if not correct_password["data"]:
            raise Exception("Incorrect password")
        
        return {
            'success': True,
            'data': find_by_email_response
        }

    except Exception as e:

        print(f"There was an error consulting from the db to login {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }

    finally:

        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()

def exists_email(email):
    try:
        
        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        count_email_query = "SELECT COUNT(*) AS total FROM users WHERE email = %s"

        cur.execute(count_email_query, (email,))

        count_query_result = cur.fetchone()

        return {
            'success': True,
            'data': int(count_query_result["total"]) > 0
        }

    except Exception as e:

        print(f"There was an error consulting from the db {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }

    finally:

        if conn is not None:
            conn.close()

        if cur is not None:
            cur.close()

def add_user(name, email, password):
    try:

        hashed_password = encrypt_password(password)

        if not hashed_password["success"]:
            raise Exception(hashed_password["data"])

        conn = connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        query = "INSERT INTO users(name, email, password) VALUES (%s, %s, %s) RETURNING id"

        cur.execute(query, (name, email, hashed_password["data"]))

        new_user_response = cur.fetchone()

        conn.commit()

        return {
            'success': True,
            'data': new_user_response["id"]
        }

    except Exception as e:
        
        print(f"Error adding the user {str(e)}")

        return {
            'success': False,
            'data': str(e)
        }
    
    finally:

        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close()