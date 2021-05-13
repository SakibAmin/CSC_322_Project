from Clerk_Complain import browse_all_complains
import mysql.connector
from tkinter import *
from tkinter import ttk
import os

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)
#print ("Connnected To Database")
cursor = con.cursor()

def Clerk_GUI(id):

    clerk = Tk()
    clerk.geometry('500x450')

    #Title Label
    cursor.execute("Select name FROM store_clerk WHERE clerk_id = %s", (id,))
    records = cursor.fetchall()
    for record in records:
        name = record[0]
    #We will be getting info from login about the id 
    welcomeMessage = 'Welcome Back {}'.format(name)
    Title_Label = Label(clerk, text = welcomeMessage)
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    Label(clerk, text="").pack()
    Label(clerk, text="").pack()
    Label(clerk, text="").pack()

    def vpendOrders():

        viewpendOrders(id)

    pendOrders_Button = Button(clerk, text = "Bidding Orders", width = 20, height = 3, command = vpendOrders)
    pendOrders_Button.config(font = ("Hevetica", 15,))
    pendOrders_Button.pack()

    complain_button = Button(clerk, text = "List of Complains", width = 20, height = 3, command = lambda id=id: browse_all_complains(id))
    complain_button.config(font = ("Hevetica", 15,))
    complain_button.pack()

    clerk.mainloop()

def viewpendOrders(id):
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

    my_tree['columns'] = ("Order Id", "Delivery Id", "bid")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Order Id", anchor = CENTER, width = 140)
    my_tree.column("Delivery Id", anchor = CENTER, width = 140)
    my_tree.column("bid", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Order Id", text = "Order Id", anchor = CENTER)
    my_tree.heading("Delivery Id", text = "Delivery Id", anchor = CENTER)
    my_tree.heading("bid", text = "Bid", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("Select order_id, delivery_id, bid FROM delivery_bid")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        count += 1
    con.commit()

    button_frame = LabelFrame(order)
    button_frame.pack(expand="yes", padx=0, pady = 0)

    def sortOrder():

        order.destroy()
        bid = Tk()
        bid.geometry('300x100')

        order_Label = Label(bid, text = "Order Number: ")
        order_Label.config(font = ("Hevetica", 10))
        order_Label.grid(row=0, column=0, padx=0, pady=0)

        order_id = IntVar()
        OrderEntry = Entry(bid, textvariable = order_id)
        OrderEntry.grid(row=0, column=1, padx=0, pady=0)

        def findBids():

            
            find = Tk()
            find.geometry('500x500')

            order_id = OrderEntry.get()
            bid.destroy()

            Title_Label = Label(find, text = "Pending Orders")
            Title_Label.config(font = ("Hevetica", 20, "underline"))
            Title_Label.pack()

            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
            style.map("Treeview", background = [("selected", "#347083")])
            
            tree_frame = Frame(find)
            tree_frame.pack(pady = 10)
            
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side = RIGHT, fill = Y)
            my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
            my_tree.pack()
            tree_scroll.config(command = my_tree.yview)

            my_tree['columns'] = ("Order Id", "Delivery Id", "bid")
            my_tree.column("#0", width = 0, stretch = NO)
            my_tree.column("Order Id", anchor = CENTER, width = 140)
            my_tree.column("Delivery Id", anchor = CENTER, width = 140)
            my_tree.column("bid", anchor = CENTER, width = 140)

            my_tree.heading("#0", text = "", anchor = CENTER)
            my_tree.heading("Order Id", text = "Order Id", anchor = CENTER)
            my_tree.heading("Delivery Id", text = "Delivery Id", anchor = CENTER)
            my_tree.heading("bid", text = "Bid", anchor = CENTER)

            my_tree.tag_configure('oddrow', background = "white")
            my_tree.tag_configure('evenrow', background = "lightblue")

            cursor.execute("Select order_id, delivery_id, bid FROM delivery_bid WHERE order_id = %s", (order_id,))
            records = cursor.fetchall()
            count = 0
            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
                count += 1
            con.commit()

            button_frame = LabelFrame(find)
            button_frame.pack(expand="yes", padx=0, pady = 0)

            def winBid():

                win = Tk()
                win.geometry('300x100')

                selected = my_tree.focus()
                values = my_tree.item(selected, 'values')

                delivery_id = values[1]

                reason_Label = Label(win, text = "Reasoning: ")
                reason_Label.config(font = ("Hevetica", 10))
                reason_Label.grid(row=0, column=0, padx=0, pady=0)

                reasoning = StringVar()
                reasonEntry = Entry(win, textvariable = reasoning)
                reasonEntry.grid(row=0, column=1, padx=0, pady=0)

                def finalOrder():

                    reasoning = reasonEntry.get()
                    find.destroy()
                    win.destroy()
                    cursor.execute("Update customer_orders SET order_status = 'Shipped', winning_delivery_company_id = %s, reasoning = %s WHERE order_id = %s",(delivery_id, reasoning, order_id))
                    con.commit()

                    cursor.execute("Delete FROM delivery_bid WHERE order_id = %s",(order_id,))
                    con.commit()

                reasoning_Button = Button(win, text = "Update Quantity", width = 13, command = finalOrder)
                reasoning_Button.grid(row=1, column=1, padx=0, pady=0)

                

            winning_Button = Button(button_frame, text = "Select Delivery Company", width = 20, command = winBid)
            winning_Button.config(font = ("Hevetica", 15,))
            winning_Button.grid(row = 0, column = 0, padx = 0, pady = 0)


        sort_Button = Button(bid, text = "Find Order Bids", width = 13, command = findBids)
        sort_Button.grid(row=1, column=1, padx=0, pady=0)

    Sort_Button = Button(button_frame, text = "Find Order", width = 10, command = sortOrder)
    Sort_Button.config(font = ("Hevetica", 15,))
    Sort_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

#id = 1
#Clerk_GUI()