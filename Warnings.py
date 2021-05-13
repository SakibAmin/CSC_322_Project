from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connect_DB import *

def subtract_pending_warning(id, user_type):
    id_prefix = None
    if user_type == "registered_customers":
        id_prefix = "registered"
    elif user_type == "store_clerk":
        id_prefix = "clerk"
    elif user_type == "delivery_companies":
        id_prefix = "delivery"
    elif user_type == "computer_parts_companies":
        id_prefix = "company"

    sql_query = "UPDATE computer_store."+ user_type + " SET pending_warnings = pending_warnings - 1 WHERE "+ id_prefix + "_id=" +  str(id)
    cursor.execute(sql_query)
    con.commit()

def add_pending_warning(id, user_type):
    id_prefix = None
    if user_type == "registered_customers":
        id_prefix = "registered"
    elif user_type == "store_clerk":
        id_prefix = "clerk"
    elif user_type == "delivery_companies":
        id_prefix = "delivery"
    elif user_type == "computer_parts_companies":
        id_prefix = "company"

    sql_query = "UPDATE computer_store."+ user_type + " SET pending_warnings = pending_warnings + 1 WHERE "+ id_prefix + "_id=" +  str(id)
    cursor.execute(sql_query)
    con.commit()

def add_standing_warning(id, user_type):
    id_prefix = None
    if user_type == "registered_customers":
        id_prefix = "registered"
    elif user_type == "store_clerk":
        id_prefix = "clerk"
    elif user_type == "delivery_companies":
        id_prefix = "delivery"
    elif user_type == "computer_parts_companies":
        id_prefix = "company"

    sql_query = "UPDATE computer_store."+ user_type + " SET standing_warnings = standing_warnings + 1 WHERE "+ id_prefix + "_id=" +  str(id)
    cursor.execute(sql_query)
    con.commit()

def suspend(id, user_type):
    id_prefix = None
    if user_type == "registered_customers":
        id_prefix = "registered"
    elif user_type == "store_clerk":
        id_prefix = "clerk"
    elif user_type == "delivery_companies":
        id_prefix = "delivery"
    elif user_type == "computer_parts_companies":
        id_prefix = "company"

    sql_query = "SELECT email FROM computer_store."+ user_type + " WHERE " + id_prefix + "_id=" + str(id)
    cursor.execute(sql_query)
    email = cursor.fetchall()
    email = email[0][0]

    sql_query = "INSERT INTO computer_store.avoid_list VALUE ("+ id + ", " + email + ", '3 warnings or by manager')"
    cursor.execute(sql_query)
    con.commit()

    sql_query = "DELETE FROM FROM computer_store."+ user_type + " WHERE " + id_prefix + "_id=" + str(id)
    cursor.execute(sql_query)
    con.commit()

def on_logout_standing_warnings(id, user_type):
    id_prefix = "registered"
    sql_query = "SELECT standing_warnings FROM computer_store."+ user_type + " WHERE "+ id_prefix + "_id=" +  str(id)
    cursor.execute(sql_query)
    warnings = cursor.fetchall()
    if warnings[0][0] == 100:
        suspend(id, user_type)

def check_standing_warnings_no_customers(id, user_type):
    id_prefix = None
    if user_type == "registered_customers":
        id_prefix = "registered"
    elif user_type == "store_clerk":
        id_prefix = "clerk"
    elif user_type == "delivery_companies":
        id_prefix = "delivery"
    elif user_type == "computer_parts_companies":
        id_prefix = "company"
    
    sql_query = "SELECT standing_warnings FROM computer_store."+ user_type + " WHERE "+ id_prefix + "_id=" +  str(id)
    cursor.execute(sql_query)
    warnings = cursor.fetchall()
    if (user_type == "registered_customers") and (warnings[0][0] >= 3):
        messagebox.showwarning("Last Chance","Warning, this is your last chance to do anything before you are suspended.")
        sql_query = "UPDATE computer_store."+ user_type + " SET standing_warnings = 100 WHERE "+ id_prefix + "_id=" +  str(id)
        cursor.execute(sql_query)
        con.commit()
    elif warnings[0][0] >= 3:
        suspend(id, user_type)