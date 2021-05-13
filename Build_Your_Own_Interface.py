from tkinter import *
from tkinter import ttk
import mysql.connector
import os
from Buy_GUI import *

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)

#print ("Connnected To Database")
cursor = con.cursor()


def Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id):
    
    global Build
    Build = Tk()
    Build.geometry('500x450')
    
    #Title Label
    Title_Label = Label(Build, text = "Build Your Own PC")
    Title_Label.config(font = ("Hevetica", 20, "underline"))
    Title_Label.pack()

    #CPU Selection
    CPU_Frame = LabelFrame(Build, text="CPU")
    CPU_Frame.pack(fill="x", expand="yes", padx=0)

    CPU_Label = Label(CPU_Frame, text = "CPU:")
    CPU_Label.config(font = ("Hevetica", 15,))
    CPU_Label.grid(row=0, column=0, padx=0, pady=0)

    cpu_name_Label = Label(CPU_Frame, text = cpu_name)
    cpu_name_Label.config(font = ("Hevetica", 12,))
    cpu_name_Label.grid(row=0, column=2, padx=0, pady=0)

    CPU_Button = Button(CPU_Frame, text = "Select CPU", width = 10, command=lambda id=id: selectCPU(id))
    CPU_Button.grid(row=0, column=1, padx=0, pady=0)
    
    #RAM Selection
    RAM_Frame = LabelFrame(Build, text="RAM")
    RAM_Frame.pack(fill="x", expand="yes", padx=0)

    RAM_Label = Label(RAM_Frame, text = "RAM:")
    RAM_Label.config(font = ("Hevetica", 15,))
    RAM_Label.grid(row=0, column=0, padx=0, pady=0)

    ram_name_Label = Label(RAM_Frame, text = ram_name)
    ram_name_Label.config(font = ("Hevetica", 12,))
    ram_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    RAM_Button = Button(RAM_Frame, text = "Select RAM", width = 10, command=lambda id=id: selectRAM(id))
    RAM_Button.grid(row=0, column=1, padx=0, pady=0)

    #GPU Label
    GPU_Frame = LabelFrame(Build, text="GPU")
    GPU_Frame.pack(fill="x", expand="yes", padx=0)

    GPU_Label = Label(GPU_Frame, text = "GPU:")
    GPU_Label.config(font = ("Hevetica", 15,))
    GPU_Label.grid(row=0, column=0, padx=0, pady=0)

    gpu_name_Label = Label(GPU_Frame, text = gpu_name)
    gpu_name_Label.config(font = ("Hevetica", 12,))
    gpu_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    GPU_Button = Button(GPU_Frame, text = "Select GPU", width = 10, command=lambda id=id: selectGPU(id))
    GPU_Button.grid(row=0, column=1, padx=0, pady=0)

    #Motherboard Label
    Mother_Frame = LabelFrame(Build, text="MotherBoard")
    Mother_Frame.pack(fill="x", expand="yes", padx=0)

    Mother_Label = Label(Mother_Frame, text = "MotherBoard:")
    Mother_Label.config(font = ("Hevetica", 15,))
    Mother_Label.grid(row=0, column=0, padx=0, pady=0)

    mother_name_Label = Label(Mother_Frame, text = mother_name)
    mother_name_Label.config(font = ("Hevetica", 12,))
    mother_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    Mother_Button = Button(Mother_Frame, text = "Select MotherBoard", width = 12, command=lambda id=id: selectMotherboard(id))
    Mother_Button.grid(row=0, column=1, padx=0, pady=0)

    #Case Label
    Case_Frame = LabelFrame(Build, text="Case")
    Case_Frame.pack(fill="x", expand="yes", padx=0)

    Case_Label = Label(Case_Frame, text = "Case:")
    Case_Label.config(font = ("Hevetica", 15,))
    Case_Label.grid(row=0, column=0, padx=0, pady=0)

    case_name_Label = Label(Case_Frame, text = case_name)
    case_name_Label.config(font = ("Hevetica", 12,))
    case_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    Case_Button = Button(Case_Frame, text = "Select Case", width = 10, command=lambda id=id: selectCase(id))
    Case_Button.grid(row=0, column=1, padx=0, pady=0)

    #Storage Label
    Storage_Frame = LabelFrame(Build, text="Storage")
    Storage_Frame.pack(fill="x", expand="yes", padx=0)

    Storage_Label = Label(Storage_Frame, text = "Storage:")
    Storage_Label.config(font = ("Hevetica", 15,))
    Storage_Label.grid(row=0, column=0, padx=0, pady=0)

    storage_name_Label = Label(Storage_Frame, text = storage_name)
    storage_name_Label.config(font = ("Hevetica", 12,))
    storage_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    Storage_Button = Button(Storage_Frame, text = "Select Storage", width = 10, command=lambda id=id: selectStorage(id))
    Storage_Button.grid(row=0, column=1, padx=0, pady=0)

    #Cooler Label
    Cooler_Frame = LabelFrame(Build, text="Cooler")
    Cooler_Frame.pack(fill="x", expand="yes", padx=0)

    Cooler_Label = Label(Cooler_Frame, text = "Cooler:")
    Cooler_Label.config(font = ("Hevetica", 15,))
    Cooler_Label.grid(row=0, column=0, padx=0, pady=0)

    cooler_name_Label = Label(Cooler_Frame, text = cooler_name)
    cooler_name_Label.config(font = ("Hevetica", 12,))
    cooler_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    Cooler_Button = Button(Cooler_Frame, text = "Select Cooler", width = 10, command=lambda id=id: selectCooler(id))
    Cooler_Button.grid(row=0, column=1, padx=0, pady=0)

    #Power Label
    Power_Frame = LabelFrame(Build, text="Power Supply")
    Power_Frame.pack(fill="x", expand="yes", padx=0)

    Power_Label = Label(Power_Frame, text = "Power_Supply:")
    Power_Label.config(font = ("Hevetica", 15,))
    Power_Label.grid(row=0, column=0, padx=0, pady=0)

    power_name_Label = Label(Power_Frame, text = power_name)
    power_name_Label.config(font = ("Hevetica", 12,))
    power_name_Label.grid(row=0, column=2, padx=0, pady=0)
    
    Power_Button = Button(Power_Frame, text = "Select Power Supply", width = 13, command=lambda id=id: selectPower(id))
    Power_Button.grid(row=0, column=1, padx=0, pady=0)

    #Compatiable Label
    Compatiable_Frame = LabelFrame(Build, text="Issues")
    Compatiable_Frame.pack(fill="x", expand="yes", padx=0)

    Compatiable_Label = Label(Compatiable_Frame, text = "Issues:")
    Compatiable_Label.config(font = ("Hevetica", 15,))
    Compatiable_Label.grid(row=0, column=0, padx=0, pady=0)

    #Compatiable Code
    
    global mother_formfactor
    global case_formfactor
    global mother_formfactor_num
    global case_formfactor_num

    if case_formfactor == 'E-ATX':
        case_formfactor_num = 4
    elif case_formfactor == 'ATX':
        case_formfactor_num = 3
    elif case_formfactor == 'Micro-ATX':
        case_formfactor_num = 2
    
    if mother_formfactor == 'E-ATX':
        mother_formfactor_num = 4
    elif mother_formfactor == 'ATX':
        mother_formfactor_num = 3
    elif mother_formfactor == 'Micro-ATX':
        mother_formfactor_num = 2

    global gpu_length
    global case_gpu_length
    gpu_length = int (gpu_length)
    case_gpu_length = int(case_gpu_length)

    global case_radiator
    global cooler_radiator
    case_radiator = int(case_radiator)
    cooler_radiator = int(cooler_radiator)

    global cpu_socket
    global mother_socket
    if cpu_socket == mother_socket:
        global ram_type
        global mother_ram_type
        if ram_type == mother_ram_type:
            global ram_sticks
            global mother_ram_sticks
            if mother_ram_sticks >= ram_sticks:
                if case_gpu_length >= gpu_length:
                    if case_formfactor_num >= mother_formfactor_num:
                        if case_radiator >= cooler_radiator:
                            global cooler_socket
                            if cooler_socket == 'All':
                                issue_name_Label = Label(Compatiable_Frame, text = 'No Issues')
                                issue_name_Label.config(font = ("Hevetica", 12,))
                                issue_name_Label.grid(row=0, column=2, padx=0, pady=0) 
                            elif cooler_socket == cpu_socket:
                                issue_name_Label = Label(Compatiable_Frame, text = 'No Issues')
                                issue_name_Label.config(font = ("Hevetica", 12,))
                                issue_name_Label.grid(row=0, column=2, padx=0, pady=0) 
                            else:
                                issue_name_Label = Label(Compatiable_Frame, text = 'Your cooler is not compatiable with your CPU')
                                issue_name_Label.config(font = ("Hevetica", 12,))
                                issue_name_Label.grid(row=0, column=2, padx=0, pady=0)          
                        else:
                            issue_name_Label = Label(Compatiable_Frame, text = 'The Radiator is not compatiable with your Case')
                            issue_name_Label.config(font = ("Hevetica", 12,))
                            issue_name_Label.grid(row=0, column=2, padx=0, pady=0)  
                    else:
                        issue_name_Label = Label(Compatiable_Frame, text = 'Your Motherboard and your Case are not Compatiable')
                        issue_name_Label.config(font = ("Hevetica", 12,))
                        issue_name_Label.grid(row=0, column=2, padx=0, pady=0)
                else:
                    issue_name_Label = Label(Compatiable_Frame, text = 'The GPU is too Large to fit the case')
                    issue_name_Label.config(font = ("Hevetica", 12,))
                    issue_name_Label.grid(row=0, column=2, padx=0, pady=0)
            else:
                issue_name_Label = Label(Compatiable_Frame, text = 'The Motherboard does not have space for this much RAM')
                issue_name_Label.config(font = ("Hevetica", 12,))
                issue_name_Label.grid(row=0, column=2, padx=0, pady=0)
        else:
            issue_name_Label = Label(Compatiable_Frame, text = 'The Ram is not compatiable with the Motherboard')
            issue_name_Label.config(font = ("Hevetica", 12,))
            issue_name_Label.grid(row=0, column=2, padx=0, pady=0)
    else:
        issue_name_Label = Label(Compatiable_Frame, text = 'The CPU and Motherboard are not Compatiable')
        issue_name_Label.config(font = ("Hevetica", 12,))
        issue_name_Label.grid(row=0, column=2, padx=0, pady=0)

    def buyBuild():
       
       #print(id)
       addtoCart(cpu_name, id)
       addtoCart(ram_name, id)
       addtoCart(gpu_name, id)
       addtoCart(mother_name, id)
       addtoCart(case_name, id)
       addtoCart(storage_name, id)
       addtoCart(cooler_name, id)
       addtoCart(power_name, id)
       viewCart(id)

    if cpu_name != 'N/A' and ram_name != 'N/A' and gpu_name != 'N/A' and mother_name != 'N/A' and case_name != 'N/A' and storage_name != 'N/A' and cooler_name != 'N/A' and power_name != 'N/A':
        Buy_Button = Button(Compatiable_Frame, text = "Buy this Build", width = 13, command = buyBuild)
        Buy_Button.grid(row=0, column=2, padx=0, pady=0)
        
    Build.mainloop()

