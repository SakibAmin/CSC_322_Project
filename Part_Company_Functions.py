import mysql.connector

#Goal: Create a Function to add a Company to the database
#      Add products that each company are selling

#Connecting to Database
con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)
print ("Connnected")

cursor = con.cursor()

def Register_Companies(): #This function adds a Company to the database 
    email = input("Enter your company email: ")
    cursor.execute("SELECT * FROM Computer_Parts_Companies WHERE email = %s", (email,))
    data = cursor.fetchall()
    if len(data) == 0:
        password_loop = True
        while password_loop == True:
            password1 = input("Enter your password: ")
            password2 = input("Please Confirm password: ")
            if password1 == password2:
                break
            else:
                print("Passwords do not match please try again")
    else:
        print("This email is already in use")
    name = input("Enter Company Name: ")
    cursor.execute("INSERT INTO Computer_Parts_Companies (Company_Name, email, password) VALUES ('{}', '{}', '{}')".format(name, email, password1))
    con.commit()
    print(cursor.rowcount, "record inserted")

def Register_CPU(): #Adds CPU to database

    id = 1 #Must code variable to be linked to the id assigned when signed in

    #Information of CPU
    name = input("Enter the CPU Name: ")
    num_Cores = input("How many cores does the CPU have?: ")
    clock_speed = input("What is the clock speed of the CPU?: ")
    boosted_clock_speed = input("What is the boosted clock speed of the CPU?: ")
    integrated_graphics = input("What type of Integrated Graphics does the CPU have? If it does not have any Integrated Graphics just type in N/A: ")
    Socket = input("What is the socket type for the CPU: ")
    cooler = input("Does the CPU come with a cooler?: ")
    Price = input("What is the  price of the CPU?: ")

    #Query to add to database
    cursor.execute("INSERT INTO CPU (company_id, name, number_of_cores, clock_speed, boosted_clock_speed, integrated_graphics, socket, cooler, price)" + 
    "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, num_Cores, clock_speed, boosted_clock_speed, integrated_graphics, Socket, cooler, Price))
    con.commit()

def Register_RAM(): #Adds Ram to database

    id = 3 #Must code variable to be linked to the id assigned when signed in

    #Information on RAM
    name = input("Enter the RAM Name: ")
    type = input("What type of RAM is it?: ")
    speed = input("What is the RAM speed?: ")
    modules = input("How many modules does the RAM have?: ")
    rgb = input("Does the RAM have RGB?: ")
    Price = input("What is the  price of the RAM?: ")

    #Query to add to database
    cursor.execute("INSERT INTO RAM (company_id, name, type, speed, modules, rgb, price)" +
    "VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(id, name, type, speed, modules, rgb, Price))
    con.commit()

def Register_GPU(): #Adds GPU to database

    id = 6 #Must code variable to be linked to the id assigned when signed in

    #Information on GPU
    name = input("Enter the GPU Name: ")
    memory = input("Enter the amount of memory?: ")
    clock_speed = input("What is the clock speed of the GPU?: ")
    boosted_clock_speed = input("What is the boosted clock speed of the GPU?: ")
    interface = input("What type of interface does the GPU use?: ")
    length = input("What is the length of the GPU?: ")
    hdmi_ports = input("How many HDMI ports does the GPU have?: ")
    display_ports = input("How many Display ports does the GPU have?: ")
    Price = input("What is the  price of the GPU?: ")

    #Query to add to the database
    cursor.execute("INSERT INTO GPU (company_id, name, memory, clock_speed, boosted_clock_speed, interface, length, hdmi_ports, display_ports, price)" +
    "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, memory, clock_speed, boosted_clock_speed, interface, length, hdmi_ports, display_ports, Price))
    con.commit()

def Register_Motherboard(): #Adds motherboard to database

    id = 8 #Must code variable to be linked to the id assigned when signed in

    #Information on Motherboard
    name = input("Enter the Motherboard Name: ")
    form_factor = input("What is the form factor of the motherboard?: ")
    socket = input("What type of socket does the motherboard have?: ")
    memory_type = input("What type of memory does the motherboard use?: ")
    memory_slots = input("How many memory slots does the motherboard have?: ")
    pci_16 = input("Does the motherboard use PCIx16?: ")
    ethernet = input("Does the motherboard support ethernet?: ")
    sata = input("How manny sata ports does the motherboard have?: ")
    usb_2 = input("How many usb 2.0 headers does the motherboard have?: ")
    usb_3 = input("How many usb 3.0 headers does the motherboard have?: ")
    wireless = input("Does the motherboard support wireless connection?: ")
    rgb = input("Does the motherboard have rgb?: ")
    Price = input("What is the  price of the motherboard?: ")

    #Query to add to the database
    cursor.execute("INSERT INTO motherboard (company_id, name, form_factor, socket, memory_type, memory_slots, pci_16, ethernet, sata, usb_2, usb_3, wireless, rgb, price)" +
    "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, form_factor, socket, memory_type, memory_slots, pci_16, ethernet, sata, usb_2, usb_3, wireless, rgb, Price))
    con.commit()

def Register_Cases(): #Adds cases to database
    

    id = 10 #Must code variable to be linked to the id assigned when signed in

    #Information on Case
    name = input("Enter the Case Name: ")
    case_type = input("What is the case type?: ")
    side_panel = input("What is the type of side_panel the case has? If it does not have one write N/A: ")
    external_bay = input("How many external bays does the case have?: ")
    internal_bay = input("How man internal bays does the the case have?: ")
    max_gpu_size = input("What the the maximum gpu size you can fit in the case?: ")
    max_fan_size = input("What is the maximum size of fans that can fit in the case?: ")
    num_front_fan = input("What is the max number of front panel fans you can have?: ")
    num_top_fan = input("What is the maximum number of top panel fans you can have?: ")
    num_exhaust_fan = input("What is the number of exhaust fans the case has?: ")
    num_fan_included = input("How many fans are included in the case?: ")
    max_radiator = input("What is the maximum radiator size?: ")
    rgb = input("Does the case have rgb?: ")
    Price = input("What is the  price of the case?: ")

    #Query to add to the database
    cursor.execute("INSERT INTO case (company_id, name, case_type, side_panel, external_bay, internal_bay, max_gpu_size, max_fan_size, num_front_fan, num_top_fan, num_exhaust_fan, num_fan_included, max_radiator, rgb, price)" +
    "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, case_type, side_panel, external_bay, internal_bay, max_gpu_size, max_fan_size, num_front_fan, num_top_fan, num_exhaust_fan, num_fan_included, max_radiator, rgb, Price))
    con.commit()



con.close()