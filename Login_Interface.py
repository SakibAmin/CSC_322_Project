from Logged_Home import create_logged_home
from Manager_GUI import manager_view
import mysql.connector
from tkinter import *
import os
import PIL.Image
import PIL.ImageTk
# from Registered_GUI import *
from Computer_Part_Company_GUI import *
from Registration_Interface import *
from Browsing_GUI import *
from Computer_Part_Company_GUI import *
from Delivery_Company_GUI import *
from Store_Clerk_GUI import *
from Manager_GUI import *
from Visitor_Home import *
from Logged_Home import *

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)
#print ("Connnected To Database")
cursor = con.cursor()

def Login_Page(): #Login Screen

    global Login

    Login = Tk()
    Login.geometry('300x250')

    #Title of Page
    Label(Login, text="").pack()
    login_Label = Label(Login, text = "Sign In")
    login_Label.pack()
    Label(Login, text="").pack()
    Label(Login, text="").pack()
    Label(Login, text="").pack()

    global login_email
    global login_password

    global emailEntry
    global passwordEntry

    #Username
    login_email = StringVar()
    emailLabel = Label(Login, text = "Email")
    emailLabel.pack()
    emailEntry = Entry(Login, textvariable = login_email)
    emailEntry.pack()

    #Password
    login_password = StringVar()
    passwordLabel = Label(Login, text = "Password")
    passwordLabel.pack()
    passwordEntry = Entry(Login, textvariable = login_password, show = '*')
    passwordEntry.pack()

    #Login Button

    Label(Login, text="").pack()
    Button(Login, text = "Login", width = 10, height = 1, command = Login_Verfication).pack()

    Button_Frame = LabelFrame(Login)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def register(): 

        Login.destroy()
        Registration_Page()
        
    def browse():

        Login.destroy()
        browsing_GUI()
        
    Button(Button_Frame, text = "Register", width = 10, height = 1, command = register).grid(row=0, column=0, padx=0, pady=0)
    Button(Button_Frame, text = "Browse", width = 10, height = 1, command = browse).grid(row=0, column=1, padx=0, pady=0)

    Login.mainloop()

def Login_Verfication(): #Logs users into the database
    
    #Store Inputted Values
    email1 = login_email.get()
    password1 = login_password.get()

    #Delete Previous Inputted Values
    emailEntry.delete(0, END)
    passwordEntry.delete(0, END)

    cursor.execute("SELECT * FROM registered_customers WHERE email = %s AND password = %s", (email1, password1))
    #print(username1), print(password1)
    records = cursor.fetchall()
    count = cursor.rowcount
    #print(count)
    global id
    if count == 0:
        cursor.execute("SELECT * FROM computer_parts_companies WHERE email = %s AND password = %s", (email1, password1))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 0:
            cursor.execute("SELECT * FROM delivery_companies WHERE email = %s AND password = %s", (email1, password1))
            records = cursor.fetchall()
            count = cursor.rowcount
            if count == 0:
                cursor.execute("SELECT * FROM store_clerk WHERE email = %s AND password = %s", (email1, password1))
                records = cursor.fetchall()
                count = cursor.rowcount
                if count == 0:
                    cursor.execute("SELECT * FROM store_manager WHERE email = %s AND password = %s", (email1, password1))
                    records = cursor.fetchall()
                    count = cursor.rowcount
                    if count == 1:
                        print("You are good")
                        for record in records:
                            id = record[0]
                            #print(id)
                        #Add the store manager GUI
                        '''
                        Things a store manager GUI needs:

                            A way to view complaints from registered customers on clerks, parts, and delivery companies
                                This system should be able to view these messages and then provide a way to give punishments
                            A way to view appeals from clerks, parts, and delivery companies
                            A way to view complaints on disscussion fourms and allow the manager to make the proper corrections or punishments
                        '''
                        manager_view(id)
                    else:
                        Login_Failed()  
                elif count == 1:
                    print("You are good")
                    for record in records:
                        id = record[0]
                        warning = record[5]
                        #print(id)
                        if warning == 3:
                            clerkBanned()
                        else:
                            Clerk_GUI(id)
                    #Add the store clerk GUI 
                    '''
                    Things a store clerk GUI needs:

                        A way to see the bidding system and select which company will be doing the delivery service. Will also provide justification
                        A appeal system where u can provide justification to the complaint recieved
                    '''
            elif count == 1:
                print("You are good")
                for record in records:
                    id = record[0]
                    warning = record[5]
                    #print(id)
                if warning == 3:
                    deliveryBanned()
                else:
                    Delivery_GUI(id)
                #Add the delivery company GUI
                '''
                Things a delivery company GUI needs:

                    Bidding System where they can place bids on orders
                    A appeal system where u can provide justification to the complaint recieved
                '''
        elif count == 1:
            print("You are good")
            for record in records:
                id = record[0]
                warning = record[5]
                #print(id)
            if warning == 3:
                cpcBanned()
            else:
                CPC_GUI(id)
                #Login.destroy()
            #Add the computer part company GUI
            '''
            Things Computer Part Company GUI needs:

                List of Products they are selling and how much of it has sold
                Add Parts System
                Wallet to see how much money they have earned
                A appeal system where u can provide justification to the complaint recieved
            '''
    elif count == 1:
        #print("Login Successful")
        for record in records:
            id = record[0]
            warning = record[6]
            #print(id)
            #print(warning)
        if warning == 3:
            registeredBanned()
        else:
            Login_Successful(id)

