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

def Registration_Page():

    global Register

    Register = Tk()
    Register.geometry('400x350')

    #Title of Page
    Label(Register, text="").pack()
    login_Label = Label(Register, text = "Registration")
    login_Label.pack()
    Label(Register, text="").pack()
    Label(Register, text="").pack()

    #Global Variables:
    global registerName
    global registerAddress
    global registerEmail
    global registerPassword
    global registerConfirmPassword

    global registerNameEntry
    global registerAddressEntry
    global registerEmailEntry
    global registerPasswordEntry
    global registerConfirmPasswordEntry

    #Name
    registerName = StringVar()
    registerNameLabel = Label(Register, text = "Name (First and Last)")
    registerNameLabel.pack()
    registerNameEntry = Entry(Register, textvariable = registerName)
    registerNameEntry.pack()

    #Address
    registerAddress = StringVar()
    registerAddressLabel = Label(Register, text = "Address")
    registerAddressLabel.pack()
    registerAddressEntry = Entry(Register, textvariable = registerAddress)
    registerAddressEntry.pack()
   
    #Email
    registerEmail = StringVar()
    registerEmailLabel = Label(Register, text = "Email")
    registerEmailLabel.pack()
    registerEmailEntry = Entry(Register, textvariable = registerEmail)
    registerEmailEntry.pack()

    #Password and Password Confirm
    registerPassword = StringVar()
    registerPasswordLabel = Label(Register, text = "Password")
    registerPasswordLabel.pack()
    registerPasswordEntry = Entry(Register, textvariable = registerPassword, show = '*')
    registerPasswordEntry.pack()

    registerConfirmPassword = StringVar()
    registerConfirmPasswordLabel = Label(Register, text = "Confirm Password")
    registerConfirmPasswordLabel.pack()
    registerConfirmPasswordEntry = Entry(Register, textvariable = registerConfirmPassword, show = '*')
    registerConfirmPasswordEntry.pack()

    #Button
    Button(Register, text = "Register", width = 10, height = 1, command = Register_Verfication).pack()

    Register.mainloop()

def Register_Verfication():
    
    #Store Inputted Values
    name1 = registerName.get()
    address1 = registerAddress.get()
    email1 = registerEmail.get()
    password1 = registerPassword.get()
    password2 = registerConfirmPassword.get()

    #Delete Previous Inputted Values
    registerNameEntry.delete(0, END)
    registerAddressEntry.delete(0, END)
    registerEmailEntry.delete(0, END)
    registerPasswordEntry.delete(0, END)
    registerConfirmPasswordEntry.delete(0, END)

    #Check to see if email in use
    cursor.execute("SELECT * FROM Registered_Customers WHERE email = %s", (email1,))
    data = cursor.fetchall()
    if len(data) == 0:
        cursor.execute("SELECT * FROM computer_parts_companies WHERE email = %s", (email1,))
        data = cursor.fetchall()
        if len(data) == 0:
            cursor.execute("SELECT * FROM delivery_companies WHERE email = %s", (email1,))
            data = cursor.fetchall()
            if len(data) == 0:
                cursor.execute("SELECT * FROM store_clerk WHERE email = %s", (email1,))
                data = cursor.fetchall()
                if len(data) == 0:
                    cursor.execute("SELECT * FROM store_manager WHERE email = %s", (email1,))
                    data = cursor.fetchall()
                    if len(data) == 0:
                        if password1 == password2:
                            cursor.execute("INSERT INTO registered_customers (name, email, password, address) VALUES ('{}', '{}', '{}', '{}')".format(name1, email1, password1, address1))
                            con.commit()
                            Register_Success()
                        else:
                            passwordFailed()
    else:
        emailFailed()

def emailFailed():

    #global Variable
    global emailFail

    emailFail = Tk()

    #Email Failed Message
    emailFail.title("Email Already in Use")
    emailFail.geometry("150x100")
    Label(emailFail, text = "Email Already in Use").pack()
    Button(emailFail, text = "OK", width = 10, height = 1, command = delete_emailedFailed).pack()

    emailFail.mainloop()

def passwordFailed():

    #global Variables
    global passwordFail

    passwordFail = Tk()

    passwordFail.title("Passwords do not match")
    passwordFail.geometry("150x100")
    Label(passwordFail, text = "Passwords do not match").pack()
    Button(passwordFail, text = "OK", width = 10, height = 1, command = delete_passwordFail).pack()

    passwordFail.mainloop()

def Register_Success():

    #global Variable
    global registerSuccess

    registerSuccess = Tk()

    #Register Succuess Screen
    registerSuccess.title("Registration was Successful")
    registerSuccess.geometry("150x100")
    Label(registerSuccess, text = "Registration was Successful").pack()
    Button(registerSuccess, text = "OK", width = 10, height = 1, command = delete_Register_Success).pack()

    registerSuccess.mainloop()

def delete_Register_Success():
    registerSuccess.destroy()
    Register.destroy()

def delete_emailedFailed():
    emailFail.destroy()

def delete_passwordFail():
    passwordFail.destroy()

#Registration_Page()
