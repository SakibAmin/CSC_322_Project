from Connect_DB import *
from tkinter import *
from tkinter import ttk

def manager_view(id):

    manager = Tk()
    manager.title('Manager Page')
    manager.geometry('500x450')

    cursor.execute("Select name FROM registered_customers WHERE registered_id = %s", (id,))
    data = cursor.fetchall()
    name = data[0][0]

    welcomeMessage = 'Welcome Back Manager' + name
    Title_Label = Label(manager, text = welcomeMessage)
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    Label(manager, text="").pack()
    Label(manager, text="").pack()
    Label(manager, text="").pack()

    complaints_button = Button(manager, text = "List of Complaints", width = 20, height = 3, command = viewComplaints)
    complaints_button.config(font = ("Hevetica", 15,))
    complaints_button.pack()
    
    appeals_button = Button(manager, text = "List of Appeals", width = 20, height = 3, command = viewAppeals)
    appeals_button.config(font = ("Hevetica", 15,))
    appeals_button.pack()

    manager.mainloop()

def viewComplaints():

    complain = Tk()
    complain.title('Complain Page')
    complain.geometry('600x600')

    label = Label(complain, text = 'Review Complains')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

    complain_frame = LabelFrame(complain, text="Review Complains")
    complain_frame.pack(expand="yes", padx=0, pady = 0)

    CPU_Button = Button(complain_frame, text = "CPU", width = 20, height = 3, command = viewCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.grid(row=0, column=0, padx=0, pady=0)

def viewAppeals():

    appeal = Tk()
    appeal.title('Appeal Page')
    appeal.geometry('600x600')

    label = Label(appeal, text = 'Review Appeals')
    label.config(font = ("Hevetica", 15, "underline"))
    label.pack()

    appeal_frame = LabelFrame(appeal, text="Part Type")
    appeal_frame.pack(expand="yes", padx=0, pady = 0)

    CPU_Button = Button(appeal_frame, text = "CPU", width = 20, height = 3, command = viewCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.grid(row=0, column=0, padx=0, pady=0)

id = 1
manager_view(id)