import mysql.connector
from tkinter import *
from tkinter import ttk
from Delivery_Company_Complain import *
import os

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)
#print ("Connnected To Database")
cursor = con.cursor()

def CPC_GUI(id):

    cpc = Tk()
    cpc.geometry('500x450')

    #Title Label
    #global id
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

    def vProducts():
        viewProducts(id)

    Product_Button = Button(cpc, text = "List of Parts on Posted", width = 20, height = 3, command = vProducts)
    Product_Button.config(font = ("Hevetica", 15,))
    Product_Button.pack()
    
    def aProducts():
        addProducts(id)

    addProduct_Button = Button(cpc, text = "Add Part to System", width = 20, height = 3, command = aProducts)
    addProduct_Button.config(font = ("Hevetica", 15,))
    addProduct_Button.pack()

    def vWallet():
        viewWallet(id)

    Wallet_Button = Button(cpc, text = "Wallet", width = 20, height = 3, command = vWallet)
    Wallet_Button.config(font = ("Hevetica", 15,))
    Wallet_Button.pack()

    complain_button = Button(cpc, text = "List of Complains", width = 20, height = 3, command = lambda id=id: browse_all_complains(id))
    complain_button.config(font = ("Hevetica", 15,))
    complain_button.pack()

    cpc.mainloop()

