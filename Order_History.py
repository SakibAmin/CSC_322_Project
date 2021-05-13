import tkinter as tk
# from Connect_DB import *
from db_connector import get_db_connection


def make_order_history(registered_id):
    def get_delivery_name(delivery_id):
        with get_db_connection() as connn:
            q_delivery_name = "SELECT (Company_Name) FROM delivery_companies WHERE delivery_id={}".format(delivery_id)
            with connn.cursor(buffered=True) as cursorr:
                cursorr.execute(q_delivery_name)
                return cursorr.fetchone()[0]

    root = tk.Tk()

    root.title("Order History")
    root.geometry("350x300")

    orders = []

    with get_db_connection() as connn:
        q_get_orders = "SELECT * FROM customer_orders WHERE customer_id={}".format(registered_id)
        with connn.cursor(buffered=True) as cursorr:
            cursorr.execute(q_get_orders)
            query = cursorr.fetchall()

    for q in query:
        orders.append(q)

    print(orders)

    order_number = tk.Label(root,text="Order Number")
    order_number.grid(row=0, column=0)

    total_price = tk.Label(root,text="Total Price")
    total_price.grid(row=0, column=1)

    status = tk.Label(root,text="Order Status")
    status.grid(row=0, column=2)

    delivery = tk.Label(root,text="Delivery Company")
    delivery.grid(row=0, column=3)

    rows = len(orders)
    columns = len(orders[0]) - 1

    for i in range(rows):

        number = orders[i][0]
        n = tk.Label(root,text=number)
        n.grid(row=i+1, column=0)

        price = orders[i][2]
        p = tk.Label(root,text=price)
        p.grid(row=i+1, column=1)

        status = orders[i][3]
        s = tk.Label(root,text=status)
        s.grid(row=i+1, column=2)

        delivery = get_delivery_name(orders[i][4])
        d = tk.Label(root,text=delivery)
        d.grid(row=i+1, column=3)

        


    root.mainloop()