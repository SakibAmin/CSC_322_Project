import mysql.connector
from tkinter import *
from tkinter import ttk
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

def CPC_GUI(id):

    cpc = Tk()
    cpc.geometry('500x450')

    #Title Label
    cursor.execute("Select company_name FROM computer_parts_companies WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    for record in records:
        name = record[0]
    #We will be getting info from login about the id 
    welcomeMessage = 'Welcome Back {} Company'.format(name)
    Title_Label = Label(cpc, text = welcomeMessage)
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    Label(cpc, text="").pack()
    Label(cpc, text="").pack()
    Label(cpc, text="").pack()

    #Buttons

    Product_Button = Button(cpc, text = "List of Parts on Posted", width = 20, height = 3, command = viewProducts)
    Product_Button.config(font = ("Hevetica", 15,))
    Product_Button.pack()
    
    addProduct_Button = Button(cpc, text = "Add Part to System", width = 20, height = 3, command = addProducts)
    addProduct_Button.config(font = ("Hevetica", 15,))
    addProduct_Button.pack()

    cpc.mainloop()

def viewProducts():

    products = Tk()
    products.geometry('600x600')

    Select_Label = Label(products, text = 'Select Part Type')
    Select_Label.config(font = ("Hevetica", 15, "underline"))
    Select_Label.pack()

    Product_Frame = LabelFrame(products, text="Part Type")
    Product_Frame.pack(expand="yes", padx=0, pady = 0)

    CPU_Button = Button(Product_Frame, text = "CPU", width = 20, height = 3, command = viewCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.grid(row=0, column=0, padx=0, pady=0)

    RAM_Button = Button(Product_Frame, text = "RAM", width = 20, height = 3, command = viewRAM)
    RAM_Button.config(font = ("Hevetica", 15,))
    RAM_Button.grid(row=0, column=1, padx=0, pady=0)

    GPU_Button = Button(Product_Frame, text = "GPU", width = 20, height = 3, command = viewGPU)
    GPU_Button.config(font = ("Hevetica", 15,))
    GPU_Button.grid(row=1, column=0, padx=0, pady=0)

    Mother_Button = Button(Product_Frame, text = "Motherboard", width = 20, height = 3, command = viewMother)
    Mother_Button.config(font = ("Hevetica", 15,))
    Mother_Button.grid(row=1, column=1, padx=0, pady=0)

    Case_Button = Button(Product_Frame, text = "Case", width = 20, height = 3, command = viewCase)
    Case_Button.config(font = ("Hevetica", 15,))
    Case_Button.grid(row=2, column=0, padx=0, pady=0)

    Storage_Button = Button(Product_Frame, text = "Storage", width = 20, height = 3, command = viewStorage)
    Storage_Button.config(font = ("Hevetica", 15,))
    Storage_Button.grid(row=2, column=1, padx=0, pady=0)

    Cooler_Button = Button(Product_Frame, text = "CPU Cooler", width = 20, height = 3, command = viewCooler)
    Cooler_Button.config(font = ("Hevetica", 15,))
    Cooler_Button.grid(row=3, column=0, padx=0, pady=0)

    Power_Button = Button(Product_Frame, text = "Power Supply", width = 20, height = 3, command = viewPower)
    Power_Button.config(font = ("Hevetica", 15,))
    Power_Button.grid(row=3, column=1, padx=0, pady=0)

def viewCPU():

    cpu = Tk()
    cpu.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(cpu)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    #CPU
    cursor.execute("Select name, in_stock, sold, total_profit FROM cpu WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewRAM():

    ram = Tk()
    ram.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(ram)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    cursor.execute("Select name, in_stock, sold, total_profit FROM ram WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewGPU():
    gpu = Tk()
    gpu.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(gpu)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    #GPU
    cursor.execute("Select name, in_stock, sold, total_profit FROM gpu WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewMother():
    mother = Tk()
    mother.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(mother)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    #Motherboard
    cursor.execute("Select name, in_stock, sold, total_profit FROM motherboard WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewCase():
    case = Tk()
    case.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(case)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

     #Case
    cursor.execute("Select name, in_stock, sold, total_profit FROM cases WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewStorage():
    storage = Tk()
    storage.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(storage)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    #Storage
    cursor.execute("Select name, in_stock, sold, total_profit FROM storage WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewCooler():
    cooler = Tk()
    cooler.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(cooler)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    #Cooler
    cursor.execute("Select name, in_stock, sold, total_profit FROM cooler WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewPower():
    power = Tk()
    power.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(power)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "In Stock", "Number Sold", "Total Profit")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("In Stock", anchor = CENTER, width = 140)
    my_tree.column("Number Sold", anchor = CENTER, width = 140)
    my_tree.column("Total Profit", anchor = CENTER, width = 140)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("In Stock", text = "In Stock", anchor = CENTER)
    my_tree.heading("Number Sold", text = "Number Sold", anchor = CENTER)
    my_tree.heading("Total Profit", text = "Total Profit", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    global id 

    #PowerSupply
    cursor.execute("Select name, in_stock, sold, total_profit FROM powersupply WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def addProducts():
    products = Tk()
    products.geometry('600x600')

    Label(products, text="").pack()
    Label(products, text="").pack()
    Select_Label = Label(products, text = 'What type of Part would you like to Add?')
    Select_Label.config(font = ("Hevetica", 15))
    Select_Label.pack()

    Product_Frame = LabelFrame(products, text="Part Type")
    Product_Frame.pack(expand="yes", padx=0, pady = 0)

    CPU_Button = Button(Product_Frame, text = "CPU", width = 20, height = 3, command = addCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.grid(row=0, column=0, padx=0, pady=0)

    RAM_Button = Button(Product_Frame, text = "RAM", width = 20, height = 3, command = addRAM)
    RAM_Button.config(font = ("Hevetica", 15,))
    RAM_Button.grid(row=0, column=1, padx=0, pady=0)

    GPU_Button = Button(Product_Frame, text = "GPU", width = 20, height = 3, command = addGPU)
    GPU_Button.config(font = ("Hevetica", 15,))
    GPU_Button.grid(row=1, column=0, padx=0, pady=0)

    Mother_Button = Button(Product_Frame, text = "Motherboard", width = 20, height = 3, command = addMother)
    Mother_Button.config(font = ("Hevetica", 15,))
    Mother_Button.grid(row=1, column=1, padx=0, pady=0)

    Case_Button = Button(Product_Frame, text = "Case", width = 20, height = 3, command = addCase)
    Case_Button.config(font = ("Hevetica", 15,))
    Case_Button.grid(row=2, column=0, padx=0, pady=0)

    Storage_Button = Button(Product_Frame, text = "Storage", width = 20, height = 3, command = addStorage)
    Storage_Button.config(font = ("Hevetica", 15,))
    Storage_Button.grid(row=2, column=1, padx=0, pady=0)

    Cooler_Button = Button(Product_Frame, text = "CPU Cooler", width = 20, height = 3, command = addCooler)
    Cooler_Button.config(font = ("Hevetica", 15,))
    Cooler_Button.grid(row=3, column=0, padx=0, pady=0)

    Power_Button = Button(Product_Frame, text = "Power Supply", width = 20, height = 3, command = addPower)
    Power_Button.config(font = ("Hevetica", 15,))
    Power_Button.grid(row=3, column=1, padx=0, pady=0)

def addCPU():
    
    add = Tk()
    add.geometry('600x400')

    Info_Label = Label(add, text = 'CPU Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(add, text="").pack()
    Label(add, text="").pack()
    Label(add, text="").pack()

    CPU_Button = Button(add, text = "View CPU's already in System", width = 25, height = 2, command = viewCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(add)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)
    global id
    name = StringVar()
    number_of_cores = IntVar()
    clock_speed = StringVar()
    boosted_clock_speed = StringVar()
    integrated_graphics = StringVar()
    socket = StringVar()
    cooler = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the CPU Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many cores does the CPU have?: ").grid(row=1, column=0, padx=0, pady=0)
    coreEntry = Entry(Info_Frame, textvariable = number_of_cores)
    coreEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What is the clock speed of the CPU?: ").grid(row=2, column=0, padx=0, pady=0)
    cspeedEntry = Entry(Info_Frame, textvariable = clock_speed)
    cspeedEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the boosted clock speed of the CPU?: ").grid(row=3, column=0, padx=0, pady=0)
    bspeedEntry = Entry(Info_Frame, textvariable = boosted_clock_speed)
    bspeedEntry.grid(row=3, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What type of Integrated Graphics does the CPU have? Type N/A if no IG: ").grid(row=4, column=0, padx=0, pady=0)
    igEntry = Entry(Info_Frame, textvariable = integrated_graphics)
    igEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the socket type for the CPU: ").grid(row=5, column=0, padx=0, pady=0)
    socketEntry = Entry(Info_Frame, textvariable = socket)
    socketEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the CPU come with a cooler?: ").grid(row=5, column=0, padx=0, pady=0)
    coolerEntry = Entry(Info_Frame, textvariable = socket)
    coolerEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the CPU?: ").grid(row=6, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=7, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=7, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(add)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def cpuAdd():

        global id
        name = nameEntry.get()
        num_Cores = coreEntry.get()
        clock_speed = cspeedEntry.get()
        boosted_clock_speed = bspeedEntry.get()
        integrated_graphics = igEntry.get()
        socket = socketEntry.get()
        cooler = coolerEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()
        cursor.execute("INSERT INTO CPU (company_id, name, number_of_cores, clock_speed, boosted_clock_speed, integrated_graphics, socket, cooler, price, in_stock)" + 
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, num_Cores, clock_speed, boosted_clock_speed, integrated_graphics, socket, cooler, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM cpu WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = cpuAdd)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        add.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addRAM():

    add = Tk()
    add.geometry('600x400')

    Info_Label = Label(add, text = 'RAM Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(add, text="").pack()
    Label(add, text="").pack()
    Label(add, text="").pack()

    CPU_Button = Button(add, text = "View RAM's already in System", width = 25, height = 2, command = viewRAM)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(add)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)
    global id
    name = StringVar()
    type = StringVar()
    speed = IntVar()
    modules = StringVar()
    sticks = IntVar()
    rgb = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the RAM Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What type of RAM is it?: ").grid(row=1, column=0, padx=0, pady=0)
    typeEntry = Entry(Info_Frame, textvariable = type)
    typeEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What is the RAM speed?: ").grid(row=2, column=0, padx=0, pady=0)
    speedEntry = Entry(Info_Frame, textvariable = speed)
    speedEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many modules does the RAM have?: ").grid(row=3, column=0, padx=0, pady=0)
    modulesEntry = Entry(Info_Frame, textvariable = modules)
    modulesEntry.grid(row=3, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many sticks are in the RAM Package").grid(row=4, column=0, padx=0, pady=0)
    sticksEntry = Entry(Info_Frame, textvariable = sticks)
    sticksEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the RAM have RGB?: ").grid(row=5, column=0, padx=0, pady=0)
    rgbEntry = Entry(Info_Frame, textvariable = rgb)
    rgbEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the RAM?: ").grid(row=5, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=6, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=6, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(add)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def ramAdd():

        global id
        name = nameEntry.get()
        type = typeEntry.get()
        speed = speedEntry.get()
        modules = modulesEntry.get()
        sticks = sticksEntry.get()
        rgb = rgbEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO RAM (company_id, name, type, speed, modules, sticks, rgb, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, type, speed, modules, sticks, rgb, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM ram WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = ramAdd)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        add.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addGPU():

    add = Tk()
    add.geometry('600x400')

    Info_Label = Label(add, text = 'GPU Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(add, text="").pack()
    Label(add, text="").pack()
    Label(add, text="").pack()

    CPU_Button = Button(add, text = "View GPU's already in System", width = 25, height = 2, command = viewGPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(add)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

    global id
    name = StringVar()
    memory = IntVar()
    clock_speed = IntVar()
    boosted_clock_speed = IntVar()
    interface = StringVar()
    length = IntVar()
    hdmi = IntVar()
    display = IntVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the GPU Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Enter the amount of memory?: ").grid(row=1, column=0, padx=0, pady=0)
    memoryEntry = Entry(Info_Frame, textvariable = memory)
    memoryEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What is the clock speed of the GPU?: ").grid(row=2, column=0, padx=0, pady=0)
    cspeedEntry = Entry(Info_Frame, textvariable = clock_speed)
    cspeedEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the boosted clock speed of the GPU?: ").grid(row=4, column=0, padx=0, pady=0)
    bspeedEntry = Entry(Info_Frame, textvariable = boosted_clock_speed)
    bspeedEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What type of interface does the GPU use?: ").grid(row=5, column=0, padx=0, pady=0)
    interfaceEntry = Entry(Info_Frame, textvariable = interface)
    interfaceEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the length of the GPU?: ").grid(row=6, column=0, padx=0, pady=0)
    lengthEntry = Entry(Info_Frame, textvariable = length)
    lengthEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many HDMI ports does the GPU have?: ").grid(row=7, column=0, padx=0, pady=0)
    hdmiEntry = Entry(Info_Frame, textvariable = hdmi)
    hdmiEntry.grid(row=7, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many Display ports does the GPU have?: ").grid(row=8, column=0, padx=0, pady=0)
    displayEntry = Entry(Info_Frame, textvariable = display)
    displayEntry.grid(row=8, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the GPU?: ").grid(row=9, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=9, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=10, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=10, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(add)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def ramAdd():

        global id
        name = nameEntry.get()
        memory = memoryEntry.get()
        clock_speed = cspeedEntry.get()
        boosted_clock_speed = bspeedEntry.get()
        interface = interfaceEntry.get()
        length = lengthEntry.get()
        hdmi = hdmiEntry.get()
        display = displayEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO GPU (company_id, name, memory, clock_speed, boosted_clock_speed, interface, length, hdmi_ports, display_ports, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, memory, clock_speed, boosted_clock_speed, interface, length, hdmi, display, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM gpu WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = ramAdd)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        add.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)
    
def addMother():
    print('')
def addCase():
    print('')
def addCase():
    print('')
def addStorage():
    print('')
def addCooler():
    print('')
def addPower():
    print('')





id = 1
CPC_GUI(id)