def viewProducts(id):

    products = Tk()
    products.geometry('600x600')

    Select_Label = Label(products, text = 'Select Part Type')
    Select_Label.config(font = ("Hevetica", 15, "underline"))
    Select_Label.pack()

    Product_Frame = LabelFrame(products, text="Part Type")
    Product_Frame.pack(expand="yes", padx=0, pady = 0)

    def vCPU():
        viewCPU(id)

    CPU_Button = Button(Product_Frame, text = "CPU", width = 20, height = 3, command = vCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.grid(row=0, column=0, padx=0, pady=0)

    def vRAM():
        viewRAM(id)

    RAM_Button = Button(Product_Frame, text = "RAM", width = 20, height = 3, command = vRAM)
    RAM_Button.config(font = ("Hevetica", 15,))
    RAM_Button.grid(row=0, column=1, padx=0, pady=0)

    def vGPU():
        viewGPU(id)

    GPU_Button = Button(Product_Frame, text = "GPU", width = 20, height = 3, command = vGPU)
    GPU_Button.config(font = ("Hevetica", 15,))
    GPU_Button.grid(row=1, column=0, padx=0, pady=0)

    def vMother():
        viewMother(id)

    Mother_Button = Button(Product_Frame, text = "Motherboard", width = 20, height = 3, command = vMother)
    Mother_Button.config(font = ("Hevetica", 15,))
    Mother_Button.grid(row=1, column=1, padx=0, pady=0)

    def vCase():
        viewCase(id)

    Case_Button = Button(Product_Frame, text = "Case", width = 20, height = 3, command = vCase)
    Case_Button.config(font = ("Hevetica", 15,))
    Case_Button.grid(row=2, column=0, padx=0, pady=0)

    def vStorage():
        viewStorage(id)

    Storage_Button = Button(Product_Frame, text = "Storage", width = 20, height = 3, command = vStorage)
    Storage_Button.config(font = ("Hevetica", 15,))
    Storage_Button.grid(row=2, column=1, padx=0, pady=0)

    def vCooler():
        viewCooler(id)

    Cooler_Button = Button(Product_Frame, text = "CPU Cooler", width = 20, height = 3, command = vCooler)
    Cooler_Button.config(font = ("Hevetica", 15,))
    Cooler_Button.grid(row=3, column=0, padx=0, pady=0)

    def vPower():
        viewPower(id)

    Power_Button = Button(Product_Frame, text = "Power Supply", width = 20, height = 3, command = vPower)
    Power_Button.config(font = ("Hevetica", 15,))
    Power_Button.grid(row=3, column=1, padx=0, pady=0)

def viewCPU(id):

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

def viewRAM(id):

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

def viewGPU(id):
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

def viewMother(id):
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

def viewCase(id):
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

     #Case
    cursor.execute("Select name, in_stock, sold, total_profit FROM case WHERE company_id = %s", (id,))
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        count += 1
    con.commit()

def viewStorage(id):
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

def viewCooler(id):
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

def viewPower(id):
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


def addProducts(id):

    products = Tk()
    products.geometry('600x600')

    Label(products, text="").pack()
    Label(products, text="").pack()
    Select_Label = Label(products, text = 'What type of Part would you like to Add?')
    Select_Label.config(font = ("Hevetica", 15))
    Select_Label.pack()

    Product_Frame = LabelFrame(products, text="Part Type")
    Product_Frame.pack(expand="yes", padx=0, pady = 0)

    def aCPU():
        addCPU(id)

    CPU_Button = Button(Product_Frame, text = "CPU", width = 20, height = 3, command = aCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.grid(row=0, column=0, padx=0, pady=0)

    def aRAM():
        addRAM(id)

    RAM_Button = Button(Product_Frame, text = "RAM", width = 20, height = 3, command = aRAM)
    RAM_Button.config(font = ("Hevetica", 15,))
    RAM_Button.grid(row=0, column=1, padx=0, pady=0)

    def aGPU():
        addGPU(id)

    GPU_Button = Button(Product_Frame, text = "GPU", width = 20, height = 3, command = aGPU)
    GPU_Button.config(font = ("Hevetica", 15,))
    GPU_Button.grid(row=1, column=0, padx=0, pady=0)

    def aMother():
        addMother(id)

    Mother_Button = Button(Product_Frame, text = "Motherboard", width = 20, height = 3, command = aMother)
    Mother_Button.config(font = ("Hevetica", 15,))
    Mother_Button.grid(row=1, column=1, padx=0, pady=0)

    def aCase():
        addCase(id)

    Case_Button = Button(Product_Frame, text = "Case", width = 20, height = 3, command = aCase)
    Case_Button.config(font = ("Hevetica", 15,))
    Case_Button.grid(row=2, column=0, padx=0, pady=0)

    def aStorage():
        addStorage(id)

    Storage_Button = Button(Product_Frame, text = "Storage", width = 20, height = 3, command = aStorage)
    Storage_Button.config(font = ("Hevetica", 15,))
    Storage_Button.grid(row=2, column=1, padx=0, pady=0)

    def aCooler():
        addCooler(id)

    Cooler_Button = Button(Product_Frame, text = "CPU Cooler", width = 20, height = 3, command = aCooler)
    Cooler_Button.config(font = ("Hevetica", 15,))
    Cooler_Button.grid(row=3, column=0, padx=0, pady=0)

    def aPower():
        addPower(id)

    Power_Button = Button(Product_Frame, text = "Power Supply", width = 20, height = 3, command = aPower)
    Power_Button.config(font = ("Hevetica", 15,))
    Power_Button.grid(row=3, column=1, padx=0, pady=0)

def addCPU(id):
    
    cpuadd = Tk()
    cpuadd.geometry('600x400')

    Info_Label = Label(cpuadd, text = 'CPU Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(cpuadd, text="").pack()
    Label(cpuadd, text="").pack()
    Label(cpuadd, text="").pack()

    CPU_Button = Button(cpuadd, text = "View CPU's already in System", width = 25, height = 2, command = viewCPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(cpuadd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

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
    coolerEntry = Entry(Info_Frame, textvariable = cooler)
    coolerEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the CPU?: ").grid(row=6, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=7, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=7, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(cpuadd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

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

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        cpuadd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addRAM(id):

    ramadd = Tk()
    ramadd.geometry('600x400')

    Info_Label = Label(ramadd, text = 'RAM Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(ramadd, text="").pack()
    Label(ramadd, text="").pack()
    Label(ramadd, text="").pack()

    CPU_Button = Button(ramadd, text = "View RAM's already in System", width = 25, height = 2, command = viewRAM)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(ramadd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

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

    Button_Frame = LabelFrame(ramadd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

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

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        ramadd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addGPU(id):

    gpuadd = Tk()
    gpuadd.geometry('600x400')

    Info_Label = Label(gpuadd, text = 'GPU Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(gpuadd, text="").pack()
    Label(gpuadd, text="").pack()
    Label(gpuadd, text="").pack()

    CPU_Button = Button(gpuadd, text = "View GPU's already in System", width = 25, height = 2, command = viewGPU)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(gpuadd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

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

    Button_Frame = LabelFrame(gpuadd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

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

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        gpuadd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)
    
def addMother(id):
   
    motheradd = Tk()
    motheradd.geometry('600x500')

    Info_Label = Label(motheradd, text = 'Motherboard Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(motheradd, text="").pack()
    Label(motheradd, text="").pack()
    Label(motheradd, text="").pack()

    CPU_Button = Button(motheradd, text = "View Motherboard's already in System", width = 25, height = 2, command = viewMother)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(motheradd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

    name = StringVar()
    form_factor = StringVar()
    socket = StringVar()
    memory_type = StringVar()
    memory_slots = IntVar()
    pci_16 = StringVar()
    ethernet = StringVar()
    sata = IntVar()
    usb_2 = IntVar()
    usb_3 = IntVar()
    wireless = StringVar()
    rgb = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the Motherboard Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the form factor of the motherboard?: ").grid(row=1, column=0, padx=0, pady=0)
    ffEntry = Entry(Info_Frame, textvariable = form_factor)
    ffEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What type of socket does the motherboard have?: ").grid(row=2, column=0, padx=0, pady=0)
    socketEntry = Entry(Info_Frame, textvariable = socket)
    socketEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What type of memory does the motherboard use?: ").grid(row=4, column=0, padx=0, pady=0)
    mtypeEntry = Entry(Info_Frame, textvariable = memory_type)
    mtypeEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many memory slots does the motherboard have?: ").grid(row=5, column=0, padx=0, pady=0)
    mslotsEntry = Entry(Info_Frame, textvariable = memory_slots)
    mslotsEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the motherboard use PCIx16?: ").grid(row=6, column=0, padx=0, pady=0)
    pciEntry = Entry(Info_Frame, textvariable = pci_16)
    pciEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the motherboard support ethernet?: ").grid(row=7, column=0, padx=0, pady=0)
    ethernetEntry = Entry(Info_Frame, textvariable = ethernet)
    ethernetEntry.grid(row=7, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How manny sata ports does the motherboard have?: ").grid(row=8, column=0, padx=0, pady=0)
    sataEntry = Entry(Info_Frame, textvariable = sata)
    sataEntry.grid(row=8, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many usb 2.0 headers does the motherboard have?: ").grid(row=9, column=0, padx=0, pady=0)
    usb2Entry = Entry(Info_Frame, textvariable = usb_2)
    usb2Entry.grid(row=9, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many usb 3.0 headers does the motherboard have?: ").grid(row=10, column=0, padx=0, pady=0)
    usb3Entry = Entry(Info_Frame, textvariable = usb_3)
    usb3Entry.grid(row=10, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the motherboard support wireless connection?: ").grid(row=11, column=0, padx=0, pady=0)
    wirelessEntry = Entry(Info_Frame, textvariable = wireless)
    wirelessEntry.grid(row=11, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the motherboard have rgb?: ").grid(row=12, column=0, padx=0, pady=0)
    rgbEntry = Entry(Info_Frame, textvariable = rgb)
    rgbEntry.grid(row=12, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the motherboard?: ").grid(row=13, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=13, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=14, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=14, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(motheradd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

        name = nameEntry.get()
        form_factor = ffEntry.get()
        socket = socketEntry.get()
        memory_type = mtypeEntry.get()
        memory_slots = mslotsEntry.get()
        pci_16 = pciEntry.get()
        ethernet = ethernetEntry.get()
        sata = sataEntry.get()
        usb_2 = usb2Entry.get()
        usb_3 = usb3Entry.get()
        wireless = wirelessEntry.get()
        rgb = rgbEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO motherboard (company_id, name, form_factor, socket, memory_type, memory_slots, pci_16, ethernet, sata, usb_2, usb_3, wireless, rgb, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, form_factor, socket, memory_type, memory_slots, pci_16, ethernet, sata, usb_2, usb_3, wireless, rgb, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM motherboard WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        motheradd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addCase(id):

    caseadd = Tk()
    caseadd.geometry('600x500')

    Info_Label = Label(caseadd, text = 'Case Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(caseadd, text="").pack()
    Label(caseadd, text="").pack()
    Label(caseadd, text="").pack()

    CPU_Button = Button(caseadd, text = "View Case's already in System", width = 25, height = 2, command = viewCase)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(caseadd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

    name = StringVar()
    case_type = StringVar()
    side_panel = StringVar()
    external_bay = IntVar()
    internal_bay = IntVar()
    max_gpu_size = IntVar()
    max_fan_size = IntVar()
    num_front_fan = IntVar()
    num_top_fan = IntVar()
    num_exhuast_fan = IntVar()
    num_fan_included = IntVar()
    max_radiator = IntVar()
    rgb = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the Case Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the case type?: ").grid(row=1, column=0, padx=0, pady=0)
    ctypeEntry = Entry(Info_Frame, textvariable = case_type)
    ctypeEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What is the type of side_panel the case has?: ").grid(row=2, column=0, padx=0, pady=0)
    spanelEntry = Entry(Info_Frame, textvariable = side_panel)
    spanelEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many external bays does the case have?: ").grid(row=4, column=0, padx=0, pady=0)
    ebayEntry = Entry(Info_Frame, textvariable = external_bay)
    ebayEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How man internal bays does the the case have?: ").grid(row=5, column=0, padx=0, pady=0)
    ibayEntry = Entry(Info_Frame, textvariable = internal_bay)
    ibayEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What the the maximum gpu size you can fit in the case?: ").grid(row=6, column=0, padx=0, pady=0)
    mgsizeEntry = Entry(Info_Frame, textvariable = max_gpu_size)
    mgsizeEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the maximum size of fans that can fit in the case?: ").grid(row=7, column=0, padx=0, pady=0)
    mfsizeEntry = Entry(Info_Frame, textvariable = max_fan_size)
    mfsizeEntry.grid(row=7, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the max number of front panel fans you can have?: ").grid(row=8, column=0, padx=0, pady=0)
    nffEntry = Entry(Info_Frame, textvariable = num_front_fan)
    nffEntry.grid(row=8, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the maximum number of top panel fans you can have?: ").grid(row=9, column=0, padx=0, pady=0)
    ntfEntry = Entry(Info_Frame, textvariable = num_top_fan)
    ntfEntry.grid(row=9, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the number of exhaust fans the case has?: ").grid(row=10, column=0, padx=0, pady=0)
    nefEntry = Entry(Info_Frame, textvariable = num_exhuast_fan)
    nefEntry.grid(row=10, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many fans are included in the case?: ").grid(row=11, column=0, padx=0, pady=0)
    nfiEntry = Entry(Info_Frame, textvariable = num_fan_included)
    nfiEntry.grid(row=11, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the maximum radiator size?: ").grid(row=12, column=0, padx=0, pady=0)
    mradEntry = Entry(Info_Frame, textvariable = max_radiator)
    mradEntry.grid(row=12, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the case have rgb?: ").grid(row=13, column=0, padx=0, pady=0)
    rgbEntry = Entry(Info_Frame, textvariable = rgb)
    rgbEntry.grid(row=13, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the motherboard?: ").grid(row=14, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=14, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=15, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=15, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(caseadd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

        name = nameEntry.get()
        case_type = ctypeEntry.get()
        side_panel = spanelEntry.get()
        external_bay = ebayEntry.get()
        internal_bay = ibayEntry.get()
        max_gpu_size = mgsizeEntry.get()
        max_fan_size = mfsizeEntry.get()
        num_front_fan = nffEntry.get()
        num_top_fan = ntfEntry.get()
        num_exhuast_fan = nefEntry.get()
        num_fan_included = nfiEntry.get()
        max_radiator = mradEntry.get()
        rgb = rgbEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO case (company_id, name, case_type, side_panel, external_bay, internal_bay, max_gpu_size, max_fan_size, num_front_fan, num_top_fan, num_exhaust_fan, num_fan_included, max_radiator, rgb, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, case_type, side_panel, external_bay, internal_bay, max_gpu_size, max_fan_size, num_front_fan, num_top_fan, num_exhuast_fan, num_fan_included, max_radiator, rgb, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM case WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        caseadd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addStorage(id):

    storageadd = Tk()
    storageadd.geometry('600x500')

    Info_Label = Label(storageadd, text = 'Case Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(storageadd, text="").pack()
    Label(storageadd, text="").pack()
    Label(storageadd, text="").pack()

    CPU_Button = Button(storageadd, text = "View Case's already in System", width = 25, height = 2, command = viewCase)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(storageadd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

    name = StringVar()
    capacity = StringVar()
    type = StringVar()
    form_factor = StringVar()
    interface = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the Storage Device Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the total capacity of the storage device?: ").grid(row=1, column=0, padx=0, pady=0)
    capacityEntry = Entry(Info_Frame, textvariable = capacity)
    capacityEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What is the form factor of the storage device?: ").grid(row=2, column=0, padx=0, pady=0)
    typeEntry = Entry(Info_Frame, textvariable = type)
    typeEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How many external bays does the case have?: ").grid(row=4, column=0, padx=0, pady=0)
    ffEntry = Entry(Info_Frame, textvariable = form_factor)
    ffEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What interface does the storage device use? ").grid(row=5, column=0, padx=0, pady=0)
    interfaceEntry = Entry(Info_Frame, textvariable = interface)
    interfaceEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the storage device?: ").grid(row=6, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=7, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=7, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(storageadd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

        name = nameEntry.get()
        capacity = capacityEntry.get()
        type = typeEntry.get()
        form_factor = ffEntry.get()
        interface = interfaceEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO storage (company_id, name, capacity, type, form_factor, Interface, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, capacity, type, form_factor, interface, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM storage WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        storageadd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addCooler(id):

    cooleradd = Tk()
    cooleradd.geometry('600x500')

    Info_Label = Label(cooleradd, text = 'CPU Cooler Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(cooleradd, text="").pack()
    Label(cooleradd, text="").pack()
    Label(cooleradd, text="").pack()

    CPU_Button = Button(cooleradd, text = "View Coolers already in System", width = 25, height = 2, command = viewCase)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(cooleradd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

    name = StringVar()
    fan_rpm = StringVar()
    type_of_cooler = StringVar()
    radiator = IntVar()
    socket = StringVar()
    rgb = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the Cooler Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the fan rpm of the cooler?: ").grid(row=1, column=0, padx=0, pady=0)
    frpmEntry = Entry(Info_Frame, textvariable = fan_rpm)
    frpmEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What type of cooler is it?: ").grid(row=2, column=0, padx=0, pady=0)
    tocEntry = Entry(Info_Frame, textvariable = type_of_cooler)
    tocEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How big is the radiator? If no radiator type 0: ").grid(row=4, column=0, padx=0, pady=0)
    radiatorEntry = Entry(Info_Frame, textvariable = radiator)
    radiatorEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What sockets does the cooler support? ").grid(row=5, column=0, padx=0, pady=0)
    socketEntry = Entry(Info_Frame, textvariable = socket)
    socketEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "Does the cooler have rgb? ").grid(row=6, column=0, padx=0, pady=0)
    rgbEntry = Entry(Info_Frame, textvariable = rgb)
    rgbEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the cooler device?: ").grid(row=7, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=7, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=8, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=8, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(cooleradd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

        name = nameEntry.get()
        fan_rpm = frpmEntry.get()
        type_of_cooler = tocEntry.get()
        radiator = radiatorEntry.get()
        socket = socketEntry.get()
        rgb = rgbEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO cooler (company_id, name, fan_rpm, type_of_cooler, Radiator, socket, rgb, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}', '{}')".format(id, name, fan_rpm, type_of_cooler, radiator, socket, rgb, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM cooler WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        cooleradd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def addPower(id):

    poweradd = Tk()
    poweradd.geometry('600x500')

    Info_Label = Label(poweradd, text = 'Power Supply Info')
    Info_Label.config(font = ("Hevetica", 15, "underline"))
    Info_Label.pack()

    Label(poweradd, text="").pack()
    Label(poweradd, text="").pack()
    Label(poweradd, text="").pack()

    CPU_Button = Button(poweradd, text = "View Power Supplies already in System", width = 25, height = 2, command = viewCase)
    CPU_Button.config(font = ("Hevetica", 15,))
    CPU_Button.pack()

    Info_Frame = LabelFrame(poweradd)
    Info_Frame.pack(expand="yes", padx=0, pady = 0)

    name = StringVar()
    form_factor = StringVar()
    efficency = StringVar()
    wattage = IntVar()
    modular = StringVar()
    price = IntVar()
    stock = IntVar()

    Label(Info_Frame, text = "Enter the power supply Name: ").grid(row=0, column=0, padx=0, pady=0)
    nameEntry = Entry(Info_Frame, textvariable = name)
    nameEntry.grid(row=0, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the form factor of the power supply?: ").grid(row=1, column=0, padx=0, pady=0)
    ffEntry = Entry(Info_Frame, textvariable = form_factor)
    ffEntry.grid(row=1, column=1, padx=0, pady=0)
    
    Label(Info_Frame, text = "What is the efficency of the power supply?: ").grid(row=2, column=0, padx=0, pady=0)
    efficencyEntry = Entry(Info_Frame, textvariable = efficency)
    efficencyEntry.grid(row=2, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the total wattage of the power supply: ").grid(row=4, column=0, padx=0, pady=0)
    wattageEntry = Entry(Info_Frame, textvariable = wattage)
    wattageEntry.grid(row=4, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "If the power supply modular? ").grid(row=5, column=0, padx=0, pady=0)
    modularEntry = Entry(Info_Frame, textvariable = modular)
    modularEntry.grid(row=5, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "What is the  price of the cooler device?: ").grid(row=6, column=0, padx=0, pady=0)
    priceEntry = Entry(Info_Frame, textvariable = price)
    priceEntry.grid(row=6, column=1, padx=0, pady=0)

    Label(Info_Frame, text = "How much stock do you have?: ").grid(row=7, column=0, padx=0, pady=0)
    stockEntry = Entry(Info_Frame, textvariable = stock)
    stockEntry.grid(row=7, column=1, padx=0, pady=0)

    Button_Frame = LabelFrame(poweradd)
    Button_Frame.pack(expand="yes", padx=0, pady = 0)

    def Add():

        name = nameEntry.get()
        form_factor = ffEntry.get()
        efficency = efficencyEntry.get()
        wattage = wattageEntry.get()
        modular = modularEntry.get()
        price = priceEntry.get()
        stock = stockEntry.get()

        cursor.execute("INSERT INTO powersupply (company_id, name, form_factor, efficency, wattage, modular, price, in_stock)" +
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, form_factor, efficency, wattage, modular, price, stock))
        con.commit()

        cursor.execute("SELECT * FROM powersupply WHERE company_id = %s AND name = %s", (id, name))
        records = cursor.fetchall()
        count = cursor.rowcount
        if count == 1:
            Label(Button_Frame, text = "The Part was added to the System").grid(row=2, column=0, padx=0, pady=0)
        else:
            Label(Button_Frame, text = "Failed to add Part to the System,").grid(row=2, column=0, padx=0, pady=0)

    Add_Button = Button(Button_Frame, text = "Add to System", width = 10, command = Add)
    Add_Button.config(font = ("Hevetica", 10,))
    Add_Button.grid(row=0, column=0, padx=0, pady=0)

    def close():
        poweradd.destroy()

    Close_Button = Button(Button_Frame, text = "Close", width = 10, command = close)
    Close_Button.config(font = ("Hevetica", 10,))
    Close_Button.grid(row=1, column=0, padx=0, pady=0)

def viewWallet(id):

    wallet = Tk()
    wallet.geometry('500x450')

    #CPU Total
    cursor.execute("SELECT SUM(total_profit) FROM cpu WHERE company_id = %s", (id,))
    cpusum = cursor.fetchall()[0][0]
    if cpusum is None:
        cpusum = 0
    #print(cpusum)
    #RAM Total
    cursor.execute("SELECT SUM(total_profit) FROM ram WHERE company_id = %s", (id,))
    ramsum = cursor.fetchall()[0][0]
    if ramsum is None:
        ramsum = 0
    #print(ramsum)
    #GPU Total
    cursor.execute("SELECT SUM(total_profit) FROM gpu WHERE company_id = %s", (id,))
    gpusum = cursor.fetchall()[0][0]
    if gpusum is None:
        gpusum = 0
    #print(gpusum)
    #Mother Total
    cursor.execute("SELECT SUM(total_profit) FROM motherboard WHERE company_id = %s", (id,))
    mothersum = cursor.fetchall()[0][0]
    if mothersum is None:
        mothersum = 0
    #print(mothersum)
    #Case Total
    cursor.execute("SELECT SUM(total_profit) FROM computer_store.case WHERE company_id = %s", (id,))
    casesum = cursor.fetchall()[0][0]
    if casesum is None:
        casesum = 0
    #print(casesum)
    #Storage Total
    cursor.execute("SELECT SUM(total_profit) FROM storage WHERE company_id = %s", (id,))
    storagesum = cursor.fetchall()[0][0]
    if storagesum is None:
        storagesum = 0
    #print(storagesum)
    #Cooler Total
    cursor.execute("SELECT SUM(total_profit) FROM cooler WHERE company_id = %s", (id,))
    coolersum = cursor.fetchall()[0][0]
    if coolersum is None:
        coolersum = 0
    #print(coolersum)
    #Power Total 
    cursor.execute("SELECT SUM(total_profit) FROM powersupply WHERE company_id = %s", (id,))
    powersum = cursor.fetchall()[0][0]
    if powersum is None:
        powersum = 0
    #print(powersum)

    #Total Sum:
    totalSum = cpusum + ramsum + gpusum + mothersum + casesum + storagesum + coolersum + powersum
    #print(totalSum)
    cursor.execute("Update computer_parts_companies SET funds = %s WHERE company_id = %s",(totalSum, id))
    con.commit()

    Title_Label = Label(wallet, text = 'Wallet')
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    Label(wallet, text="").pack()
    Label(wallet, text="").pack()
    Label(wallet, text="").pack()

    Cash_Frame = LabelFrame(wallet)
    Cash_Frame.pack(expand="yes", padx=0, pady = 0)

    Cash_Label = Label(Cash_Frame, text = "Cash: ")
    Cash_Label.config(font = ("Hevetica", 30))
    Cash_Label.grid(row=0, column=0, padx=0, pady=0)
    
    totalSum_Label = Label(Cash_Frame, text = "$%s" % (totalSum))
    totalSum_Label.config(font = ("Hevetica", 30))
    totalSum_Label.grid(row=0, column=1, padx=0, pady=0)

#id = 1
#CPC_GUI(id)