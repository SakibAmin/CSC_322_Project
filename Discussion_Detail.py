from tkinter import *
from tkinter import ttk
from Connect_DB import *
from Browse_Item import *
import tkinter as tk

def browse_discussion_detail(item_id, item_type):
    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def get_text():
        # text = comment_box.get()
        # comment_box.delete(1.0, END)
        text = text_box.getvar(1.0, END)
        print(text)
        text_box.delete(1.0, END)

    def get_item_data(frame, item_id, item_type):
        print("huh?")
        sql_query = "SELECT name FROM computer_store." + item_type + " WHERE " +  item_type + "_id = " + str(item_id)
        cursor.execute(sql_query)
        item_data = cursor.fetchall()
        print(item_data)

        # SQL queries to find the discussion and comments

        # sql_query = "SELECT * FROM computer_store.discussion WHERE str(item_id) = " + str(item_id)
        # cursor.execute(sql_query)
        # discussion_data = cursor.fetchall()

        # sql_query = "SELECT <comment> FROM computer_store.comments WHERE discussion_id = " + str(discussion_data[0][0])
        # cursor.execute(sql_query)
        # comment_data = cursor.fetchall()

        name = item_data[0][0]
        item_label = Label(frame, text=name, borderwidth=1, font=('Helvetica', 60)).grid(row=0, column=1)

        comment_title_label = Label(frame, text="Comments", borderwidth=1, font=('Helvetica', 45)).grid(row=1, column=1)

        # test comment 

        # retrieve comment owner & comment
        # this would be in a for loop
        comment_author_label = Label(frame, text="Made by John", borderwidth=1, font=('Helvetica', 20)).grid(row=2, column=1)
        random_text = "jadvblvnalvnalkvnavakjlvn;kvba;jvakvhba;dhvba;kdabvkahbdvaabakbkjvbadbbvbdvbdvbjwenhofiehfoiwhnofihewofihwefhwfnevnovnowvnkldsbkjvbs.dhivabldv sjbcvadhacvludvcalushvcaushcvajhsc ahjs cajhsv cahsv cahsvailcvauscvax"
        comment_label = Label(frame, text=random_text * 5, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=3, column=1)

        break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=4, column=1)

        comment_author_label = Label(frame, text="Made by John", borderwidth=1, font=('Helvetica', 20)).grid(row=5, column=1)
        random_text = "jadvblvnalvnalkvnavakjlvn;kvba;jvakvhba;dhvba;kdabvkahbdvaabakbkjvbadbbvbdvbdvbjwenhofiehfoiwhnofihewofihwefhwfnevnovnowvnkldsbkjvbs.dhivabldv sjbcvadhacvludvcalushvcaushcvajhsc ahjs cajhsv cahsv cahsvailcvauscvax"
        comment_label = Label(frame, text=random_text * 5, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=6, column=1)

        break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=7, column=1)

        comment_author_label = Label(frame, text="Made by John", borderwidth=1, font=('Helvetica', 20)).grid(row=8, column=1)
        random_text = "jadvblvnalvnalkvnavakjlvn;kvba;jvakvhba;dhvba;kdabvkahbdvaabakbkjvbadbbvbdvbdvbjwenhofiehfoiwhnofihewofihwefhwfnevnovnowvnkldsbkjvbs.dhivabldv sjbcvadhacvludvcalushvcaushcvajhsc ahjs cajhsv cahsv cahsvailcvauscvax"
        comment_label = Label(frame, text=random_text * 5, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=9, column=1)

        break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=10, column=1)

        # comment_box = tk.Entry(root)
        comment_box = Text(frame, height=10, width=60).grid(row=11, column=1)
        # comment_canvas = tk.Canvas(frame, height=480, width=500, borderwidth=0)
        # comment_canvas.create_window(0,0, window=comment_box)
        # comment_canvas.grid(row=11, column=1)

        text = ""
        # tk.Button(frame, text="Post Comment", command=lambda comment_box=comment_box: get_text(comment_box), borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)
        # tk.Button(frame, text="Post Comment", command=get_text, borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)

        # print(text)

        # break_label = Label(frame, text=" " * 3000, borderwidth=1, font=('Helvetica', 15), wraplength=500).grid(row=13, column=1)

    root = Tk()
    root.title('Discussion Detail')
    canvas = tk.Canvas(root, height=720, width=1280)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    get_item_data(frame, item_id, item_type)
    print(item_id, " ", item_type)

    text_box = Text(frame, height=10, width=60)
    tk.Button(frame, text="Post Comment", command=get_text, borderwidth=0, font=('Helvetica', 12)).grid(row=12, column=1, padx=10)

    root.mainloop()