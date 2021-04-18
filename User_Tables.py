import mysql.connector

#Creation of all the different users and their log in inforamtion

#Connecting to Database
con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
        database = "computer_store",
        port = 3306
)
print ("Connnected")

#Creating User Tables
cursor = con.cursor()

cursor.execute("CREATE TABLE Registered_Customers" + 
"(name VARCHAR(255), email VARCHAR(255) PRIMARY KEY," +
"password VARCHAR(255), address VARCHAR(255))")

cursor.execute("CREATE TABLE Store_Clerk" +
"(name VARCHAR(255), email VARCHAR(255) PRIMARY KEY," +
"password VARCHAR(255))")

cursor.execute("CREATE TABLE Store_Managers" +
"(name VARCHAR(255), email VARCHAR(255) PRIMARY KEY," +
"password VARCHAR(255))")

cursor.execute("CREATE TABLE Computer_Parts_Companies" +
"(Company_Name VARCHAR(255), email VARCHAR(255) PRIMARY KEY," +
"password VARCHAR(255))")

cursor.execute("CREATE TABLE Delivery_Companies" +
"(Company_Name VARCHAR(255), email VARCHAR(255) PRIMARY KEY," +
"password VARCHAR(255))")

#Check to see if Tables Exist
cursor.execute("Show Tables")
for x in cursor:
        print(x)


con.close()