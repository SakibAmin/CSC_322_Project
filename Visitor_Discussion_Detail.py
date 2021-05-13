from tkinter import *
from tkinter import ttk
from Connect_DB import *
import tkinter as tk
# from Logged_Home import create_logged_home, go_back_to_logged_home
# from Return_Logged import go_back_to_logged_home

def browse_discussion_detail(item_id, item_type, user_id):
    user_id = 0
    def quit_discussion_detail(user_id):
        detail.destroy()
        # go_back_to_logged_home(user_id)
    def complain_user(author_name, author_id):
        def delete_warning():
            complain.destroy()
        def deny_self():
            if author_id == CUSTOMER_ID:
                return True
            else:
                return False
        def return_reason():
            def comment_to_database(text):
                def notify_success():
                    def delete_success():
                        success.destroy()
                        complain.destroy()
                    success = Tk()
                    success.title('Write a Complain')
                    success.geometry('250x50')
                    label = Label(success, text = "Successful complain!")
                    label.pack()
                    tk.Button(success, text="Ok", command=delete_success, borderwidth=0, font=('Helvetica', 12)).pack()
                sql_query = "SELECT email FROM computer_store.registered_customers WHERE registered_id=" + str(author_id)
                cursor.execute(sql_query)
                author_email = cursor.fetchall()
                print(author_name)
                author_email = author_email[0][0]

                sql_query = "INSERT INTO computer_store.complain (complainee_email, complainant_id, reason) VALUES ('"+ author_email + "'," +  str(CUSTOMER_ID) + ","    + "'" + text + "')"
                cursor.execute(sql_query)
                con.commit()
                notify_success()


            reason_text = reason.get()
            reason.delete(0, 'end')
            print(reason_text)
            comment_to_database(reason_text)

            # add_complain(text)

        is_self_report = deny_self()
        if is_self_report:
            print("deny")
            complain = Tk()
            complain.title('Make a Complain')
            complain.geometry('250x50')
            label = Label(complain, text = "You can't complain about yourself!")
            label.pack()
            tk.Button(complain, text="Oops", command=delete_warning, borderwidth=0, font=('Helvetica', 12)).pack()
        else:
            print(CUSTOMER_ID)
            print(author_id)
            complain = Tk()
            complain.title('Make a Complain')
            complain.geometry('400x350')

            label = Label(complain, text = "Type your reason: ")
            label.pack()
            reason = Entry(complain)
            reason.pack()
            tk.Button(complain, text="Confirm", command=return_reason, borderwidth=0, font=('Helvetica', 12)).pack()
            print("complain")

    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def restart(item_id, item_type):
        detail.destroy()
        browse_discussion_detail(item_id, item_type, user_id)

    def comment_to_database(text):
        sql_query = "INSERT INTO computer_store.comment (discussion_id, registered_id, description) VALUES ("+ str(DETAIL_ID) + "," +  str(CUSTOMER_ID) + ","    +"'" + text + "')"
        cursor.execute(sql_query)
        con.commit()
        restart(item_id, item_type)

    def give_warning():
        def delete_warning():
            warning.destroy()
        print("deny")
        warning = Tk()
        warning.title('WARNING TABOO WORD')
        warning.geometry('400x50')
        label = Label(warning, text = "You have typed a taboo word, please try again.")
        label.pack()
        tk.Button(warning, text="Oops", command=delete_warning, borderwidth=0, font=('Helvetica', 12)).pack()

    def check_taboo(text, words):
        taboo_found = False
        for word in words:
            print(word)
            if (text.find(word) != -1):
                taboo_found = True
                max = 100
                star = "***"
                text = text.replace(word, star, 100)
        print(text)
        return taboo_found

    def add_comment(text):
        print("is this working?")
        sql_query = "SELECT * FROM computer_store.taboo"
        cursor.execute(sql_query)
        taboo = cursor.fetchall()
        taboo_list = []
        for data in taboo:
            taboo_list.append(data[1])
        print(taboo_list)
        check = check_taboo(text, taboo_list)
        print(check)
        if check:
            give_warning()
        else:
            comment_to_database(text)


    # def get_text(comment_box):
    #     text = comment_box.get()
    #     print(text)
    #     # add_comment(text)
    #     print(text + "HELLO")
    #     # comment_box.delete("1.0", END)
    #     print(text + "HELLO")


    def get_comments(discussion_id):
        DETAIL_ID = discussion_id
        print("grabbing discussion id" + str(discussion_id))
        sql_query = "SELECT * FROM computer_store.comment WHERE discussion_id=" + str(discussion_id)
        cursor.execute(sql_query)
        comment_data = cursor.fetchall()
        return comment_data

    def get_comment_author(registered_id):
        CUSTOMER_ID = registered_id
        sql_query = "SELECT name FROM computer_store.registered_customers WHERE registered_id=" + str(registered_id)
        cursor.execute(sql_query)
        name = cursor.fetchall()
        print(name[0][0])
        return name[0][0]

    def return_entry():
        text = entry.get()
        entry.delete(0, 'end')
        print(text)
        add_comment(text)

    def get_item_data(frame, item_id, item_type):
        print("huh?")
        sql_query = "SELECT name FROM computer_store." + item_type + " WHERE " +  item_type + "_id = " + str(item_id)
        cursor.execute(sql_query)
        item_data = cursor.fetchall()
        print(item_data)
        name = item_data[0][0]
        print(name)

        sql_query = "SELECT * FROM computer_store.discussion WHERE part_name='" + name + "'"
        cursor.execute(sql_query)
        disscussion_data = cursor.fetchall()
        print(disscussion_data)

        # SQL queries to find the discussion and comments

        item_label = Label(frame, text=name, borderwidth=1, font=('Helvetica', 60)).grid(row=0, column=1)

        comment_title_label = Label(frame, text="Comments", borderwidth=1, font=('Helvetica', 45)).grid(row=1, column=1)

        comment_author_label = Label(frame, text="ENTER YOU COMMENT BELOW!!", borderwidth=1, font=('Helvetica', 20)).grid(row=2, column=1)
        random_text = "Act civil in discussion and be nice to one another! Enjoy discussing!"
        comment_label = Label(frame, text=random_text, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=3, column=1)

        break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=4, column=1)

        discussion_id = disscussion_data[0][0]
        comment_data = get_comments(discussion_id)
        print(comment_data)

        row_num = 5
        for comment in comment_data:
            author_id = comment[2]
            author_name = get_comment_author(author_id)
            comment = comment[3]
            print(comment[2])
            print(comment[3])


            comment_author_label = Label(frame, text=author_name, borderwidth=1, font=('Helvetica', 20)).grid(row=row_num, column=1)
            row_num += 1
            comment_label = Label(frame, text=comment, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=row_num, column=1)
            row_num += 1

            break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=row_num, column=1)
            row_num += 1

        return row_num, discussion_id

    DETAIL_ID = None
    CUSTOMER_ID = user_id

    detail = Tk()
    detail.title('Discussion Detail')
    canvas = tk.Canvas(detail, height=720, width=800)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(detail, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True, anchor="center")
    canvas.create_window((4,4), window=frame, anchor="center")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    row_num, DETAIL_ID = get_item_data(frame, item_id, item_type)
    print("THIS IS A PAGE FOR" + str(DETAIL_ID))
    print(item_id, " ", item_type)



    entry = Entry(frame)
    entry.grid(row=row_num, column=1, padx=10)
    row_num += 1
    tk.Button(frame, text="Return to HOME", command=lambda id=user_id: quit_discussion_detail(user_id), borderwidth=0, font=('Helvetica', 12)).grid(row=row_num+1, column=1, padx=10)



    detail.mainloop()