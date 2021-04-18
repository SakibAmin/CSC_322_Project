import mysql.connector
from tkinter import *
import os

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
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
    Button(Login, text = "Login", width = 10, height = 1, command = Login_Verfication).pack()

    Login.mainloop()

def Login_Verfication(): #Logs users into the database
    email1 = login_email.get()
    password1 = login_password.get()
    emailEntry.delete(0, END)
    passwordEntry.delete(0, END)
    cursor.execute("SELECT * FROM Registered_Customers WHERE email = %s AND password = %s", (email1, password1))
    #print(username1), print(password1)
    result = cursor.fetchall()
    count = cursor.rowcount
    if count == 1:
        #print("Login Successful")
        Login_Successful() 
    else:
        #print("Email or Password is Incorrect")
        Login_Failed()
        

    #Delete Previous Entries
   

def Login_Successful(): #Tells user the login was successful
    
    #global Variable
    global loginSuccess

    loginSuccess = Tk()

    #Login Success Screen
    loginSuccess.title("Login was Successful")
    loginSuccess.geometry("150x100")
    Label(loginSuccess, text = "Login was Successful").pack()
    Button(loginSuccess, text = "OK", width = 10, height = 1, command = delete_Login_Successful).pack()

    loginSuccess.mainloop()

def delete_Login_Successful(): #deletes the success screen
    loginSuccess.destroy()
    Login.destroy()

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
    

Login_Page()
con.close()