def selectCPU(id):

    Build.destroy()

    cpuroot = Tk()
    cpuroot.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(cpuroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "Number of Cores", "Clock Speed", "Boosted Clock Speed", "Integrated Graphics", "Socket", "Cooler?", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 140)
    my_tree.column("Number of Cores", anchor = CENTER, width = 140)
    my_tree.column("Clock Speed", anchor = CENTER, width = 140)
    my_tree.column("Boosted Clock Speed", anchor = CENTER, width = 140)
    my_tree.column("Integrated Graphics", anchor = CENTER, width = 140)
    my_tree.column("Socket", anchor = CENTER, width = 100)
    my_tree.column("Cooler?", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 100)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Number of Cores", text = "Number of Cores", anchor = CENTER)
    my_tree.heading("Clock Speed", text = "Clock Speed", anchor = CENTER)
    my_tree.heading("Boosted Clock Speed", text = "Boossted Clock Speed", anchor = CENTER)
    my_tree.heading("Integrated Graphics", text = "Integrated Graphics", anchor = CENTER)
    my_tree.heading("Socket", text = "Socket", anchor = CENTER)
    my_tree.heading("Cooler?", text = "Cooler?", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, number_of_cores, clock_speed, boosted_clock_speed, integrated_graphics, socket, cooler, price FROM cpu")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        count += 1
    con.commit()

    button_frame = LabelFrame(cpuroot)
    button_frame.pack(fill="x", expand="yes", padx=500)

    def CPU_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        cpuSelected = values[0]
        global cpu_name
        global cpu_socket
        cpu_name = cpuSelected
        cpu_socket = values[5]
        cpuroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    Select_Button = Button(button_frame, text = "Select", command = CPU_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectRAM(id):

    Build.destroy()

    global ramroot
    ramroot = Tk()
    ramroot.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(ramroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "Type", "Speed", "Modules", "RAM Sticks", "RGB?", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 180)
    my_tree.column("Type", anchor = CENTER, width = 140)
    my_tree.column("Speed", anchor = CENTER, width = 140)
    my_tree.column("Modules", anchor = CENTER, width = 100)
    my_tree.column("RAM Sticks", anchor = CENTER, width = 100)
    my_tree.column("RGB?", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 100)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Type", text = "Number of Cores", anchor = CENTER)
    my_tree.heading("Speed", text = "Clock Speed", anchor = CENTER)
    my_tree.heading("Modules", text = "Modules", anchor = CENTER)
    my_tree.heading("RAM Sticks", text = "RAM Sticks", anchor = CENTER)
    my_tree.heading("RGB?", text = "RGB?", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, type, speed, modules, sticks, rgb, price FROM ram")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        count += 1
    con.commit()

    def RAM_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        ramSelected = values[0]
        global ram_name
        global ram_type
        global ram_sticks
        ram_name = ramSelected
        ram_type = values[1]
        ram_sticks = values[4]
        ramroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

        
    button_frame = LabelFrame(ramroot)
    button_frame.pack(fill="x", expand="yes", padx=500)

    Select_Button = Button(button_frame, text = "Select", command = RAM_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectGPU(id):

    Build.destroy()

    global gpuroot
    gpuroot = Tk()
    gpuroot.geometry('1200x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(gpuroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "Memory", "Clock Speed", "Boosted Clock Speed", "Interface", "Length", "HDMI Ports", "Display Ports", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 250)
    my_tree.column("Memory", anchor = CENTER, width = 100)
    my_tree.column("Clock Speed", anchor = CENTER, width = 100)
    my_tree.column("Boosted Clock Speed", anchor = CENTER, width = 140)
    my_tree.column("Interface", anchor = CENTER, width = 100)
    my_tree.column("Length", anchor = CENTER, width = 100)
    my_tree.column("HDMI Ports", anchor = CENTER, width = 100)
    my_tree.column("Display Ports", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 100)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Memory", text = "Memory", anchor = CENTER)
    my_tree.heading("Clock Speed", text = "Clock Speed", anchor = CENTER)
    my_tree.heading("Boosted Clock Speed", text = "Boossted Clock Speed", anchor = CENTER)
    my_tree.heading("Interface", text = "Interface", anchor = CENTER)
    my_tree.heading("Length", text = "Length", anchor = CENTER)
    my_tree.heading("HDMI Ports", text = "HDMI Ports", anchor = CENTER)
    my_tree.heading("Display Ports", text = "Display Ports", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, memory, clock_speed, boosted_clock_speed, interface, length, hdmi_ports, display_ports, price FROM gpu")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
        count += 1
    con.commit()

    def GPU_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        gpuSelected = values[0]
        global gpu_name
        global gpu_length
        gpu_name = gpuSelected
        gpu_length = values[5]
        gpuroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    button_frame = LabelFrame(gpuroot)
    button_frame.pack(fill="x", expand="yes", padx=500)

    Select_Button = Button(button_frame, text = "Select", command = GPU_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectMotherboard(id):
    
    Build.destroy()

    global motherroot
    motherroot = Tk()
    motherroot.geometry('1400x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(motherroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name","Form Factor", "Socket", "Memory Type", "Memory Slots", "PCI-16?", "Ethernet", "SATA", "USB_2", "USB_3", "Wireless", "RGB?", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 200)
    my_tree.column("Form Factor", anchor = CENTER, width = 100)
    my_tree.column("Socket", anchor = CENTER, width = 100)
    my_tree.column("Memory Type", anchor = CENTER, width = 100)
    my_tree.column("Memory Slots", anchor = CENTER, width = 100)
    my_tree.column("PCI-16?", anchor = CENTER, width = 100)
    my_tree.column("Ethernet", anchor = CENTER, width = 100)
    my_tree.column("SATA", anchor = CENTER, width = 100)
    my_tree.column("USB_2", anchor = CENTER, width = 100)
    my_tree.column("USB_3", anchor = CENTER, width = 100)
    my_tree.column("Wireless", anchor = CENTER, width = 100)
    my_tree.column("RGB?", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 100)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Form Factor", text = "Form Factor", anchor = CENTER)
    my_tree.heading("Socket", text = "Socket", anchor = CENTER)
    my_tree.heading("Memory Type", text = "Memory Type", anchor = CENTER)
    my_tree.heading("Memory Slots", text = "Memory Slots", anchor = CENTER)
    my_tree.heading("PCI-16?", text = "PCI-16?", anchor = CENTER)
    my_tree.heading("Ethernet", text = "Ethernet", anchor = CENTER)
    my_tree.heading("SATA", text = "SATA", anchor = CENTER)
    my_tree.heading("USB_2", text = "USB_2", anchor = CENTER)
    my_tree.heading("USB_3", text = "USB_3", anchor = CENTER)
    my_tree.heading("Wireless", text = "Wireless", anchor = CENTER)
    my_tree.heading("RGB?", text = "RGB?", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, form_factor, socket, memory_type, memory_slots, pci_16, ethernet, sata, usb_2, usb_3, wireless, rgb, price FROM motherboard")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12]), tags=('evenrow',))
        count += 1
    con.commit()

    def Mother_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        motherSelected = values[0]
        global mother_name
        global mother_socket
        global mother_ram_type
        global mother_ram_sticks
        global mother_formfactor
        mother_name = motherSelected
        mother_socket = values[2]
        mother_ram_type = values[3]
        mother_ram_sticks = values[4]
        mother_formfactor = values[1]
        motherroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    button_frame = LabelFrame(motherroot)
    button_frame.pack(fill="x", expand="yes", padx=500)

    Select_Button = Button(button_frame, text = "Select", command = Mother_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectCase(id):

    Build.destroy()

    global caseroot
    caseroot = Tk()
    caseroot.geometry('1800x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(caseroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name","Case Type", "Side Panel", "External Bay", "Internal Bay", "Max GPU Size", "Max Fan Size", "Number of Front Panel Fans", "Number of Top Panel Fans", "Number of Exhaust Panel Fans", "Number of Fans Included", "Max Radiator", "RGB?", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 150)
    my_tree.column("Case Type", anchor = CENTER, width = 100)
    my_tree.column("Side Panel", anchor = CENTER, width = 100)
    my_tree.column("External Bay", anchor = CENTER, width = 100)
    my_tree.column("Internal Bay", anchor = CENTER, width = 100)
    my_tree.column("Max GPU Size", anchor = CENTER, width = 100)
    my_tree.column("Max Fan Size", anchor = CENTER, width = 100)
    my_tree.column("Number of Front Panel Fans", anchor = CENTER, width = 180)
    my_tree.column("Number of Top Panel Fans", anchor = CENTER, width = 180)
    my_tree.column("Number of Exhaust Panel Fans", anchor = CENTER, width = 180)
    my_tree.column("Number of Fans Included", anchor = CENTER, width = 180)
    my_tree.column("Max Radiator", anchor = CENTER, width = 100)
    my_tree.column("RGB?", anchor = CENTER, width = 80)
    my_tree.column("Price", anchor = CENTER, width = 80)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Case Type", text = "Case Type", anchor = CENTER)
    my_tree.heading("Side Panel", text = "Side Panel", anchor = CENTER)
    my_tree.heading("External Bay", text = "External Bay", anchor = CENTER)
    my_tree.heading("Internal Bay", text = "Internal Bay", anchor = CENTER)
    my_tree.heading("Max GPU Size", text = "Max GPU Size", anchor = CENTER)
    my_tree.heading("Max Fan Size", text = "Max Fan Size", anchor = CENTER)
    my_tree.heading("Number of Front Panel Fans", text = "Number of Front Panel Fans", anchor = CENTER)
    my_tree.heading("Number of Top Panel Fans", text = "Number of Top Panel Fans", anchor = CENTER)
    my_tree.heading("Number of Exhaust Panel Fans", text = "Number of Exhaust Panel Fans", anchor = CENTER)
    my_tree.heading("Number of Fans Included", text = "Number of Fans Included", anchor = CENTER)
    my_tree.heading("Max Radiator", text = "Max Radiator", anchor = CENTER)
    my_tree.heading("RGB?", text = "RGB?", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, case_type, side_panel, external_bay, internal_bay, max_gpu_size, max_fan_size, num_front_fan, num_top_fan, num_exhaust_fan, num_fan_included, max_radiator, rgb, price FROM computer_store.case")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13]), tags=('evenrow',))
        count += 1
    con.commit()
    
    def Case_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        caseSelected = values[0]
        global case_name
        global case_gpu_length
        global case_formfactor
        global case_radiator
        case_name = caseSelected
        case_gpu_length = values[5]
        case_formfactor = values[1]
        case_radiator = values[11]
        caseroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    button_frame = LabelFrame(caseroot)
    button_frame.pack(fill="x", expand="yes", padx=500)

    Select_Button = Button(button_frame, text = "Select", command = Case_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectStorage(id):

    Build.destroy()

    global storageroot
    storageroot = Tk()
    storageroot.geometry('800x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(storageroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name","Capacity", "Type", "Form Factor", "Interface", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 150)
    my_tree.column("Capacity", anchor = CENTER, width = 100)
    my_tree.column("Type", anchor = CENTER, width = 100)
    my_tree.column("Form Factor", anchor = CENTER, width = 100)
    my_tree.column("Interface", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 80)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Capacity", text = "Capacity", anchor = CENTER)
    my_tree.heading("Type", text = "Type", anchor = CENTER)
    my_tree.heading("Form Factor", text = "Form Factor", anchor = CENTER)
    my_tree.heading("Interface", text = "Interface", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, capacity, type, form_factor, Interface, price from storage")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
        count += 1
    con.commit()

    def Storage_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        storageSelected = values[0]
        global storage_name
        storage_name = storageSelected
        storageroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    button_frame = LabelFrame(storageroot)
    button_frame.pack(fill="x", expand="yes", padx=200)

    Select_Button = Button(button_frame, text = "Select", command = Storage_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectCooler(id):

    Build.destroy()

    global coolerroot
    coolerroot = Tk()
    coolerroot.geometry('800x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(coolerroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name","Fan RPM", "Type", "Radiator", "Socket", "RGB?", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 150)
    my_tree.column("Fan RPM", anchor = CENTER, width = 100)
    my_tree.column("Type", anchor = CENTER, width = 100)
    my_tree.column("Radiator", anchor = CENTER, width = 100)
    my_tree.column("Socket", anchor = CENTER, width = 100)
    my_tree.column("RGB?", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 80)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Fan RPM", text = "Fan RPM", anchor = CENTER)
    my_tree.heading("Type", text = "Type", anchor = CENTER)
    my_tree.heading("Radiator", text = "Radiator", anchor = CENTER)
    my_tree.heading("Socket", text = "Socket", anchor = CENTER)
    my_tree.heading("RGB?", text = "RGB?", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, fan_rpm, type_of_cooler, Radiator, socket, rgb, price from cooler")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        count += 1
    con.commit()

    def Cooler_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        coolerSelected = values[0]
        global cooler_name
        global cooler_socket
        global cooler_radiator
        cooler_name = coolerSelected
        cooler_socket = values[4]
        cooler_radiator = values[3]
        coolerroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    button_frame = LabelFrame(coolerroot)
    button_frame.pack(fill="x", expand="yes", padx=200)

    Select_Button = Button(button_frame, text = "Select", command = Cooler_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

def selectPower(id):

    Build.destroy()

    global powerroot
    powerroot = Tk()
    powerroot.geometry('800x500')

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")
    style.map("Treeview", background = [("selected", "#347083")])
    
    tree_frame = Frame(powerroot)
    tree_frame.pack(pady = 10)
    
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side = RIGHT, fill = Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set, selectmode = "extended")
    my_tree.pack()
    tree_scroll.config(command = my_tree.yview)

    my_tree['columns'] = ("Name", "Form Factor", "Efficency", "Wattage", "Modular", "Price")
    my_tree.column("#0", width = 0, stretch = NO)
    my_tree.column("Name", anchor = CENTER, width = 150)
    my_tree.column("Form Factor", anchor = CENTER, width = 100)
    my_tree.column("Efficency", anchor = CENTER, width = 100)
    my_tree.column("Wattage", anchor = CENTER, width = 100)
    my_tree.column("Modular", anchor = CENTER, width = 100)
    my_tree.column("Price", anchor = CENTER, width = 80)

    my_tree.heading("#0", text = "", anchor = CENTER)
    my_tree.heading("Name", text = "Name", anchor = CENTER)
    my_tree.heading("Form Factor", text = "Form Factor", anchor = CENTER)
    my_tree.heading("Efficency", text = "Efficency", anchor = CENTER)
    my_tree.heading("Wattage", text = "Wattage", anchor = CENTER)
    my_tree.heading("Modular", text = "Modular", anchor = CENTER)
    my_tree.heading("Price", text = "Price", anchor = CENTER)

    my_tree.tag_configure('oddrow', background = "white")
    my_tree.tag_configure('evenrow', background = "lightblue")

    cursor.execute("SELECT name, form_factor, efficency, wattage, modular, price from powersupply")
    records = cursor.fetchall()
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
        else:
             my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
        count += 1
    con.commit()

    def Power_updateSelection():

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        powerSelected = values[0]
        global power_name
        power_name = powerSelected
        powerroot.destroy()
        Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name, id)

    button_frame = LabelFrame(powerroot)
    button_frame.pack(fill="x", expand="yes", padx=200)

    Select_Button = Button(button_frame, text = "Select", command = Power_updateSelection)
    Select_Button.grid(row = 0, column = 0, padx = 0, pady = 0)

#Global Names
cpu_name = 'N/A'
ram_name = 'N/A'
gpu_name = 'N/A'
mother_name = 'N/A'
case_name = 'N/A'
storage_name = 'N/A'
cooler_name = 'N/A'
power_name = 'N/A'

#Global Conditions to Check

cpu_socket = 'N/A'
mother_socket = 'N/A'

ram_type = 'N/A'
mother_ram_type = 'N/A'

ram_sticks = 0
mother_ram_sticks = 0

gpu_length = 0
case_gpu_length = 0

mother_formfactor = 'N/A'
case_formfactor = 'N/A'
mother_formfactor_num = 0
case_formfactor_num = 0

case_radiator = 0
cooler_radiator = 0

cooler_socket = 'N/A'
#cpu_socket = 'N/A'


#Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name)
