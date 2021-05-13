from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
from Connect_DB import *
from Discussion_Detail import *
from Buy_GUI import *
# from Visitor_Home import create_visitor_home

def browsing_catalog_choice(user_id):
    browse = Tk()
    browse.title('Browsing Catalog')
    browse.geometry('1280x720')

    def return_home():
        print("WIP")
        browse.destroy()
        # go_back_to_logged_home(user_id)

    def go_to_discussion(category, id):
        browse.destroy()
        browse_discussion_detail(id, category, user_id)

    def add_to_cart(category, name):
        # do something with id
        print("buying")
        addtoCart(name, user_id)
        viewCart(user_id)

    def browse_cpu_detail(cpu_name):
        print("WE BROWSIN!!")
        print(cpu_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.cpu WHERE name = '" + cpu_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        cpu_label = Label(detail_frame, text=cpu_name, borderwidth=1, font=('Helvetica', 60)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 30)).pack()

        num_of_cores = "Number of Cores: " + str(data[0][3])
        cores_label = Label(detail_frame, text=num_of_cores, borderwidth=0, font=('Helvetica', 30)).pack()
        
        clock_speed = "Clock Speed: " + data[0][4]
        clock_speed_label = Label(detail_frame, text=clock_speed, borderwidth=0, font=('Helvetica', 30)).pack()
        
        boosted_clock_speed = "Boosted Clock Speed: " + data[0][5]
        boosted_clock_speed_label = Label(detail_frame, text=boosted_clock_speed, borderwidth=0, font=('Helvetica', 30)).pack()
        
        integrated_graphics = "Integrated Graphics: " + data[0][6]
        integrated_graphics_label = Label(detail_frame, text=integrated_graphics, borderwidth=0, font=('Helvetica', 30)).pack()
        
        socket = "Socket: " + data[0][7]
        socket_label = Label(detail_frame, text=socket, borderwidth=0, font=('Helvetica', 30)).pack()
        
        cooling = "Cooling?: " + data[0][8]
        cooling_label = Label(detail_frame, text=cooling, borderwidth=0, font=('Helvetica', 30)).pack()
        
        price = "Price: $" + str(data[0][9])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 30)).pack()

        category = "cpu"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_cpu).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()
    
    def browse_ram_detail(ram_name):
        print("WE BROWSIN!!")
        print(ram_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.ram WHERE name = '" + ram_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ram_label = Label(detail_frame, text=ram_name, borderwidth=1, font=('Helvetica', 60)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 30)).pack()

        type_ram = "Type: " + data[0][3]
        type_label = Label(detail_frame, text=type_ram, borderwidth=0, font=('Helvetica', 30)).pack()

        ram_speed = "Speed: " + str(data[0][4])
        speed_label = Label(detail_frame, text=ram_speed, borderwidth=0, font=('Helvetica', 30)).pack()

        ram_modules = "Modules: " + data[0][5]
        modules_label = Label(detail_frame, text=ram_modules, borderwidth=0, font=('Helvetica', 30)).pack()

        ram_sticks = "Sticks: " + str(data[0][6])
        sticks_label = Label(detail_frame, text=ram_sticks, borderwidth=0, font=('Helvetica', 30)).pack()

        rgb_string = "RGB?: " + data[0][7]
        rgb_label = Label(detail_frame, text=rgb_string, borderwidth=0, font=('Helvetica', 30)).pack()

        price = "Price: $" + str(data[0][8])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 30)).pack()

        category = "ram"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_ram).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_motherboard_detail(motherboard_name):
        print("WE BROWSIN!!")
        print(motherboard_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.motherboard WHERE name = '" + motherboard_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        motherboard_label = Label(detail_frame, text=motherboard_name, borderwidth=1, font=('Helvetica', 50)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        form_factor = "Form Factor: " + data[0][3]
        form_factor_label = Label(detail_frame, text=form_factor, borderwidth=0, font=('Helvetica', 25)).pack()

        socket = "Socket: " + data[0][4]
        socket_label = Label(detail_frame, text=socket, borderwidth=0, font=('Helvetica', 25)).pack()

        memory_type = "Memory Type: " + data[0][5]
        memory_type_label = Label(detail_frame, text=memory_type, borderwidth=0, font=('Helvetica', 25)).pack()

        memory_slots = "Memory Slots: " + str(data[0][6])
        memory_slots_label = Label(detail_frame, text=memory_slots, borderwidth=0, font=('Helvetica', 25)).pack()

        pci = "PCI 16?: " + data[0][7]
        pci_label = Label(detail_frame, text=pci, borderwidth=0, font=('Helvetica', 25)).pack()

        ethernet = "Ethernet?: " + data[0][8]
        ethernet_label = Label(detail_frame, text=ethernet, borderwidth=0, font=('Helvetica', 25)).pack()

        sata = "Sata: " + str(data[0][9])
        sata_label = Label(detail_frame, text=sata, borderwidth=0, font=('Helvetica', 25)).pack()

        usb_2 = "Usb 2: " + str(data[0][10])
        usb_2_label = Label(detail_frame, text=usb_2, borderwidth=0, font=('Helvetica', 25)).pack()

        usb_3 = "Usb 3: " + str(data[0][11])
        usb_3_label = Label(detail_frame, text=usb_3, borderwidth=0, font=('Helvetica', 25)).pack()

        wireless = "Wireless?: " + data[0][12]
        wireless_label = Label(detail_frame, text=wireless, borderwidth=0, font=('Helvetica', 25)).pack()

        rgb_string = "RGB?: " + data[0][13]
        rgb_label = Label(detail_frame, text=rgb_string, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][14])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

        category = "motherboard"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_motherboard).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_gpu_detail(gpu_name):
        print("WE BROWSIN!!")
        print(gpu_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.gpu WHERE name = '" + gpu_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        gpu_label = Label(detail_frame, text=gpu_name, borderwidth=1, font=('Helvetica', 60)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 30)).pack()

        memory = "Memory: " + str(data[0][3])
        memory_level = Label(detail_frame, text=memory, borderwidth=0, font=('Helvetica', 30)).pack()

        clock_speed = "Clock Speed: " + data[0][4]
        clock_speed_label = Label(detail_frame, text=clock_speed, borderwidth=0, font=('Helvetica', 30)).pack()

        boosted_clock_speed = "Boosted Clock Speed: " + data[0][5]
        boosted_clock_speed_label = Label(detail_frame, text=boosted_clock_speed, borderwidth=0, font=('Helvetica', 30)).pack()

        interface = "Interface: " + data[0][6]
        interface_label = Label(detail_frame, text=interface, borderwidth=0, font=('Helvetica', 30)).pack()

        length = "Length: " + str(data[0][7])
        length_label = Label(detail_frame, text=length, borderwidth=0, font=('Helvetica', 30)).pack()

        hdmi_ports = "HDMI Ports: " + str(data[0][8])
        hdmi_ports_label = Label(detail_frame, text=hdmi_ports, borderwidth=0, font=('Helvetica', 30)).pack()

        display_ports = "Display Ports: " + str(data[0][9])
        display_ports_label = Label(detail_frame, text=display_ports, borderwidth=0, font=('Helvetica', 30)).pack()

        price = "Price: $" + str(data[0][10])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 30)).pack()

        category = "gpu"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_GPU).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_case_detail(case_name):
        print("WE BROWSIN!!")
        print(case_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.case WHERE name = '" + case_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        case_label = Label(detail_frame, text=case_name, borderwidth=1, font=('Helvetica', 40)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 20)).pack()

        case_type = "Case Type: " + data[0][3]
        case_type_label = Label(detail_frame, text=case_type, borderwidth=0, font=('Helvetica', 20)).pack()

        side_panel = "Side Panel?: " + data[0][4]
        side_panel_label = Label(detail_frame, text=side_panel, borderwidth=0, font=('Helvetica', 20)).pack()

        external_bay = "Exernal Bays: " + str(data[0][5])
        external_bay_label = Label(detail_frame, text=external_bay, borderwidth=0, font=('Helvetica', 20)).pack()

        internal_bay = "Internal Bays: " + str(data[0][6])
        internal_bay_label = Label(detail_frame, text=internal_bay, borderwidth=0, font=('Helvetica', 20)).pack()

        max_gpu_size = "Max GPU Size: " + str(data[0][7])
        max_gpu_size_label = Label(detail_frame, text=max_gpu_size, borderwidth=0, font=('Helvetica', 20)).pack()

        max_fan_size = "Max Fan Size: " + str(data[0][8])
        max_fan_size_label = Label(detail_frame, text=max_fan_size, borderwidth=0, font=('Helvetica', 20)).pack()

        num_front_fan = "Number of Front Fans: " + str(data[0][9])
        num_front_fan_label = Label(detail_frame, text=num_front_fan, borderwidth=0, font=('Helvetica', 20)).pack()

        num_top_fan = "Number of Top Fans: " + str(data[0][10])
        num_top_fan_label = Label(detail_frame, text=num_top_fan, borderwidth=0, font=('Helvetica', 20)).pack()

        num_exhaust_fan = "Number of Exhaust Fans: " + str(data[0][11])
        num_exhaust_fan_label = Label(detail_frame, text=num_exhaust_fan, borderwidth=0, font=('Helvetica', 20)).pack()

        num_included_fan = "Number of Included Fans: " + str(data[0][12])
        num_included_fan_label = Label(detail_frame, text=num_included_fan, borderwidth=0, font=('Helvetica', 20)).pack()

        max_radiator = "Number of Radiators: " + str(data[0][13])
        max_radiator_label = Label(detail_frame, text=max_radiator, borderwidth=0, font=('Helvetica', 20)).pack()

        rgb_string = "RGB?: " + data[0][14]
        rgb_label = Label(detail_frame, text=rgb_string, borderwidth=0, font=('Helvetica', 20)).pack()

        price = "Price: $" + str(data[0][15])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 20)).pack()

        category = "case"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_case).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_cooler_detail(cooler_name):
        print("WE BROWSIN!!")
        print(cooler_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.cooler WHERE name = '" + cooler_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        case_label = Label(detail_frame, text=cooler_name, borderwidth=1, font=('Helvetica', 60)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        rpm_type = "Fan RPM: " + data[0][3]
        rpm_label = Label(detail_frame, text=rpm_type, borderwidth=0, font=('Helvetica', 25)).pack()

        cooler_type = "Cooler Type: " + data[0][4]
        cooler_type_label = Label(detail_frame, text=cooler_type, borderwidth=0, font=('Helvetica', 25)).pack()

        radiator = "Radiator: " + str(data[0][5])
        radiator_label = Label(detail_frame, text=radiator, borderwidth=0, font=('Helvetica', 25)).pack()

        socket = "Socket: " + data[0][6]
        socket_label = Label(detail_frame, text=socket, borderwidth=0, font=('Helvetica', 25)).pack()

        rgb = "RGB?: " + data[0][7]
        rgb_label = Label(detail_frame, text=rgb, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][8])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

        category = "cooler"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_cpu_cooler).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_storage_detail(storage_name):
        print("WE BROWSIN!!")
        print(storage_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.storage WHERE name = '" + storage_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        storage_label = Label(detail_frame, text=storage_name, borderwidth=1, font=('Helvetica', 60)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        capacity_type = "Capacity: " + data[0][3]
        capacity_label = Label(detail_frame, text=capacity_type, borderwidth=0, font=('Helvetica', 25)).pack()

        storage_type = "Storage Type: " + data[0][4]
        storage_type_label = Label(detail_frame, text=storage_type, borderwidth=0, font=('Helvetica', 25)).pack()

        form_factor = "Form Factor: " + data[0][5]
        form_factor_label = Label(detail_frame, text=form_factor, borderwidth=0, font=('Helvetica', 25)).pack()

        interface = "Interface: " + data[0][6]
        interface_label = Label(detail_frame, text=interface, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][7])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

        category = "Prebuild"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_storage).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_powersupply_detail(ps_name):
        print("WE BROWSIN!!")
        print(ps_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.powersupply WHERE name = '" + ps_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=ps_name, borderwidth=1, font=('Helvetica', 60)).pack()

        company = "Company ID: " + str(data[0][1])
        company_label = Label(detail_frame, text=company, borderwidth=0, font=('Helvetica', 25)).pack()

        form_factor = "Form Factor: " + data[0][3]
        form_factor_label = Label(detail_frame, text=form_factor, borderwidth=0, font=('Helvetica', 25)).pack()

        efficency = "Efficency: " + data[0][4]
        efficency_label = Label(detail_frame, text=efficency, borderwidth=0, font=('Helvetica', 25)).pack()

        wattage = "Wattage: " + str(data[0][5])
        wattage_label = Label(detail_frame, text=wattage, borderwidth=0, font=('Helvetica', 25)).pack()

        modular = "Modular: " + data[0][6]
        modular_label = Label(detail_frame, text=modular, borderwidth=0, font=('Helvetica', 25)).pack()

        price = "Price: $" + str(data[0][7])
        price_label = Label(detail_frame, text=price, borderwidth=0, font=('Helvetica', 25)).pack()

        category = "powersupply"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_power_supply).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_prebuild_detail(prebuild_name):

        print("WE BROWSIN!!")
        print(prebuild_name)
        for child in mainFrame.winfo_children():
            child.destroy()
        sql_query = "SELECT * FROM computer_store.prebuild WHERE name = '" + prebuild_name + "'"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        print(data)
        print(data[0][0])
        detail_frame = Frame(mainFrame, width=728, height=550)
        detail_frame.pack(pady=20, padx=20)

        ps_label = Label(detail_frame, text=prebuild_name, borderwidth=1, font=('Helvetica', 60)).pack()

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

        category = "Prebuild"
        return_to_list_button = Button(detail_frame, text="Return", command=browse_prebuilt).pack()
        go_to_discussion_button = Button(detail_frame, text="Discuss", command=lambda category=category, id=data[0][0]: go_to_discussion(category, id)).pack()
        add_to_cart_button = Button(detail_frame, text="Add to cart", command=lambda category=category, id=data[0][2]: add_to_cart(category, id)).pack()

    def browse_GPU():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM GPU")
        data = cursor.fetchall()
        print(data)
        gpu_frame = Frame(mainFrame, width= 720, height=550)
        gpu_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            gpu_button = Button(gpu_frame, text=name, command=lambda name=name: browse_gpu_detail(name)).pack()
        del data

    def browse_motherboard():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM motherboard")
        data = cursor.fetchall()
        print(data)
        motherboard_frame = Frame(mainFrame, width= 720, height=550)
        motherboard_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            motherboard_button = Button(motherboard_frame, text=name, command=lambda name=name: browse_motherboard_detail(name)).pack()
        del data

    def browse_ram():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM ram")
        data = cursor.fetchall()
        print(data)
        ram_frame = Frame(mainFrame, width= 720, height=550)
        ram_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            ram_button = Button(ram_frame, text=name, command=lambda name=name: browse_ram_detail(name)).pack()
        del data
    
    def browse_cpu():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM cpu")
        data = cursor.fetchall()
        print(data)
        cpu_frame = Frame(mainFrame, width= 720, height=550)
        cpu_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            cpu_button = Button(cpu_frame, text=name, command=lambda name=name: browse_cpu_detail(name)).pack()
        del data

    def browse_case():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM computer_store.case")
        data = cursor.fetchall()
        print(data)
        case_frame = Frame(mainFrame, width= 720, height=550)
        case_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            case = Button(case_frame, text=name, command=lambda name=name: browse_case_detail(name)).pack()
        del data

    def browse_cpu_cooler():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM cooler")
        data = cursor.fetchall()
        print(data)
        cooler_frame = Frame(mainFrame, width= 720, height=550)
        cooler_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            cooler_button = Button(cooler_frame, text=name, command=lambda name=name: browse_cooler_detail(name)).pack()
        del data

    def browse_storage():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM storage")
        data = cursor.fetchall()
        print(data)
        storage_frame = Frame(mainFrame, width= 720, height=550)
        storage_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            storage_button = Button(storage_frame, text=name, command=lambda name=name: browse_storage_detail(name)).pack()
        del data

    def browse_power_supply():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM powersupply")
        data = cursor.fetchall()
        print(data)
        powersupply_frame = Frame(mainFrame, width= 720, height=550)
        powersupply_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            powersupply_button = Button(powersupply_frame, text=name, command=lambda name=name: browse_powersupply_detail(name)).pack()
        del data

    def browse_prebuilt():
        for child in mainFrame.winfo_children():
            child.destroy()
        cursor.execute("SELECT name FROM prebuild")
        data = cursor.fetchall()
        print(data)
        prebuild_frame = Frame(mainFrame, width= 720, height=550)
        prebuild_frame.pack(pady=20, padx=20)
        for item in data:
            print(item)
            print(type(item))
            print(item[0])
            name = item[0]
            powersupply_button = Button(prebuild_frame, text=name, command=lambda name=name: browse_prebuild_detail(name)).pack()
        del data

    def browse_reset():
        for child in mainFrame.winfo_children():
            child.destroy()

    def comboClick(event):
        choice = myCombo.get()
        if choice == "CPU":
            browse_cpu()
        elif choice == "Motherboard":
            browse_motherboard()
        elif choice == "CPU Cooler":
            browse_cpu_cooler()
        elif choice == "RAM":
            browse_ram()
        elif choice == "GPU":
            browse_GPU()
        elif choice == "Case":
            browse_case()
        elif choice == "Storage":
            browse_storage()
        elif choice == "Power Supply":
            browse_power_supply()
        elif choice == "PreBuilt":
            browse_prebuilt()
        else:
            browse_reset()


    browsingOptions = [
        "BROWSE", 
        "CPU", 
        "Motherboard", 
        "CPU Cooler", 
        "RAM", 
        "GPU", 
        "Case", 
        "Storage", 
        "Power Supply",
        "PreBuilt",
    ]

    # clickedOption = StringVar()
    # clickedOption.set(browsingOptions[0])

    # drop_menu = OptionMenu(browse, clickedOption, *browsingOptions, command=selected)
    # drop_menu.pack(pady=20)

    
    #logo_image = PhotoImage(file = 'images/Logo.png')
    #logo_label = Label(image = logo_image)
    
    logo_button = Button(browse, text = 'SMN PARTS', width = 20, height = 5, font = ("Hevetica", 20), command=return_home, borderwidth = 0)
    logo_button.place(x = 640, y = 0)
    logo_button.pack(pady=20, padx=20)


    myCombo = ttk.Combobox(browse, value=browsingOptions)
    myCombo.current(0)
    myCombo.bind("<<ComboboxSelected>>", comboClick)
    myCombo.pack()
    mainFrame = Frame(browse, width= 1280, height=720)
    mainFrame.pack()
    browse.mainloop()
