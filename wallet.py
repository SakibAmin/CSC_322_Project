from db_connector import get_db_connection
import tkinter as tk
from collections import namedtuple
import datetime as dt


customer_id = 1


class Credit_Card:
    def __init__(self, number, cvv, exp_month, exp_year):
        self.number = number
        self.cvv = cvv
        self.exp_month = exp_month
        self.exp_year = exp_year

def get_customer_cards():
    with get_db_connection() as conn:
        q_card_info = "SELECT cc_number \
                       FROM customer_funds WHERE customer_id={}".format(customer_id)
        with conn.cursor() as cursor:
            cursor.execute(q_card_info)
            return cursor.fetchall()

def add_credit_card(cc: Credit_Card):
    with get_db_connection() as conn:
        q_add_cc = "INSERT INTO customer_funds \
                    VALUES ({}, {}, {}, {}, {}, 0)".format(customer_id, cc.number, cc.cvv, cc.exp_month, cc.exp_year)
        with conn.cursor() as cursor:
            cursor.execute(q_add_cc)

def num_digits(n):
    count = 0
    while (n > 0):
        count += 1
        n //= 10
    return count

print(num_digits(12345678))

def is_expired(exp_month, exp_year):
    date_today = dt.datetime.now()
    if (2000 + exp_year >= date_today.year):
        return False
    if (exp_month >= date_today.month):
        return False
    return True


def is_valid_cc(cc: Credit_Card): # Assumes credit cards must have a 16-digit number, 3-digit cvc, and expiration month/year
    return num_digits(cc.number) == 16 \
            and num_digits(cc.cvv) == 3 \
            and not (is_expired(cc.exp_month, cc.exp_year))

def add_funds():
    pass


def add_card_gui():
    window = tk.Tk()

    window.title("Add Credit Card")

    window.geometry("500x500")

    number = tk.Label(window, text="Credit Card Number (16 digits)")
    number.grid(column=0, row=0)

    enter_cc_number = tk.Entry(window, width=30, borderwidth=5)
    enter_cc_number.grid(column=1, row=0)

    cvv = tk.Label(window, text="CVV (3 digits)")
    cvv.grid(column=0, row=1)

    enter_cvv = tk.Entry(window, width=30, borderwidth=5)
    enter_cvv.grid(column=1, row=1)


    exp_month = tk.Label(window, text="Expiration Month")
    exp_month.grid(column=0, row=2) 

    enter_exp_month = tk.Entry(window, width=30, borderwidth=5)
    enter_exp_month.grid(column=1, row=2)

    exp_year = tk.Label(window, text="Expiration Year")
    exp_year.grid(column=0, row=3) 

    enter_exp_month = tk.Entry(window, width=30, borderwidth=5)
    enter_exp_month.grid(column=1, row=3)

    def on_click():
        cc_number = int(enter_cc_number.get())
        cvv = int(enter_cvv.get())
        exp_month = int(enter_exp_month.get())
        exp_year = int(enter_exp_month.get())

        card = Credit_Card(cc_number, cvv, exp_month, exp_year)
        if not is_valid_cc(card):
            error = tk.Label(window, text="Information entered is not valid. Please try again.")
            error.grid(column=0, row=5)
        else:
            success = tk.Label(window, text="This credit card has been successfully added to you account")
            success.grid(column=0, row=5)
            add_credit_card(card)
    
    enter_info = tk.Button(window, text="Enter Credit Card Information", command=on_click)
    enter_info.grid(column=0, row=4)




def wallet_gui():
    root = tk.Tk()
    
    root.title("Wallet")

    root.geometry("300x300")

    added_cards = tk.Label(text="Credit Cards on Account")
    added_cards.grid(column=0, row=0)

    row_num = 1
    for card in get_customer_cards():
        cc_number = card[0]
        last_four_digits = str(cc_number)[-4:]
        cc = tk.Label(text="Credit Card ending in {}".format(last_four_digits))
        cc.grid(column=0, row=1)
    
    add_cc = tk.Button(text="Add Card", command=add_card_gui)
    add_cc.grid(column=1, row=0)

    root.mainloop()

wallet_gui()