from tkinter import *
from tkinter import ttk
from Connect_DB import *

def browse_all_complains(USER_ID):
    def view_complain(data):
        def deny_self():
            sql_query = "SELECT * FROM computer_store.appeal WHERE complain_id=" + str(data[0])
            cursor.execute(sql_query)
            if cursor.rowcount == 0:
                return False
            else:
                return True
        def appealComplain():
            def delete_warning():
                appeal.destroy()

            def return_reason():
                def appeal_to_database(text):
                    def notify_success():
                        def delete_success():
                            success.destroy()
                            appeal.destroy()
                        success = Tk()
                        success.title('Write an Appeal')
                        success.geometry('250x50')
                        label = Label(success, text = "Successful appeal!")
                        label.pack()
                        Button(success, text="Ok", command=delete_success, borderwidth=0, font=('Helvetica', 12)).pack()
                    sql_query = "SELECT name FROM computer_store.registered_customers WHERE registered_id=" + str(USER_ID)
                    cursor.execute(sql_query)
                    author_name = cursor.fetchall()
                    print(author_name)
                    author_name = author_name[0][0]

                    sql_query = "INSERT INTO computer_store.appeal (complain_id, reason) VALUES ("+ str(data[0]) + ",'" + text + "')"
                    cursor.execute(sql_query)
                    con.commit()
                    notify_success()

                reason_text = reason.get()
                reason.delete(0, 'end')
                print(reason_text)
                appeal_to_database(reason_text)
                print("create appeal")

            appeal_already_made = deny_self()
            if appeal_already_made:
                print("deny")
                appeal = Tk()
                appeal.title('Make a appeal')
                appeal.geometry('250x50')
                label = Label(appeal, text = "You already made an appeal!")
                label.pack()
                Button(appeal, text="Oops", command=delete_warning, borderwidth=0, font=('Helvetica', 12)).pack()
            else:
                appeal = Tk()
                appeal.title('Make an Appeal')
                appeal.geometry('400x350')

                label = Label(appeal, text = "Type your reason: ")
                label.pack()
                reason = Entry(appeal)
                reason.pack()
                Button(appeal, text="Confirm", command=return_reason, borderwidth=0, font=('Helvetica', 12)).pack()
                print("appeal")

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
        reason_label = Label(leftFrame, text="Reason: ", font=("Hevetica", 20)).grid(row=2, column=0)
        reason_description_label = Label(leftFrame, text=data[3], font=("Hevetica", 20)).grid(row=2, column=1)

        appeal_button = Button(detail, text = "Appeal Complain", width = 20, height = 3, command = appealComplain)
        appeal_button.config(font = ("Hevetica", 15,))
        appeal_button.pack()

    def select_complain():
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        view_complain(values)

    sql_query = "SELECT * FROM computer_store.registered_customers WHERE registered_id=" + str(USER_ID)
    cursor.execute(sql_query)
    customer_data = cursor.fetchall()
    print(customer_data)
    print(customer_data[0][1])

    complain = Tk()
    complain.title('Complain Page')
    complain.geometry('1200x500')

    label = Label(complain, text = 'Review Complains')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

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

    cursor.execute("Select complain_id, complainee_email, complainant_id, reason FROM computer_store.complain WHERE complainee_email='" + customer_data[0][2] + "'")
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

    complain.mainloop()

id = 1
browse_all_complains(id)