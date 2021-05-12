''' Connects to computer_store database, use as such:

        from db_connector import get_db_connection

        with get_db_connection() as conn:
            ...
'''

from mysql.connector import connect, Error
import contextlib

@contextlib.contextmanager
def get_db_connection():
    conn = connect(
            host="localhost",
            user="user", # for some reason, "root" denies me access, so change this to root if that's what you used
            password="password",
            database="computer_store")
    try:
        yield conn
    except Error as e:
        print(e)
    finally:
        conn.close()