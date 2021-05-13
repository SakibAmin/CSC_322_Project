import mysql.connector

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
        database = "computer_store",
        port = 3306
)
#print ("Connnected To Database")
cursor = con.cursor()

id = 1
name1 = 123
cursor.execute("SELECT name FROM computer_parts_companies WHERE company_id = %s", (id,))
records = cursor.fetchall()
count = cursor.rowcount

for x in records:
  print(x)
print(count)