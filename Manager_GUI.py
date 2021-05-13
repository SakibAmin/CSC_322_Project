from Connect_DB import *
from tkinter import *
from tkinter import ttk
from Warnings import *
from Logged_Home import *

def manager_view(id):

    manager = Tk()
    manager.title('Manager Page')
    manager.geometry('500x500')

    cursor.execute("Select name FROM store_manager WHERE manager_id = %s", (id,))
    data = cursor.fetchall()
    name = data[0][0]

    welcomeMessage = 'Welcome Back Manager ' + name
    Title_Label = Label(manager, text = welcomeMessage)
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    Label(manager, text="").pack()
    Label(manager, text="").pack()
    Label(manager, text="").pack()

    complaints_button = Button(manager, text = "List of Complaints", width = 20, height = 3, command = viewComplaints)
    complaints_button.config(font = ("Hevetica", 15,))
    complaints_button.pack()
    
    # appeals_button = Button(manager, text = "List of Appeals", width = 20, height = 3, command = viewAppeals)
    # appeals_button.config(font = ("Hevetica", 15,))
    # appeals_button.pack()

    bids_button = Button(manager, text = "List of Bids", width = 20, height = 3, command = viewBids)
    bids_button.config(font = ("Hevetica", 15,))
    bids_button.pack()

    taboo_button = Button(manager, text = "List of Taboo", width = 20, height = 3, command = viewTaboo)
    taboo_button.config(font = ("Hevetica", 15,))
    taboo_button.pack()

    users_button = Button(manager, text = "List of Users", width = 20, height = 3, command = viewUsers)
    users_button.config(font = ("Hevetica", 15,))
    users_button.pack()

    clerk_button = Button(manager, text = "List of Clerks", width = 20, height = 3, command = viewClerks)
    clerk_button.config(font = ("Hevetica", 15,))
    clerk_button.pack()

    manager.mainloop()

