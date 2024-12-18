import psycopg2
import os
from dotenv import load_dotenv

load_dotenv("db.env")

conn = None
cur = None

try:

    conn = psycopg2.connect(dbname=os.environ["POSTGRES_DB"], user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

    cur = conn.cursor()

except Exception as e:
    print(e)
    print("There was an error connecting to database")

finally:

    if conn is not None:
        conn.close()

    if cur is not None:
        conn.close()