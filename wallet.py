from db_connector import get_db_connection
import tkinter as tk
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
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(q_card_info)
            return cursor.fetchall()

def card_exists(cc: Credit_Card):
    with get_db_connection() as conn:
        q_card_exists = "SELECT EXISTS(SELECT * FROM customer_funds WHERE cc_number={})".format(cc.number)
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(q_card_exists)
            does_exist = cursor.fetchone()[0]
            return does_exist

cc = Credit_Card(1234567812345678, 123, 6, 21)
# print(card_exists(cc))

def add_credit_card(cc: Credit_Card):
    with get_db_connection() as conn:
        q_add_cc = "INSERT INTO customer_funds \
                    VALUES ({}, {}, {}, {}, {}, 0)".format(customer_id, cc.number, cc.cvv, cc.exp_month, cc.exp_year)
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(q_add_cc)

def num_digits(n):
    count = 0
    while (n > 0):
        count += 1
        n //= 10
    return count

def is_expired(exp_month, exp_year):
    date_today = dt.datetime.now()
    if (2000 + exp_year >= date_today.year):
        return False
    if (exp_month >= date_today.month):
        return False
    return True



def is_valid_cc(cc: Credit_Card): # Assumes credit cards must have a 16-digit number, 3-digit cvc, and expiration month/year
    # if (not (cc.exp_month>=1 and cc.exp_month<=12)) or (not (cc.exp_year>=21 and cc.exp_year<=99)):
    #     return False
    
    return not card_exists(cc) \
           and num_digits(cc.number) == 16 \
           and num_digits(cc.cvv) == 3 \
           and not (is_expired(cc.exp_month, cc.exp_year))

def get_funds():
    with get_db_connection() as conn:
        q_get_funds = "SELECT funds FROM customer_funds \
                       WHERE customer_id={}".format(customer_id)
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(q_get_funds)
            return cursor.fetchone()[0]

def add_funds(window: tk.Tk, entry: tk.Entry):
    amount = int(entry.get())
    new_amount = amount + get_funds()
    with get_db_connection() as conn:
        q_add_funds = "UPDATE customer_funds SET funds = {} WHERE customer_id = {}".format(new_amount, customer_id)
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(q_add_funds)
            success = tk.Label(window, text="Funds have been successfully added to you account")
            success.pack()

def refresh(self: tk.Tk, gui):
    self.destroy()
    gui()

def add_funds_gui():
    window1 = tk.Tk()

    window1.title("Add Credit Card")

    window1.geometry("300x300")
    
    add = tk.Label(window1, text="Enter an amount")
    add.pack()

    enter = tk.Entry(window1, width=20, borderwidth=5)
    enter.pack()

    a = tk.Button(window1, text="Add", command=lambda: add_funds(window1, enter))
    a.pack()

    back = tk.Button(window1, text="Back", command=window1.destroy)
    back.pack()

def add_card_gui():
    window = tk.Tk()

    window.title("Add Credit Card")

    window.geometry("500x500")

    number = tk.Label(window, text="Credit Card Number (16 digits)")
    number.pack()

    enter_cc_number = tk.Entry(window, width=30, borderwidth=5)
    enter_cc_number.pack()

    cvv = tk.Label(window, text="CVV (3 digits)")
    cvv.pack()

    enter_cvv = tk.Entry(window, width=30, borderwidth=5)
    enter_cvv.pack()

    exp_month = tk.Label(window, text="Expiration Month (mm)")
    exp_month.pack()

    enter_exp_month = tk.Entry(window, width=30, borderwidth=5)
    enter_exp_month.pack()

    exp_year = tk.Label(window, text="Expiration Year (yy)")
    exp_year.pack()

    enter_exp_month = tk.Entry(window, width=30, borderwidth=5)
    enter_exp_month.pack()

    def on_click():
        cc_number = int(enter_cc_number.get())
        cvv = int(enter_cvv.get())
        exp_month = int(enter_exp_month.get())
        exp_year = int(enter_exp_month.get())

        card = Credit_Card(cc_number, cvv, exp_month, exp_year)
        if not is_valid_cc(card):
            error = tk.Label(window, text="Information entered is not valid. Please try again.")
            error.pack()
        else:
            success = tk.Label(window, text="This credit card has been successfully added to you account")
            success.pack()
            add_credit_card(card)
            
    enter_info = tk.Button(window, text="Enter Credit Card Information", command=on_click)
    enter_info.pack()

    back = tk.Button(window, text="Back", command=window.destroy)
    back.pack()




def wallet_gui():
    root = tk.Tk()
    
    root.title("Wallet")

    root.geometry("300x300")

    current_funds = tk.Label(text="Account Funds")
    current_funds.pack()

    amount = tk.Label(text=get_funds())
    amount.pack()

    add_money = tk.Button(text="Add Funds", command=add_funds_gui)
    add_money.pack()

    added_cards = tk.Label(text="Credit Cards on Account")
    added_cards.pack()

    row_num = 1
    for card in get_customer_cards():
        cc_number = card[0]
        last_four_digits = str(cc_number)[-4:]
        cc = tk.Label(text="Credit Card ending in {}".format(last_four_digits))
        cc.pack()

    add_cc = tk.Button(text="Add Card", command=add_card_gui)
    add_cc.pack()

    refresh_wallet = tk.Button(text="Refresh", command=lambda: refresh(root, wallet_gui))
    refresh_wallet.pack()

    root.mainloop()

wallet_gui()