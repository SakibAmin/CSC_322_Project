import tkinter as tk
from db_connector import get_db_connection

delivery_id=1

''' atempting to rewrite delivery_company_gui.py'''

def get_orders():
    orders = []
    with get_db_connection() as conn:
        q_get_orders = "SELECT order_id FROM customer_orders"
        with conn.cursor() as cursor:
            cursor.execute(q_get_orders)
            orders = cursor.fetchall()
    return orders

def get_bid_entries(bid_entries: list):
    bids = []

    for entry in bid_entries:
        bids.append(entry.get())
    
    return bids

def insert_bids(orders: list, bids: list):
    with get_db_connection() as conn:
        n = len(orders)
        for i in range(n):
            q_set_bid = "INSERT INTO delivery_bids VALUES ({}, {}, {})".format(orders[i][0], delivery_id, bids[i])
            with conn.cursor() as cursor:
                cursor.execute(q_set_bid)


def display_orders(orders: list):
    root = tk.Tk()

    root.title("Orders Available to Bid")

    root.geometry("300x300")

    order_id = tk.Label(text="Order Number")
    order_id.grid(row=0, column=0)

    bid = tk.Label(text="Bid")
    bid.grid(row=0, column=1)

    num_rows = len(orders)
    num_columns = len(orders[0])

    bid_entries = []

    for i in range(num_rows):
        for j in range(num_columns):

            d = tk.Label(root, text=orders[i][j])
            d.grid(row=i+1, column=j)

        bid_entry = tk.Entry(root, width=10, borderwidth=5)
        bid_entry.grid(row=i+1, column=j+1)
        bid_entries.append(bid_entry)

    enter_bid = tk.Button(root, text="Enter Bid(s)", command=insert_bids(orders, bid_entries))
    enter_bid.grid(row=num_rows+1, column=num_columns)

    root.mainloop()

display_orders(get_orders())