def viewComplaints():
    def view_complain(data):
        def rejectComplain():
            print("delete complain/appeal and notify and add warning to the complainant")
            print(data)
            print(appeal_data)
            print(reporter_data)
            print(data[0])
            print(appeal_data[0][0])

            sql_query = "DELETE FROM computer_store.appeal WHERE appeal_id=" + str(appeal_data[0][0])
            cursor.execute(sql_query)
            con.commit()

            sql_query = "DELETE FROM computer_store.complain WHERE complain_id=" + str(data[0])
            cursor.execute(sql_query)
            con.commit()
            detail.destroy()
            complain.destroy()
            viewComplaints()

        def acceptComplain():
            print("delete complain/appeal and notify and add warning to the complainee")
            print(data)
            print(appeal_data)
            print(reporter_data)
            print(data[0])
            print(appeal_data[0][0])

            sql_query = "DELETE FROM computer_store.appeal WHERE appeal_id=" + str(appeal_data[0][0])
            cursor.execute(sql_query)
            con.commit()

            sql_query = "DELETE FROM computer_store.complain WHERE complain_id=" + str(data[0])
            cursor.execute(sql_query)
            con.commit()
            detail.destroy()
            complain.destroy()
            viewComplaints()

        print(data)
        sql_query = "SELECT * FROM computer_store.appeal WHERE complain_id=" + str(data[0])
        cursor.execute(sql_query)
        appeal_data = cursor.fetchall()
        print(appeal_data)

        if cursor.rowcount == 0:
            print("NO APPEAL YET ")
            sql_query = "SELECT * FROM computer_store.registered_customers WHERE registered_id=" + str(data[2])
            cursor.execute(sql_query)
            reporter_data = cursor.fetchall()
            print(reporter_data)

            detail = Tk()
            detail.title('Complain #' + str(data[0]))
            detail.geometry('800x400')

            detail_label = Label(detail, text = 'Review Complain #' + str(data[0]))
            detail_label.config(font = ("Hevetica", 15, "underline"))
            detail_label.pack()

            leftFrame = Frame(detail, width=600, height=400, borderwidth = 1)
            leftFrame.pack(side=LEFT, fill=X, expand=1, anchor=N, pady=20)

            reporter_label = Label(leftFrame, text="Reporter Name: " + reporter_data[0][1], font=("Hevetica", 20)).grid(row=0, column=1)
            reporter_id_label = Label(leftFrame, text="Reporter ID: " + str(reporter_data[0][0]), font=("Hevetica", 20)).grid(row=0, column=0)
            reported_name_label = Label(leftFrame, text="Receiver Email: " + data[1], font=("Hevetica", 20)).grid(row=1, column=1)
            # reported_id_name = Label(leftFrame, text="Receiver ID: " + str(appeal_data[0][2]), font=("Hevetica", 20)).grid(row=1, column=0)
            reason_label = Label(leftFrame, text="Reason: ", font=("Hevetica", 20)).grid(row=2, column=0)
            reason_description_label = Label(leftFrame, text=data[3], font=("Hevetica", 20)).grid(row=2, column=1)
            appeal_label = Label(leftFrame, text="NO APPEAL YET", font=("Hevetica", 20)).grid(row=3, column=1)

            reject_button = Button(detail, text = "Reject Complain", width = 20, height = 3, command = rejectComplain)
            reject_button.config(font = ("Hevetica", 15,))
            reject_button.pack()
            # reject_button.grid(row=3, column=0)

            accept_button = Button(detail, text = "Accept Complain", width = 20, height = 3, command = acceptComplain)
            accept_button.config(font = ("Hevetica", 15,))
            accept_button.pack()
        else:
            sql_query = "SELECT * FROM computer_store.registered_customers WHERE registered_id=" + str(data[2])
            cursor.execute(sql_query)
            reporter_data = cursor.fetchall()
            print(reporter_data)

            detail = Tk()
            detail.title('Complain #' + str(data[0]))
            detail.geometry('1200x500')

            detail_label = Label(detail, text = 'Review Complain #' + str(data[0]))
            detail_label.config(font = ("Hevetica", 15, "underline"))
            detail_label.pack()

            leftFrame = Frame(detail, width=600, height=400, borderwidth = 1)
            leftFrame.pack(side=LEFT, fill=X, expand=1, anchor=N, pady=20)

            reporter_label = Label(leftFrame, text="Reporter Name: " + reporter_data[0][1], font=("Hevetica", 20)).grid(row=0, column=1)
            reporter_id_label = Label(leftFrame, text="Reporter ID: " + str(reporter_data[0][0]), font=("Hevetica", 20)).grid(row=0, column=0)
            reported_name_label = Label(leftFrame, text="Receiver Email: " + data[1], font=("Hevetica", 20)).grid(row=1, column=1)
            # reported_id_name = Label(leftFrame, text="Receiver ID: " + str(appeal_data[0][2]), font=("Hevetica", 20)).grid(row=1, column=0)
            reason_label = Label(leftFrame, text="Reason: ", font=("Hevetica", 20)).grid(row=2, column=0)
            reason_description_label = Label(leftFrame, text=data[3], font=("Hevetica", 20)).grid(row=2, column=1)

            rightFrame = Frame(detail, width=200, height=400, borderwidth = 1)
            rightFrame.pack(side=LEFT, fill=X, expand=1, anchor=N, pady=20)

            # random_label = Label(rightFrame, text="        ", font=("Hevetica", 20)).grid(row=2, column=0)

            appeal_reason = Label(leftFrame, text=appeal_data[0][2], font=("Hevetica", 20)).grid(row=3, column=1)
            appeal_label = Label(leftFrame, text="Appeal: ", font=("Hevetica", 20)).grid(row=3, column=0)

            reject_button = Button(detail, text = "Reject Complain", width = 20, height = 3, command = rejectComplain)
            reject_button.config(font = ("Hevetica", 15,))
            reject_button.pack()
            # reject_button.grid(row=3, column=0)

            accept_button = Button(detail, text = "Accept Complain", width = 20, height = 3, command = acceptComplain)
            accept_button.config(font = ("Hevetica", 15,))
            accept_button.pack()
            # accept_button.grid(row=3, column=1)


    def select_complain():
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        # temp_label.config(text=values)
        view_complain(values)

    complain = Tk()
    complain.title('Complain Page')
    complain.geometry('1200x500')

    label = Label(complain, text = 'Review Complains')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

    # complain_frame = LabelFrame(complain, text="Review Complains")
    # complain_frame.pack(expand="yes", padx=0, pady = 0)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    table = Frame(complain)
    table.pack(pady=10)

    table_scroll = Scrollbar(table)
    table_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(table, yscrollcommand = table_scroll.set, selectmode = "extended")
    my_tree.pack()
    table_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Complain ID", "Complainee", "Reporter's ID", "Reason")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Complain ID", anchor = CENTER, width = 140)
    my_tree.column("Complainee", anchor = CENTER, width = 140)
    my_tree.column("Reporter's ID", anchor = CENTER, width = 140)
    my_tree.column("Reason", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Complain ID", text = "Complain ID", anchor = CENTER)
    my_tree.heading("Complainee", text = "Complainee", anchor = CENTER)
    my_tree.heading("Reporter's ID", text = "Reporter's ID", anchor = CENTER)
    my_tree.heading("Reason", text = "Reason", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("Select complain_id, complainee_email, complainant_id, reason FROM computer_store.complain")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1

    select_button = Button(complain, text="Select Complain", command=select_complain)
    select_button.pack(pady=20)

    temp_label = Label(complain, text="")
    temp_label.pack(pady=20)

    # table = ttk.Treeview(complain,  height=8).pack()

    # review = Button(complain, font=('',12), text="Review Complain", width=7, command=self.add_data)
    # review.grid(row=0, column=4)

    # CPU_Button = Button(complain_frame, text = "CPU", width = 20, height = 3, command = viewCPU)
    # CPU_Button.config(font = ("Hevetica", 15,))
    # CPU_Button.grid(row=0, column=0, padx=0, pady=0)

def viewBids():
    def view_bid():
        print("stuff")
        
    def select_bid():
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        # temp_label.config(text=values)
        view_bid()

    bids = Tk()
    bids.title('Bids Page')
    bids.geometry('1200x500')

    label = Label(bids, text = 'Review Bids')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    table = Frame(bids)
    table.pack(pady=10)

    table_scroll = Scrollbar(table)
    table_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(table, yscrollcommand = table_scroll.set, selectmode = "extended")
    my_tree.pack()
    table_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Order ID", "Company Id", "Bid")#, "Standing Warnings")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Order ID", anchor = CENTER, width = 140)
    my_tree.column("Company Id", anchor = CENTER, width = 140)
    my_tree.column("Bid", anchor = CENTER, width = 140)
    # my_tree.column("Standing Warnings", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Order ID", text = "Order ID", anchor = CENTER)
    my_tree.heading("Company Id", text = "Company Id", anchor = CENTER)
    my_tree.heading("Bid", text = "Bid", anchor = CENTER)
    # my_tree.heading("Standing Warnings", text = "Standing Warnings", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("Select order_id, order_id, company_id, bid FROM computer_store.delivery_bids")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1

    select_button = Button(bids, text="Select Bid", command=select_bid)
    select_button.pack(pady=20)

def viewTaboo():
    def view_taboo(values):
        def delete_word(values):
            sql_query = "DELETE FROM computer_store.taboo WHERE taboo_id=" + str(values[0])
            cursor.execute(sql_query)
            con.commit()
            detail.destroy()
            taboo.destroy()
            viewTaboo()
        print(values)

        detail = Tk()
        detail.title('Taboo #' + str(values[0]))
        detail.geometry('250x100')

        select_button = Button(detail, text="Delete", command=lambda valuues=values: delete_word(values))
        select_button.pack(pady=20)

        label = Label(detail, text = 'ARE YOU SURE?')
        label.config(font = ("Hevetica", 15, "underline"))
        label.pack()
        

    def select_taboo():
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        # temp_label.config(text=values)
        view_taboo(values)

    def add_taboo():
        word = entry.get()
        entry.delete(0, 'end')
        sql_query = "INSERT INTO computer_store.taboo (word) VALUES (" + "'" + word + "')"
        cursor.execute(sql_query)
        con.commit()
        taboo.destroy()
        viewTaboo()


    taboo = Tk()
    taboo.title('Taboo Page')
    taboo.geometry('1200x500')

    label = Label(taboo, text = 'Review Taboos')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    table = Frame(taboo)
    table.pack(pady=10)

    table_scroll = Scrollbar(table)
    table_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(table, yscrollcommand = table_scroll.set, selectmode = "extended")
    my_tree.pack()
    table_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Taboo ID", "Taboo Word")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Taboo ID", anchor = CENTER, width = 140)
    my_tree.column("Taboo Word", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Taboo ID", text = "Taboo ID", anchor = CENTER)
    my_tree.heading("Taboo Word", text = "Taboo Word", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("Select taboo_id, word FROM computer_store.taboo")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
        count += 1

    select_button = Button(taboo, text="Select Taboo Word", command=select_taboo)
    select_button.pack(pady=20)

    temp_label = Label(taboo, text="")
    temp_label.pack(pady=20)

    entry = Entry(taboo)
    entry.pack()
    add_taboo_button = Button(taboo, text="Add Taboo Word", command=add_taboo, borderwidth=0, font=('Helvetica', 12)).pack()

def viewUsers():
    def view_user(values, id):
        def suspend_user(id):
            
            cursor.execute("Select email FROM registered_customers WHERE registered_id = %s", (id,))
            records = cursor.fetchall()
            for record in records:
                email = record[0]

            cursor.execute("INSERT INTO avoid_list (email)" + 
            "VALUES ('{}')".format(email,))
            con.commit()

            cursor.execute("Delete FROM registered_customers WHERE registered_id = %s",(id,))
            con.commit()




        #     sql_query = "DELETE FROM computer_store.taboo WHERE taboo_id=" + str(values[0])
        #     cursor.execute(sql_query)
        #     con.commit()
        #     detail.destroy()
        #     taboo.destroy()
        #     viewTaboo()
        # print(values)

        detail = Tk()
        detail.title('User #' + str(values[0]))
        detail.geometry('250x100')

        select_button = Button(detail, text="Suspend", command=lambda values=values: suspend_user(id))
        select_button.pack(pady=20)

        label = Label(detail, text = 'ARE YOU SURE?')
        label.config(font = ("Hevetica", 15, "underline"))
        label.pack()
        

    def select_user():
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        # temp_label.config(text=values)
        id = values[0]
        view_user(values, id)


    user = Tk()
    user.title('Users Page')
    user.geometry('1200x500')

    label = Label(user, text = 'Review Users')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    table = Frame(user)
    table.pack(pady=10)

    table_scroll = Scrollbar(table)
    table_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(table, yscrollcommand = table_scroll.set, selectmode = "extended")
    my_tree.pack()
    table_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("User ID", "User Name", "Pending Warnings", "Standing Warnings")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("User ID", anchor = CENTER, width = 140)
    my_tree.column("User Name", anchor = CENTER, width = 140)
    my_tree.column("Pending Warnings", anchor = CENTER, width = 140)
    my_tree.column("Standing Warnings", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("User ID", text = "User ID", anchor = CENTER)
    my_tree.heading("User Name", text = "User Name", anchor = CENTER)
    my_tree.heading("Pending Warnings", text = "Pending Warnings", anchor = CENTER)
    my_tree.heading("Standing Warnings", text = "Standing Warnings", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("Select registered_id, name, pending_warnings, standing_warnings FROM computer_store.registered_customers")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1

    select_button = Button(user, text="Select User", command=select_user)
    select_button.pack(pady=20)

def viewClerks():
    def view_clerk(values, id):
        def suspend_clerk(id):
            
            cursor.execute("Select email FROM store_clerk WHERE clerk_id = %s", (id,))
            records = cursor.fetchall()
            for record in records:
                email = record[0]

            cursor.execute("INSERT INTO avoid_list (email)" + 
            "VALUES ('{}')".format(email,))
            con.commit()

            cursor.execute("Delete FROM store_clerk WHERE clerk_id = %s",(id,))
            con.commit()






        #     sql_query = "DELETE FROM computer_store.taboo WHERE taboo_id=" + str(values[0])
        #     cursor.execute(sql_query)
        #     con.commit()
        #     detail.destroy()
        #     taboo.destroy()
        #     viewTaboo()
        # print(values)

        detail = Tk()
        detail.title('Clerk #' + str(values[0]))
        detail.geometry('250x100')

        select_button = Button(detail, text="Suspend", command=lambda values=values: suspend_clerk(id))
        select_button.pack(pady=20)

        label = Label(detail, text = 'ARE YOU SURE?')
        label.config(font = ("Hevetica", 15, "underline"))
        label.pack()
        

    def select_clerk():
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        # temp_label.config(text=values)
        id = values[0]
        view_clerk(values, id)


    clerk = Tk()
    clerk.title('Clerk Page')
    clerk.geometry('1200x500')

    label = Label(clerk, text = 'Review Clerks')
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

    my_tree['columns'] = ("Clerk ID", "Clerk Name", "Pending Warnings", "Standing Warnings")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Clerk ID", anchor = CENTER, width = 140)
    my_tree.column("Clerk Name", anchor = CENTER, width = 140)
    my_tree.column("Pending Warnings", anchor = CENTER, width = 140)
    my_tree.column("Standing Warnings", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Clerk ID", text = "Clerk ID", anchor = CENTER)
    my_tree.heading("Clerk Name", text = "Clerk Name", anchor = CENTER)
    my_tree.heading("Pending Warnings", text = "Pending Warnings", anchor = CENTER)
    my_tree.heading("Standing Warnings", text = "Standing Warnings", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("Select clerk_id, name, pending_warnings, standing_warnings FROM computer_store.store_clerk")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1

    select_button = Button(clerk, text="Select Clerk", command=select_clerk)
    select_button.pack(pady=20)

# id = 1
# manager_view(id)