
import tkinter as tk
from db_connector import get_db_connection

registered_id = 1
    

def display_account_page(registered_id):
    window = tk.Tk()

    window.title("Account")

    window.geometry("300x300")

    name, email, address = get_customer_info(registered_id)

    title = tk.Label(text="Account Information")
    title.grid(column=1, row=0)

    account_name = tk.Label(text=name)
    account_name.grid(column=1, row=1)

    account_email = tk.Label(text="Email Address: "+email)
    account_email.grid(column=1, row=2)

    shipping_address = tk.Label(text="Shipping Address: "+address)
    shipping_address.grid(column=1, row=3)

    button = tk.Button(text="Back to Home", command=window.destroy)
    button.grid(column=0, row=0)

    window.mainloop()

def get_customer_info(registered_id): # later implement with db connection passed in as parameter

    with get_db_connection() as conn:
        q_customer_info = "SELECT name, email, address FROM registered_customers WHERE registered_id={}".format(registered_id)
        with conn.cursor() as cursor:
            cursor.execute(q_customer_info)
            return cursor.fetchone()
                       
    
display_account_page(registered_id)