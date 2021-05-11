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
"(registered_id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), email VARCHAR(255)," +
"password VARCHAR(255), address VARCHAR(255), PRIMARY KEY (registered_id))")

cursor.execute("CREATE TABLE Store_Clerk" + 
"(clerk_id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), email VARCHAR(255)," +
"password VARCHAR(255), PRIMARY KEY (clerk_id))")

cursor.execute("CREATE TABLE Store_Manager" + 
"(manager_id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), email VARCHAR(255)," +
"password VARCHAR(255), PRIMARY KEY (manager_id))")

cursor.execute("CREATE TABLE Computer_Parts_Companies" +
"(company_id into NOT NULL AUTO_INCREMENT, Company_Name VARCHAR(255), email VARCHAR(255)," +
"password VARCHAR(255), PRIMARY KEY (company_id))")

cursor.execute("CREATE TABLE Delivery_Companies" +
"(delivery_id int NOT NULL AUTO_INCREMENT, Company_Name VARCHAR(255), email VARCHAR(255)," +
"password VARCHAR(255), PRIMARY KEY (delivery_id))")

#Check to see if Tables Exist
cursor.execute("Show Tables")
for x in cursor:
        print(x)


con.close()