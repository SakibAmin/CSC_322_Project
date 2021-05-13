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

#View Order Table

def viewOrder():

    order = Tk()
    order.geometry('500x500')

    Title_Label = Label(order, text = "Pending Orders")
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(order)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Order Id", "Total Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Order Id", anchor = CENTER, width = 140)
    my_tree.column("Total Price", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Order Id", text = "Order Id", anchor = CENTER)
    my_tree.heading("Total Price", text = "Total Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    #CPU
    cursor.execute("Select order_id, total_price FROM customer_orders WHERE order_status = 'Processing'")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
        count += 1
    con.commit()


    button_frame = LabelFrame(order)
    button_frame.pack(expand="yes", padx=0, pady = 0)

    def placeBid():

        '''
        cursor.execute("CREATE TABLE delivery_bid" +
        "(order_id int, delivery_id int, bid int," +
        "PRIMARY KEY(order_id, delivery_id), FOREIGN KEY (order_id) REFERENCES customer_orders(order_id))")
        '''

        global id

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        order_id = values[0]

        bid = Tk()
        bid.geometry('200x100')

        Bid_Label = Label(bid, text = "Bid: ")
        Bid_Label.config(font = ("Hevetica", 10))
        Bid_Label.grid(row=0, column=0, padx=0, pady=0)

        bidAmount = IntVar()
        bidEntry = Entry(bid, textvariable = bidAmount)
        bidEntry.grid(row=0, column=1, padx=0, pady=0)

        def bidFunction():
            bidAmount = bidEntry.get()

            cursor.execute("Select * FROM delivery_bid WHERE order_id = %s AND delivery_id = %s", (order_id, id))
            count = cursor.rowcount
            if count == 1:
                placed_Label = Label(bid, text = "Your ")
                placed_Label.config(font = ("Hevetica", 10))
                placed_Label.grid(row=3, column=1, padx=0, pady=0)


            cursor.execute("INSERT INTO delivery_bid (order_id, delivery_id, bid)" +
            "VALUES ('{}','{}','{}')".format(order_id, id, bidAmount))
            con.commit()

        bid_Button = Button(bid, text = "Update Quantity", width = 13, command = bidFunction)
        bid_Button.grid(row=1, column=1, padx=0, pady=0)

        




    Bid_Button = Button(button_frame, text = "Bid on Order", width = 10, command = placeBid)
    Bid_Button.config(font = ("Hevetica", 15,))
    Bid_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

    order.mainloop()

id = 1
viewOrder()