from mysql.connector import connect, Error
import contextlib

@contextlib.contextmanager
def get_db_connection():
    connn = connect(
            host="127.0.0.1",
            user="root", # for some reason, "root" denies me access, so change this to root if that's what you used
            password="dbvb72^^DATAf2fa1#$",
            database="computer_store",
            port = 3306,
            auth_plugin="mysql_native_password")
    try:
        yield connn
    except Error as e:
        print(e)
    finally:
        connn.close()