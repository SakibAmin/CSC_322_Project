import tkinter as tk
from db_connector import get_db_connection

registered_id = 1


def get_delivery_name(delivery_id):
    with get_db_connection() as conn:
        q_delivery_name = "SELECT (Company_Name) FROM delivery_companies WHERE delivery_id={}".format(delivery_id)
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(q_delivery_name)
            return cursor.fetchone()[0]

root = tk.Tk()

root.title("Order History")
root.geometry("350x300")

orders = []

with get_db_connection() as conn:
    q_get_orders = "SELECT * FROM customer_orders WHERE customer_id={}".format(registered_id)
    with conn.cursor(buffered=True) as cursor:
        cursor.execute(q_get_orders)
        query = cursor.fetchall()

for q in query:
    orders.append(q)

print(orders)

order_number = tk.Label(text="Order Number")
order_number.grid(row=0, column=0)

total_price = tk.Label(text="Total Price")
total_price.grid(row=0, column=1)

status = tk.Label(text="Order Status")
status.grid(row=0, column=2)

delivery = tk.Label(text="Delivery Company")
delivery.grid(row=0, column=3)

rows = len(orders)
columns = len(orders[0]) - 1

for i in range(rows):

    number = orders[i][0]
    n = tk.Label(text=number)
    n.grid(row=i+1, column=0)

    price = orders[i][2]
    p = tk.Label(text=price)
    p.grid(row=i+1, column=1)

    status = orders[i][3]
    s = tk.Label(text=status)
    s.grid(row=i+1, column=2)

    delivery = get_delivery_name(orders[i][4])
    d = tk.Label(text=delivery)
    d.grid(row=i+1, column=3)

    


root.mainloop()