def Login_Successful(id): #Tells user the login was successful
    
    #global Variable
    global loginSuccess
    loginSuccess = Tk()

    #Login Success Screen
    loginSuccess.title("Login was Successful")
    loginSuccess.geometry("150x100")
    Label(loginSuccess, text = "Login was Successful").pack()
    Button(loginSuccess, text = "OK", width = 10, height = 1, command = lambda id=id: delete_Login_Successful(id)).pack()

    loginSuccess.mainloop()

def delete_Login_Successful(id): #deletes the success screen
    loginSuccess.destroy()
    Login.destroy()
    create_logged_home(id)

def Login_Failed(): #Tells user wrong password or username was entered
    #global Variable
    global loginFail

    loginFail = Tk()

    #Login Success Screen
    loginFail.title("Username or Password is Incorrect")
    loginFail.geometry("200x100")
    Label(loginFail, text = "Username or Password is Incorrect").pack()
    Button(loginFail, text = "Try Again", width = 10, height = 1, command = delete_Login_Failed).pack()

    loginFail.mainloop()

def delete_Login_Failed(): #deletes fail screen and sends back to user Login Page
    loginFail.destroy()

def registeredBanned():

    ban = Tk()
    ban.geometry('200x200')

    Ban_Label = Label(ban, text = "Your account has been BANNNED!!!! ")
    Ban_Label.config(font = ("Hevetica", 10, ))
    Ban_Label.pack()


    def removeFunds():
        zero = 0
        cursor.execute("Update customer_funds SET funds = %s WHERE customer_id = %s",(zero, id))
        con.commit()
        zero_Label = Label(ban, text = "Funds have been removed")
        zero_Label.config(font = ("Hevetica", 10, ))
        zero_Label.pack()
        ban.destroy()

    oMoney_Button = Button(ban, text = "Remove Funds", width = 5, command = removeFunds)
    oMoney_Button.config(font = ("Hevetica", 15,))
    oMoney_Button.pack()

def cpcBanned():

    ban = Tk()
    ban.geometry('200x200')

    Ban_Label = Label(ban, text = "Your account has been BANNNED!!!! ")
    Ban_Label.config(font = ("Hevetica", 10, ))
    Ban_Label.pack()


    def removeFunds():
        zero = 0
        cursor.execute("Update computer_parts_companies SET funds = %s WHERE company_id = %s",(zero, id))
        con.commit()
        zero_Label = Label(ban, text = "Funds have been removed")
        zero_Label.config(font = ("Hevetica", 10, ))
        zero_Label.pack()
        ban.destroy()

    oMoney_Button = Button(ban, text = "Remove Funds", width = 5, command = removeFunds)
    oMoney_Button.config(font = ("Hevetica", 15,))
    oMoney_Button.pack()

def deliveryBanned():

    ban = Tk()
    ban.geometry('200x200')

    Ban_Label = Label(ban, text = "Your account has been BANNNED!!!! ")
    Ban_Label.config(font = ("Hevetica", 10, ))
    Ban_Label.pack()

    def close():
        ban.destroy()

    oMoney_Button = Button(ban, text = "Ok", width = 5, command = close)
    oMoney_Button.config(font = ("Hevetica", 15,))
    oMoney_Button.pack()

def clerkBanned():

    ban = Tk()
    ban.geometry('200x200')

    Ban_Label = Label(ban, text = "Your account has been BANNNED!!!! ")
    Ban_Label.config(font = ("Hevetica", 10, ))
    Ban_Label.pack()

    def close():
        ban.destroy()

    oMoney_Button = Button(ban, text = "Ok", width = 5, command = close)
    oMoney_Button.config(font = ("Hevetica", 15,))
    oMoney_Button.pack()

id = 0
