from tkinter import *
from tkinter import ttk
from Connect_DB import *
from Browse_Item import *
import tkinter as tk

def browse_discussion_detail(item_id, item_type):
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
                sql_query = "SELECT name FROM computer_store.registered_customers WHERE registered_id=" + str(author_id)
                cursor.execute(sql_query)
                author_name = cursor.fetchall()
                print(author_name)
                author_name = author_name[0][0]

                sql_query = "INSERT INTO computer_store.complain (complainee_name, complainant_id, reason) VALUES ('"+ author_name + "'," +  str(CUSTOMER_ID) + ","    + "'" + text + "')"
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
        root.destroy()
        browse_discussion_detail(item_id, item_type)

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

        # sql_query = "SELECT * FROM computer_store.discussion WHERE str(item_id) = " + str(item_id)
        # cursor.execute(sql_query)
        # discussion_data = cursor.fetchall()

        # sql_query = "SELECT <comment> FROM computer_store.comments WHERE discussion_id = " + str(discussion_data[0][0])
        # cursor.execute(sql_query)
        # comment_data = cursor.fetchall()

        # name = item_data[0][0]
        item_label = Label(frame, text=name, borderwidth=1, font=('Helvetica', 60)).grid(row=0, column=1)

        comment_title_label = Label(frame, text="Comments", borderwidth=1, font=('Helvetica', 45)).grid(row=1, column=1)

        # test comment 

        # retrieve comment owner & comment
        # this would be in a for loop
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

            # name_and_complain_frame = Frame(frame).grid(row=row_num, column=1)
            # comment_author_label = Label(name_and_complain_frame, text=author_name, borderwidth=1, font=('Helvetica', 20)).pack()
            # report_button = Button(name_and_complain_frame, text="Complain", command=complain_user, borderwidth=0, font=('Helvetica', 12)).pack()
            comment_author_label = Label(frame, text=author_name, borderwidth=1, font=('Helvetica', 20)).grid(row=row_num, column=1)
            # report_button = Button(frame, text="Complain", command=complain_user, borderwidth=0, font=('Helvetica', 12)).grid(row=row_num, column=2, padx=10)
            row_num += 1
            comment_label = Label(frame, text=comment, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=row_num, column=1)
            row_num += 1
            report_button = Button(frame, text="Complain", command=lambda author_name=author_name, author_id=author_id: complain_user(author_name, author_id), borderwidth=0, font=('Helvetica', 12)).grid(row=row_num, column=1)
            row_num += 1
            break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=row_num, column=1)
            row_num += 1

        return row_num, discussion_id
        # comment_author_label = Label(frame, text="Made by John", borderwidth=1, font=('Helvetica', 20)).grid(row=5, column=1)
        # random_text = "jadvblvnalvnalkvnavakjlvn;kvba;jvakvhba;dhvba;kdabvkahbdvaabakbkjvbadbbvbdvbdvbjwenhofiehfoiwhnofihewofihwefhwfnevnovnowvnkldsbkjvbs.dhivabldv sjbcvadhacvludvcalushvcaushcvajhsc ahjs cajhsv cahsv cahsvailcvauscvax"
        # comment_label = Label(frame, text=random_text * 5, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=6, column=1)

        # break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=7, column=1)

        # comment_author_label = Label(frame, text="Made by John", borderwidth=1, font=('Helvetica', 20)).grid(row=8, column=1)
        # random_text = "jadvblvnalvnalkvnavakjlvn;kvba;jvakvhba;dhvba;kdabvkahbdvaabakbkjvbadbbvbdvbdvbjwenhofiehfoiwhnofihewofihwefhwfnevnovnowvnkldsbkjvbs.dhivabldv sjbcvadhacvludvcalushvcaushcvajhsc ahjs cajhsv cahsv cahsvailcvauscvax"
        # comment_label = Label(frame, text=random_text * 5, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=9, column=1)

        # break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=10, column=1)

        # comment_box = tk.Entry(root)
        # comment_box = Text(frame, height=10, width=60).grid(row=11, column=1)
        # comment_canvas = tk.Canvas(frame, height=480, width=500, borderwidth=0)
        # comment_canvas.create_window(0,0, window=comment_box)
        # comment_canvas.grid(row=11, column=1)

        # text = ""
        # tk.Button(frame, text="Post Comment", command=lambda comment_box=comment_box: get_text(comment_box), borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)
        # tk.Button(frame, text="Post Comment", command=get_text, borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)

        # print(text)

        # break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=13, column=1)

    # sql_query = "SELECT name FROM computer_store." + item_type + " WHERE " +  item_type + "_id = " + str(item_id)
    # cursor.execute(sql_query)
    # item_data = cursor.fetchall()
    # name = item_data[0][0]

    # sql_query = "SELECT * FROM computer_store.discussion WHERE part_name='" + name + "'"
    # cursor.execute(sql_query)
    # discussion_data = cursor.fetchall()
    DETAIL_ID = None
    CUSTOMER_ID = 2

    root = Tk()
    root.title('Discussion Detail')
    canvas = tk.Canvas(root, height=720, width=800)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True, anchor="center")
    canvas.create_window((4,4), window=frame, anchor="center")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    row_num, DETAIL_ID = get_item_data(frame, item_id, item_type)
    print("THIS IS A PAGE FOR" + str(DETAIL_ID))
    print(item_id, " ", item_type)

    # text_box = Text(frame, height=10, width=60)
    # text_box.bind('<Return>', get_text)
    # tk.Button(frame, text="Post Comment", command=lambda text_box=text_box: get_text(text_box), borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)
 ##########


    # entry = Entry(master)
    # entry.grid(row=0, column=1)

    # # Connect the entry with the return button
    # entry.bind('<Return>', return_entry) 


    # txtbox = Entry(frame)
    # txtbox.grid(row=13, column=1, padx=10)
    # tk.Button(frame, text="Post Comment", command=get_text, borderwidth=0, font=('Helvetica', 12)).grid(row=14, column=1, padx=10)

    entry = Entry(frame)
    entry.grid(row=row_num, column=1, padx=10)
    row_num += 1
    tk.Button(frame, text="Post Comment", command=return_entry, borderwidth=0, font=('Helvetica', 12)).grid(row=row_num, column=1, padx=10)

    # entry.bind('<Return>', return_entry) 

    # comment_box = Text(frame, height=10, width=60).grid(row=11, column=1)
    # tk.Button(frame, text="Post Comment", command=lambda comment_box=comment_box: get_text(comment_box), borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)


    root.mainloop()