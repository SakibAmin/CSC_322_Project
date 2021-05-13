import mysql.connector

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$", #change for your own pw
        database = "computer_store",
        port = 3306,
        auth_plugin="mysql_native_password"
)

cursor = con.cursor(buffered=True)
