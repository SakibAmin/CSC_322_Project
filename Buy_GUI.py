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


def viewCart():

    cart = Tk()
    cart.geometry('500x450')

    Cart_Label = Label(cart, text = "Cart")
    Cart_Label.config(font = ("Hevetica", 20, "underline"))
    Cart_Label.pack()

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(cart)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Product Name", "Quantity", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Product Name", anchor = CENTER, width = 160)
    my_tree.column("Quantity", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 140)
    
    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Product Name", text = "Product Name", anchor = CENTER)
    my_tree.heading("Quantity", text = "Quantity", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    cursor.execute("Select product_name, quantity, price FROM cart WHERE registered_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        count += 1
    con.commit()

    cursor.execute("SELECT SUM(price) FROM cart WHERE registered_id = %s", (id,))
    totalsum = cursor.fetchall()[0][0]
    if totalsum is None:
        cpusum = 0

    Button_Frame = LabelFrame(cart)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def buy():

        '''
        cursor.execute("CREATE TABLE customer_purchases" +
        "(purchase_id int NOT NULL AUTO_INCREMENT, order_id int, registered_id int, name VARCHAR(255)," +
        "quantity int, price int, " +
        "PRIMARY KEY(purchase_id), FOREIGN KEY (order_id) REFERENCES customer_orders(order_id), FOREIGN KEY (registered_id) REFERENCES registered_customers(registered_id))")
        '''

        order_status = 'Processing'
        cursor.execute("INSERT INTO customer_orders (customer_id, total_price, order_status)" +
        "VALUES ('{}','{}','{}')".format(id, totalsum, order_status))
        con.commit()

        cursor.execute("Select order_id FROM customer_orders WHERE customer_id = %s and total_price = %s", (id, totalsum))
        records = cursor.fetchall()
        for record in records:
            order_id = record[0]

        cursor.execute("INSERT INTO customer_purchases (registered_id, name, quantity, price) SELECT registered_id, product_name, quantity, price FROM cart WHERE registered_id = %s", (id,))
        con.commit()

        cursor.execute("Update customer_purchases SET order_id = %s WHERE registered_id = %s",(order_id, id))
        con.commit()

        cursor.execute("Delete FROM cart WHERE registered_id = %s",(id,))
        con.commit()

        obuy = Tk()
        obuy.geometry('200x150')

        order_Label = Label(obuy, text = "Your Order Has been placed")
        order_Label.config(font = ("Hevetica", 10))
        order_Label.grid(row=0, column=0, padx=0, pady=0)

        def destroy():

            obuy.destroy()
            cart.destroy()

        confo_Button = Button(obuy, text = "Ok", width = 13, command = destroy)
        confo_Button.pack()

    def delete():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        name = values[0]
        cursor.execute("Delete FROM cart WHERE product_name = %s",(name,))
        cart.destroy() 
        viewCart()
        con.commit()
    
    def updateQuantity():

        def update():

            quantity = quantityEntry.get()
            quantity = float(quantity)
            new_price = o_price * quantity
            cursor.execute("Update cart SET quantity = %s, price = %s WHERE product_name = %s",(quantity, new_price, name))
            quan.destroy()
            cart.destroy() 
            viewCart()

        quan = Tk()
        quan.geometry('200x150')
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        name = values[0]
        oldQuantity = values[1]
        price = values[2]
        price = int(price)
        oldQuantity = int(oldQuantity)
        o_price = price/oldQuantity

        Quantity_Label = Label(quan, text = "Quantity")
        Quantity_Label.config(font = ("Hevetica", 10))
        Quantity_Label.grid(row=0, column=0, padx=0, pady=0)

        quantity = IntVar()
        quantityEntry = Entry(quan, textvariable = quantity)
        quantityEntry.grid(row=0, column=1, padx=0, pady=0)

        Quantity_Button = Button(quan, text = "Update Quantity", width = 13, command = update)
        Quantity_Button.grid(row=1, column=1, padx=0, pady=0)


    Total_Label = Label(Button_Frame, text = "Total: $%s" % totalsum)
    Total_Label.config(font = ("Hevetica", 20))
    Total_Label.grid(row=0, column=4, padx=0, pady=0)

    updateQuantity_Button = Button(Button_Frame, text = "Update Quantity", width = 13, command = updateQuantity)
    updateQuantity_Button.grid(row=0, column=0, padx=0, pady=0)
    
    Buy_Button = Button(Button_Frame, text = "Buy this Build", width = 13, command = buy)
    Buy_Button.grid(row=0, column=3, padx=0, pady=0)

    Delete_Button = Button(Button_Frame, text = "Remove Item", width = 13, command = delete)
    Delete_Button.grid(row=0, column=2, padx=0, pady=0)

    cart.mainloop()

    
id = 1
item = 'Seagate Barracuda Compute '
#addtoCart(item)
#viewCart()