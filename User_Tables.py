import mysql.connector

#Creation of all the different users and their log in inforamtion

#Connecting to Database
con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
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

cursor.execute("CREATE TABLE customer_purchases" +
"(purchase_id int NOT NULL AUTO_INCREMENT, order_id int, registered_id int, name VARCHAR(255)," +
"quantity int, price int, " +
"PRIMARY KEY(purchase_id), FOREIGN KEY (order_id) REFERENCES customer_orders(order_id), FOREIGN KEY (registered_id) REFERENCES registered_customers(registered_id))")

cursor.execute("CREATE TABLE delivery_bid" +
"(order_id int, delivery_id int, bid int," +
"PRIMARY KEY(order_id, delivery_id), FOREIGN KEY (order_id) REFERENCES customer_orders(order_id))")


cursor.execute("CREATE TABLE PreBuild" +
"(prebuild_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"cpu VARCHAR(255), ram VARCHAR(255), gpu VARCHAR(255), storage VARCHAR(255), powersupply VARCHAR(255), OS VARCHAR(255)," +
"price int, in_stock int, sold int, total_profit int," +
"PRIMARY KEY(prebuild_id), FOREIGN KEY (company_id) REFERENCES  computer_parts_companies (company_id))")

#Check to see if Tables Exist
cursor.execute("Show Tables")
for x in cursor:
        print(x)


con.close()