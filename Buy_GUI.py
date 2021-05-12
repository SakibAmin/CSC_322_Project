from tkinter import *
from tkinter import ttk
import mysql.connector
import os
con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
        database = "computer_store",
        port = 3306
)

#print ("Connnected To Database")
cursor = con.cursor()

#Cart Table
'''
cursor.execute("CREATE TABLE Cart" +
"(cart_id int NOT NULL AUTO_INCREMENT, registered_id int, product_name VARCHAR(255)," +
"quantity int, price int," +
"PRIMARY KEY (cart_id), FOREIGN KEY (registered_id) REFERENCES registered_customers(registered_id))")
'''

def addtoCart(item):

    #CPU
    cursor.execute("Select name, price FROM cpu WHERE name = %s", (item,))
    global id
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()
    
    #RAM
    cursor.execute("Select name, price FROM ram WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()

    #GPU
    cursor.execute("Select name, price FROM gpu WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()

    #Motherboard
    cursor.execute("Select name, price FROM motherboard WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()
    
    #Case
    cursor.execute("Select name, price FROM cases WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()
    
    #Storage
    cursor.execute("Select name, price FROM storage WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()
    
    #Cooler
    cursor.execute("Select name, price FROM cooler WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()
    
    #Power
    cursor.execute("Select name, price FROM powersupply WHERE name = %s", (item,))
    records = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        for record in records:
            name = record[0]
            price = record[1]
        quantity = 1
        cursor.execute("INSERT INTO cart (registered_id, product_name, quantity, price)" + 
        "VALUES ('{}','{}','{}','{}')".format(id, name, quantity, price))
        con.commit()
id = 1
item = 'Seagate Barracuda Compute '
addtoCart(item)