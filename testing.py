from mysql.connector import connect, Error
import tkinter as tk
from user_account import display_account_page

registered_id = 1

root = tk.Tk()

root.title("Account")

root.geometry("1280x720")

test = tk.Label(text="test")
test.grid()

button = tk.Button(test="click me", command=display_account_page(registered_id))
button.grid()

root.mainloop()