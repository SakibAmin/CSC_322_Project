import mysql.connector
import sqlite3

#Goals: Add Unique Users to Tables and create warning message if user registering with same email

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)
print ("Connnected To Database")

#Creating New Registered Customer
cursor = con.cursor()

def Register_Customer(): #This will allow users to create an account

    email = input("Enter your email: ")
    cursor.execute("SELECT * FROM Registered_Customers WHERE email = %s", (email,))
    data = cursor.fetchall()
    if len(data) == 0:
        password_loop = True
        while password_loop == True:
            password1 = input("Enter your password: ")
            password2 = input("Please Confirm password: ")
            if password1 == password2:
                break
            else:
                print("Passwords do not match please try again")
    else:
        print("This email is already in use")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    cursor.execute("INSERT INTO registered_customers (name, email, password, address) VALUES ('{}', '{}', '{}', '{}')".format(name, email, password1, address))
    con.commit()
    print(cursor.rowcount, "record inserted")

def Login_Customer(): #This will allow users to login to the system
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT * FROM Registered_Customers WHERE email = %s AND password = %s", (email, password))
    result = cursor.fetchall()
    count = cursor.rowcount
    #print (count)
    if count == 1:
        print("Login Successful")
    else:
        print("Email or Password is Incorrect")


#def Register_Delivery_Companies():

#def Register_Part_Companies():

con.close()

