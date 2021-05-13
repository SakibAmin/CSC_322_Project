# from Delivery_Company_GUI import viewOrder
# from Computer_Part_Company_GUI import viewWallet
from Connect_DB import *
from tkinter import *
from tkinter import ttk
from Customer_Complain import *
from Buy_GUI import *

def account_view(id):
    def viewWallet(id):
        print("do something")

    def viewOrders(id):
        print("do something")

    def talkToClerk(id):
        print("do something")

    def userCart(id):
        
        viewCart(id)

    account = Tk()
    account.title('Account Page')
    account.geometry('500x450')

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

    # clerk_button = Button(manager, text = "List of Clerks", width = 20, height = 3, command = viewClerks)
    # clerk_button.config(font = ("Hevetica", 15,))
    # clerk_button.pack()

    account.mainloop()

