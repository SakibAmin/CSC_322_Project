# from tkinter import *
# from tkinter import ttk
# import os
import PIL
from PIL import ImageTk
from PIL import Image

from Visitor_Catalog import *
# from Login_Interface import Login_Page
import tkinter as tk



def create_visitor_home():
    def Exit_Store():
        root.destroy()

    def homepage(): #This function will either refresh the Browsing_GUI page or send you back to the Browsing GUI page

        print("Work in Progress")

    def Log_Out():
        print("logout")

    def Browse_Catalog():
        root.destroy()
        id=0
        browsing_catalog_choice(id)

        print("WIP")

    def Discussion_Forum():
        print("WIP")

    def Browse_Selection(): #This function will send user to the page of the selected part they are looking for

        print("Work in Progress")

    def Build_Your_Own(): #This function will launch the build your own PC function

        print("Work in Progress")


    def Suggested_PC1(): #This function will show more details on the PC and then output a buy button


        pc1 = Tk()
        pc1.title('Suggested PC1')
        pc1.geometry('500x500')
        
        prebuild_name = 'ABS Challenger Gaming PC - Ryzen 5 3600 - GeForce GTX 1650 - 16GB DDR4 3000MHz - 512GB SSD'
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(pc1, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 30)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        cpu = "CPU: " + data[0][3]
        cpu_label = Label(detail_frame, text=cpu, borderwidth=0, font=('Helvetica', 25)).pack()

        ram = "RAM: " + data[0][4]
        ram_label = Label(detail_frame, text=ram, borderwidth=0, font=('Helvetica', 25)).pack()

        gpu = "GPU: " + str(data[0][5])
        gpu = Label(detail_frame, text=gpu, borderwidth=0, font=('Helvetica', 25)).pack()

        storage = "Storage: " + data[0][6]
        storage_label = Label(detail_frame, text=storage, borderwidth=0, font=('Helvetica', 25)).pack()

        power = "Power Supply: " + data[0][7]
        power_label = Label(detail_frame, text=power, borderwidth=0, font=('Helvetica', 25)).pack()

        os = "Operating System: " + data[0][8]
        os_label = Label(detail_frame, text=os, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

        
    def Suggested_PC2(): #This function will show more details on the PC and then output a buy button

        pc1 = Tk()
        pc1.title('Suggested PC1')
        pc1.geometry('500x500')
        
        prebuild_name = 'ABS Challenger Gaming PC - Intel i5 10400F - GeForce GTX 1660 Super - 16GB DDR4 - 512GB Intel M.2 NVMe SSD'
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(pc1, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 30)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        cpu = "CPU: " + data[0][3]
        cpu_label = Label(detail_frame, text=cpu, borderwidth=0, font=('Helvetica', 25)).pack()

        ram = "RAM: " + data[0][4]
        ram_label = Label(detail_frame, text=ram, borderwidth=0, font=('Helvetica', 25)).pack()

        gpu = "GPU: " + str(data[0][5])
        gpu = Label(detail_frame, text=gpu, borderwidth=0, font=('Helvetica', 25)).pack()

        storage = "Storage: " + data[0][6]
        storage_label = Label(detail_frame, text=storage, borderwidth=0, font=('Helvetica', 25)).pack()

        power = "Power Supply: " + data[0][7]
        power_label = Label(detail_frame, text=power, borderwidth=0, font=('Helvetica', 25)).pack()

        os = "Operating System: " + data[0][8]
        os_label = Label(detail_frame, text=os, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

    def Suggested_PC3(): #This function will show more details on the PC and then output a buy button

        pc1 = Tk()
        pc1.title('Suggested PC1')
        pc1.geometry('500x500')
        
        prebuild_name = 'Skytech Shiva - AMD Ryzen 5 5600X - RTX 3080 - 16 GB DDR4 3200 - 1 TB SSD - B550M - 750W Gold PSU - AC WiFi - Windows 10 Home - Gaming Desktop'
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(pc1, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 30)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        cpu = "CPU: " + data[0][3]
        cpu_label = Label(detail_frame, text=cpu, borderwidth=0, font=('Helvetica', 25)).pack()

        ram = "RAM: " + data[0][4]
        ram_label = Label(detail_frame, text=ram, borderwidth=0, font=('Helvetica', 25)).pack()

        gpu = "GPU: " + str(data[0][5])
        gpu = Label(detail_frame, text=gpu, borderwidth=0, font=('Helvetica', 25)).pack()

        storage = "Storage: " + data[0][6]
        storage_label = Label(detail_frame, text=storage, borderwidth=0, font=('Helvetica', 25)).pack()

        power = "Power Supply: " + data[0][7]
        power_label = Label(detail_frame, text=power, borderwidth=0, font=('Helvetica', 25)).pack()

        os = "Operating System: " + data[0][8]
        os_label = Label(detail_frame, text=os, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

    def Popular_PC1():
       
        pc1 = Tk()
        pc1.title('Suggested PC1')
        pc1.geometry('500x500')
        
        prebuild_name = 'Dell Inspiron 3880 Desktop, 10th Gen Intel Core i5-10400 6-Core Processor,12GB DDR4,256GB SSD Plus 1TB HDD,Intel UHD Graphics 630, DVD-RW, Wifi-AC, Bluetooth, USB,HDMI,VGA, Windows 10 Home'
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(pc1, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 30)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        cpu = "CPU: " + data[0][3]
        cpu_label = Label(detail_frame, text=cpu, borderwidth=0, font=('Helvetica', 25)).pack()

        ram = "RAM: " + data[0][4]
        ram_label = Label(detail_frame, text=ram, borderwidth=0, font=('Helvetica', 25)).pack()

        gpu = "GPU: " + str(data[0][5])
        gpu = Label(detail_frame, text=gpu, borderwidth=0, font=('Helvetica', 25)).pack()

        storage = "Storage: " + data[0][6]
        storage_label = Label(detail_frame, text=storage, borderwidth=0, font=('Helvetica', 25)).pack()

        power = "Power Supply: " + data[0][7]
        power_label = Label(detail_frame, text=power, borderwidth=0, font=('Helvetica', 25)).pack()

        os = "Operating System: " + data[0][8]
        os_label = Label(detail_frame, text=os, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

    def Popular_PC2():
       
        pc1 = Tk()
        pc1.title('Suggested PC1')
        pc1.geometry('500x500')
        
        prebuild_name = 'iBUYPOWER - Ryzen 3 3100 - 8 GB DDR4 - 1 TB HDD - GeForce GT 710 - Windows 10 Home - Desktop PC (ARCB 108AV2)'
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(pc1, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 30)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        cpu = "CPU: " + data[0][3]
        cpu_label = Label(detail_frame, text=cpu, borderwidth=0, font=('Helvetica', 25)).pack()

        ram = "RAM: " + data[0][4]
        ram_label = Label(detail_frame, text=ram, borderwidth=0, font=('Helvetica', 25)).pack()

        gpu = "GPU: " + str(data[0][5])
        gpu = Label(detail_frame, text=gpu, borderwidth=0, font=('Helvetica', 25)).pack()

        storage = "Storage: " + data[0][6]
        storage_label = Label(detail_frame, text=storage, borderwidth=0, font=('Helvetica', 25)).pack()

        power = "Power Supply: " + data[0][7]
        power_label = Label(detail_frame, text=power, borderwidth=0, font=('Helvetica', 25)).pack()

        os = "Operating System: " + data[0][8]
        os_label = Label(detail_frame, text=os, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

    def Popular_PC3():
        
        pc1 = Tk()
        pc1.title('Suggested PC1')
        pc1.geometry('500x500')
        
        prebuild_name = 'Lenovo ThinkStation P330 Desktop, Intel Core i5-9500 Upto 4.4GHz, 16GB RAM, 512GB SSD, DVDRW, DisplayPort, Wi-Fi, Bluetooth, Windows 10 Pro'
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(pc1, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 30)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        cpu = "CPU: " + data[0][3]
        cpu_label = Label(detail_frame, text=cpu, borderwidth=0, font=('Helvetica', 25)).pack()

        ram = "RAM: " + data[0][4]
        ram_label = Label(detail_frame, text=ram, borderwidth=0, font=('Helvetica', 25)).pack()

        gpu = "GPU: " + str(data[0][5])
        gpu = Label(detail_frame, text=gpu, borderwidth=0, font=('Helvetica', 25)).pack()

        storage = "Storage: " + data[0][6]
        storage_label = Label(detail_frame, text=storage, borderwidth=0, font=('Helvetica', 25)).pack()

        power = "Power Supply: " + data[0][7]
        power_label = Label(detail_frame, text=power, borderwidth=0, font=('Helvetica', 25)).pack()

        os = "Operating System: " + data[0][8]
        os_label = Label(detail_frame, text=os, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

    def populate(frame, canvas):
        logo_image = tk.PhotoImage(file = 'images/Logo.png')
        logo_canvas = tk.Canvas(frame, height=60, borderwidth=0)
        logo_canvas.image = logo_image
        logo_canvas.create_image(0,10, image=logo_image, anchor='nw')
        logo_canvas.grid(row=0,column=1)
        tk.Button(frame, command=Exit_Store, text="Exit!", borderwidth=0, font=('Helvetica', 12)).grid(row=1, column=1)

        # Browsing
        
        tk.Button(frame, text = "Browse Catalog", command = Browse_Catalog, width=40, font=('Helvetica', 12)).grid(row=2, column=0)

        #Log Out
        
        tk.Button(frame, text = "Log_Out", command = Log_Out, width=40, font=('Helvetica', 12)).grid(row=2, column=1)

        #Login Button

        # Function Login Page is complete but needs to be edited a bit 
        # tk.Button(frame, text = "Log_In", command = Login_Page, width = 40, font=('Helvetica', 12)).grid(row=2, column=2)

        #3 suggested Systems by Store Manager

        sug1_img = tk.PhotoImage(file = 'images/suggested-system-1.png')
        sug_pc1_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        sug_pc1_canvas.image = sug1_img
        sug_pc1_canvas.create_image(0,10, image=sug1_img, anchor='nw')
        sug_pc1_canvas.grid(row=3,column=0)

        tk.Button(frame, command=Suggested_PC1, text="Suggested System 1", borderwidth=0, font=('Helvetica', 12)).grid(row=4, column=0)

        sug2_img = tk.PhotoImage(file = 'images/suggested-system-2.png')
        sug_pc2_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        sug_pc2_canvas.image = sug2_img
        sug_pc2_canvas.create_image(0,10, image=sug2_img, anchor='nw')
        sug_pc2_canvas.grid(row=5,column=0)

        tk.Button(frame, command=Suggested_PC2, text="Suggested System 2", borderwidth=0, font=('Helvetica', 12)).grid(row=6, column=0)

        sug3_img = tk.PhotoImage(file = 'images/suggested-system-3.png')
        sug_pc1_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        sug_pc1_canvas.image = sug3_img
        sug_pc1_canvas.create_image(0,10, image=sug3_img, anchor='nw')
        sug_pc1_canvas.grid(row=7,column=0)

        tk.Button(frame, command=Suggested_PC3, text="Suggested System 3", borderwidth=0, font=('Helvetica', 12)).grid(row=8, column=0)

        # Popular Systems

        pop1_img = tk.PhotoImage(file = 'images/suggested-system-1.png')
        pop_pc1_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        pop_pc1_canvas.image = pop1_img
        pop_pc1_canvas.create_image(0,10, image=pop1_img, anchor='nw')
        pop_pc1_canvas.grid(row=3,column=2)

        tk.Button(frame, command=Popular_PC1, text="Popular System 1", borderwidth=0, font=('Helvetica', 12)).grid(row=4, column=2)

        pop2_img = tk.PhotoImage(file = 'images/suggested-system-2.png')
        pop_pc2_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        pop_pc2_canvas.image = pop2_img
        pop_pc2_canvas.create_image(0,10, image=pop2_img, anchor='nw')
        pop_pc2_canvas.grid(row=5,column=2)

        tk.Button(frame, command=Popular_PC2, text="Popular System 2", borderwidth=0, font=('Helvetica', 12)).grid(row=6, column=2)

        pop3_img = tk.PhotoImage(file = 'images/suggested-system-3.png')
        pop_pc1_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        pop_pc1_canvas.image = pop3_img
        pop_pc1_canvas.create_image(0,10, image=pop3_img, anchor='nw')
        pop_pc1_canvas.grid(row=7,column=2)

        tk.Button(frame, command=Popular_PC3, text="Popular System 3", borderwidth=0, font=('Helvetica', 12)).grid(row=8, column=2)

        # Build your own pc!

        byp_img = tk.PhotoImage(file = 'images/build-your-pc.png')
        byp_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        byp_canvas.image = byp_img
        byp_canvas.create_image(0,10, image=byp_img, anchor='nw')
        byp_canvas.grid(row=3,column=1)

        tk.Button(frame, command=Build_Your_Own, text="Build your own PC!", borderwidth=0, font=('Helvetica', 12)).grid(row=4, column=1)

        # Browse our Discussion boards!

        discuss_img = tk.PhotoImage(file = 'images/discuss.png')
        discuss_canvas = tk.Canvas(frame, height=400, borderwidth=0)
        discuss_canvas.image = discuss_img
        discuss_canvas.create_image(0,10, image=discuss_img, anchor='nw')
        discuss_canvas.grid(row=5,column=1)

        # tk.Button(frame, command=Discussion_Forum, text="Discuss about everything!", borderwidth=0, font=('Helvetica', 12)).grid(row=6, column=1)



    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))



    root = tk.Tk()
    root.title('Home Page')
    canvas = tk.Canvas(root, height=720, width=950)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame, canvas)

    root.mainloop()

# root = tk.Tk()
# root.title('Home Page')
# canvas = tk.Canvas(root, height=720, width=950)
# frame = tk.Frame(canvas)
# vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)

# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")

# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame, canvas)

# root.mainloop()
