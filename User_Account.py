# from Delivery_Company_GUI import viewOrder
# from Computer_Part_Company_GUI import viewWallet
from Connect_DB import *
from tkinter import *
from tkinter import ttk
from Customer_Complain import *
from Buy_GUI import *
from Order_History import *

def account_view(id):
    def viewWallet(id):
        print("do something")

    def viewOrders(id):
        make_order_history(id)

    def talkToClerk(id):
        print("do something")

    def userCart(id):
        viewCart(id)

    def complain_about_clerk(id):
        def view_clerk(values):
            def return_reason():
                def comment_to_database(text, values):
                    def notify_success():
                        def delete_success():
                            success.destroy()
                            detail.destroy()
                        success = Tk()
                        success.title('Write a Complain')
                        success.geometry('250x50')
                        label = Label(success, text = "Successful complain!")
                        label.pack()
                        Button(success, text="Ok", command=delete_success, borderwidth=0, font=('Helvetica', 12)).pack()
                    # sql_query = "SELECT email FROM computer_store.registered_customers WHERE registered_id=" + str(author_id)
                    # cursor.execute(sql_query)
                    # author_email = cursor.fetchall()
                    # print(author_name)
                    # author_email = author_email[0][0]

                    sql_query = "INSERT INTO computer_store.complain (complainee_email, complainant_id, reason) VALUES ('"+ values[2] + "'," +  str(id) + ","    + "'" + text + "')"
                    cursor.execute(sql_query)
                    con.commit()
                    notify_success()
                    print(values)


                reason_text = reason.get()
                reason.delete(0, 'end')
                print(reason_text)
                comment_to_database(reason_text, values)

            print(values)
            detail = Tk()
            detail.title('Write complain about Clerk #' + str(values[0]))
            detail.geometry('300x100')

            label = Label(detail, text = 'WRITE THE COMPLAIN')
            label.config(font = ("Hevetica", 15, "underline"))
            label.pack()

            reason = Entry(detail)
            reason.pack()
            Button(detail, text="Confirm", command=return_reason, borderwidth=0, font=('Helvetica', 12)).pack()
            print("complain")
            select_button = Button(detail, text="Complain", command=lambda values=values: return_reason(values))
            select_button.pack(pady=20)

        def select_clerk():
            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')
            # temp_label.config(text=values)
            view_clerk(values)


        clerk = Tk()
        clerk.title('Complain about Clerk')
        clerk.geometry('1200x500')

        label = Label(clerk, text = 'Check Clerks')
        label.config(font = ("Hevetica", 15, "underline"))
        label.pack()

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
        style.map("Treeview", background = [("selected", "#347083")])
        
        table = Frame(clerk)
        table.pack(pady=10)

        table_scroll = Scrollbar(table)
        table_scroll.pack(side = RIGHT, fill = Y)
        my_tree = ttk.Treeview(table, yscrollcommand = table_scroll.set, selectmode = "extended")
        my_tree.pack()
        table_scroll.config(command = my_tree.yview)

        my_tree['columns'] = ("Clerk ID", "Clerk Name", "Clerk Email")# "Standing Warnings")
        my_tree.column("#0", width = 0, stretch = NO)
        my_tree.column("Clerk ID", anchor = CENTER, width = 140)
        my_tree.column("Clerk Name", anchor = CENTER, width = 140)
        my_tree.column("Clerk Email", anchor = CENTER, width = 140)
        # my_tree.column("Standing Warnings", anchor = CENTER, width = 140)

        my_tree.heading("#0", text = "", anchor = CENTER)
        my_tree.heading("Clerk ID", text = "Clerk ID", anchor = CENTER)
        my_tree.heading("Clerk Name", text = "Clerk Name", anchor = CENTER)
        my_tree.heading("Clerk Email", text = "Clerk Email", anchor = CENTER)
        # my_tree.heading("Standing Warnings", text = "Standing Warnings", anchor = CENTER)

        my_tree.tag_configure('oddrow', background = "white")
        my_tree.tag_configure('evenrow', background = "lightblue")

        cursor.execute("Select clerk_id, name, email FROM computer_store.store_clerk")
        records = cursor.fetchall()
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
            count += 1

        select_button = Button(clerk, text="Complain about Clerk", command=select_clerk)
        select_button.pack(pady=20)

    def complain_about_purchased_item(id):
        def view_item(values):
            def return_reason():
                def comment_to_database(text, values):
                    def notify_success():
                        def delete_success():
                            success.destroy()
                            detail.destroy()
                        success = Tk()
                        success.title('Write a Complain')
                        success.geometry('250x50')
                        label = Label(success, text = "Successful complain!")
                        label.pack()
                        Button(success, text="Ok", command=delete_success, borderwidth=0, font=('Helvetica', 12)).pack()
                    # sql_query = "SELECT email FROM computer_store.registered_customers WHERE registered_id=" + str(author_id)
                    # cursor.execute(sql_query)
                    # author_email = cursor.fetchall()
                    # print(author_name)
                    # author_email = author_email[0][0]
                    sql_query = "SELECT email FROM computer_store.computer_parts_companies WHERE company_id=" + values[1]
                    cursor.execute(sql_query)
                    email_of_company = cursor.fetchall()
                    print(email_of_company[0][0])
                    sql_query = "INSERT INTO computer_store.complain (complainee_email, complainant_id, reason) VALUES ('"+ email_of_company[0][0] + "'," +  str(id) + ","    + "'" + text + "')"
                    cursor.execute(sql_query)
                    con.commit()
                    notify_success()
                    print(values)


                reason_text = reason.get()
                reason.delete(0, 'end')
                print(reason_text)
                comment_to_database(reason_text, values)

            print("these are the values")
            print(values)
            detail = Tk()
            detail.title('Write complain about Item ' + values[0])
            detail.geometry('300x100')

            label = Label(detail, text = 'WRITE THE COMPLAIN')
            label.config(font = ("Hevetica", 15, "underline"))
            label.pack()

            reason = Entry(detail)
            reason.pack()
            Button(detail, text="Confirm", command=return_reason, borderwidth=0, font=('Helvetica', 12)).pack()
            print("complain")
            select_button = Button(detail, text="Complain", command=lambda values=values: return_reason(values))
            select_button.pack(pady=20)

        def select_item():
            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')
            # temp_label.config(text=values)
            view_item(values)


        item = Tk()
        item.title('Complain about Item')
        item.geometry('1200x500')

        label = Label(item, text = 'Check Items')
        label.config(font = ("Hevetica", 15, "underline"))
        label.pack()

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
        style.map("Treeview", background = [("selected", "#347083")])
        
        table = Frame(item)
        table.pack(pady=10)

        table_scroll = Scrollbar(table)
        table_scroll.pack(side = RIGHT, fill = Y)
        my_tree = ttk.Treeview(table, yscrollcommand = table_scroll.set, selectmode = "extended")
        my_tree.pack()
        table_scroll.config(command = my_tree.yview)

        my_tree['columns'] = ("Item Name", "Company ID")#, "Clerk Email")# "Standing Warnings")
        my_tree.column("#0", width = 0, stretch = NO)
        my_tree.column("Item Name", anchor = CENTER, width = 140)
        my_tree.column("Company ID", anchor = CENTER, width = 140)
        # my_tree.column("Clerk Email", anchor = CENTER, width = 140)
        # my_tree.column("Standing Warnings", anchor = CENTER, width = 140)

        my_tree.heading("#0", text = "", anchor = CENTER)
        my_tree.heading("Item Name", text = "Item Name", anchor = CENTER)
        my_tree.heading("Company ID", text = "Company ID", anchor = CENTER)
        # my_tree.heading("Clerk Email", text = "Clerk Email", anchor = CENTER)
        # my_tree.heading("Standing Warnings", text = "Standing Warnings", anchor = CENTER)

        my_tree.tag_configure('oddrow', background = "white")
        my_tree.tag_configure('evenrow', background = "lightblue")

        cursor.execute("Select name FROM computer_store.customer_purchases WHERE registered_id=" + str(id))
        name_of_item = cursor.fetchall()
        print(name_of_item)
        
        list_of_ids = []
        for pitem in name_of_item:
            print(pitem[0])
            sql_query = "SELECT company_id FROM computer_store.case WHERE name='" + pitem[0] + "' UNION SELECT company_id FROM computer_store.cooler WHERE name='" + pitem[0] + "' UNION SELECT company_id FROM computer_store.cpu WHERE name='" + pitem[0] + "' UNION SELECT company_id FROM computer_store.gpu WHERE name='" + pitem[0] + "' UNION SELECT company_id FROM computer_store.motherboard WHERE name='" + pitem[0]+ "' UNION SELECT company_id FROM computer_store.powersupply WHERE name='" + pitem[0] + "' UNION SELECT company_id FROM computer_store.ram WHERE name='" + pitem[0] + "' UNION SELECT company_id FROM computer_store.storage WHERE name='" + pitem[0] + "'"
            cursor.execute(sql_query)
            company_id = cursor.fetchall()
            print(company_id)
            list_of_ids.append(company_id[0])

        print(list_of_ids)
        print(name_of_item)
        
        # for pitem in name_of_item:
        #     cursor.execute("Select company_id FROM computer_store.computer_parts_companies WHERE ")
        # cursor.execute("Select clerk_id, name, email FROM computer_store.store_clerk")
        # records = cursor.fetchall()
        count = 0
        for id_of_company in list_of_ids:
            for name_item in name_of_item:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(name_item[0], id_of_company[0]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(name_item[0], id_of_company[0]), tags=('evenrow',))
                count += 1

        select_button = Button(item, text="Complain about item", command=select_item)
        select_button.pack(pady=20)
    def complain_about_delivery_company(id):
        print("get ")


    account = Tk()
    account.title('Account Page')
    account.geometry('500x800')

    cursor.execute("Select name FROM registered_customers WHERE registered_id = %s", (id,))
    data = cursor.fetchall()
    name = data[0][0]

    welcomeMessage = 'Welcome ' + name
    Title_Label = Label(account, text = welcomeMessage)
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    Label(account, text="").pack()
    Label(account, text="").pack()
    Label(account, text="").pack()

    complaints_button = Button(account, text = "List of Complaints", width = 20, height = 3, command = lambda id=id: browse_all_complains(id))
    complaints_button.config(font = ("Hevetica", 15,))
    complaints_button.pack()
    
    # appeals_button = Button(manager, text = "List of Appeals", width = 20, height = 3, command = viewAppeals)
    # appeals_button.config(font = ("Hevetica", 15,))
    # appeals_button.pack()

    wallet_button = Button(account, text = "View wallet", width = 20, height = 3, command = lambda id=id: viewWallet(id))
    wallet_button.config(font = ("Hevetica", 15,))
    wallet_button.pack()

    orders_button = Button(account, text = "View orders", width = 20, height = 3, command = lambda id=id: viewOrders(id))
    orders_button.config(font = ("Hevetica", 15,))
    orders_button.pack()

    talk_to_clerk_button = Button(account, text = "Talk to clerk", width = 20, height = 3, command = lambda id=id: talkToClerk(id))
    talk_to_clerk_button.config(font = ("Hevetica", 15,))
    talk_to_clerk_button.pack()

    cart_button = Button(account, text = "View cart", width = 20, height = 3, command = lambda id=id: userCart(id))
    cart_button.config(font = ("Hevetica", 15,))
    cart_button.pack()

    complain_item = Button(account, text = "Complain about item", width = 20, height = 3, command = lambda id=id: complain_about_purchased_item(id))
    complain_item.config(font = ("Hevetica", 15,))
    complain_item.pack()

    complain_clerk = Button(account, text = "Complain about clerk", width = 20, height = 3, command = lambda id=id: complain_about_clerk(id))
    complain_clerk.config(font = ("Hevetica", 15,))
    complain_clerk.pack()

    complain_delivery_company = Button(account, text = "Complain about delivery company", width = 20, height = 3, command = lambda id=id: complain_about_delivery_company(id))
    complain_delivery_company.config(font = ("Hevetica", 15,))
    complain_delivery_company.pack()
    # clerk_button = Button(manager, text = "List of Clerks", width = 20, height = 3, command = viewClerks)
    # clerk_button.config(font = ("Hevetica", 15,))
    # clerk_button.pack()

    account.mainloop()

