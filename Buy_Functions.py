from tkinter import *
from tkinter import ttk
import mysql.connector
import os

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "user",
        password = "password",
        database = "computer_store",
        port = 3306
)

#print ("Connnected To Database")
cursor = con.cursor()


def addtoCart(item):
    print("Work in Progress")