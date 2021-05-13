import mysql.connector

#Creation of all the different part types into the database 
#Connecting to Database
con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
        database = "computer_store",
        port = 3306
)
print ("Connnected")

#Creating Parts Table
cursor = con.cursor()

#CPU Table
cursor.execute("CREATE TABLE CPU" +
"(cpu_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"number_of_cores int, clock_speed VARCHAR(225), boosted_clock_speed VARCHAR(255)," + 
"integrated_graphics VARCHAR(255), socket VARCHAR(255), cooler VARCHAR(255), price int," +
"PRIMARY KEY (cpu_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#RAM Table
cursor.execute("CREATE TABLE RAM" +
"(ram_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"type VARCHAR(255), speed int, modules VARCHAR(255), rgb VARCHAR(255), price int," +
"PRIMARY KEY (ram_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#GPU Table
cursor.execute("CREATE TABLE GPU" +
"(gpu_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"memory int, clock_speed VARCHAR(255), boosted_clock_speed VARCHAR(255)," +
"interface VARCHAR(255), length int, hdmi_ports int, display_ports int, price int," +
"PRIMARY KEY (gpu_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#MotherBoard Table
cursor.execute("CREATE TABLE MotherBoard" +
"(motherboard_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"form_factor VARCHAR(255), socket VARCHAR(255), memory_type VARCHAR(255), memory_slots int, pci_16 VARCHAR(255)," +
"ethernet VARCHAR(255), sata int, usb_2 int, usb_3 int, wireless VARCHAR(255), rgb VARCHAR(255), price int," +
"PRIMARY KEY (motherboard_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#Case Table
cursor.execute("CREATE TABLE Cases" +
"(case_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"case_type VARCHAR(255), side_panel VARCHAR(255), external_bay int, internal_bay int, max_gpu_size int," +
"max_fan_size int, num_front_fan int, num_top_fan int, num_exhaust_fan int, num_fan_included int, max_radiator int," +
"rgb VARCHAR(255), price int," +
"PRIMARY KEY (case_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#Storage Table
cursor.execute("CREATE TABLE Storage" +
"(storage_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"capacity VARCHAR(255), type VARCHAR(255), form_factor VARCHAR(255), Interface VARCHAR(255), price int," +
"PRIMARY KEY (storage_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#Cooler Table
cursor.execute("CREATE TABLE Cooler" +
"(cooler_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"fan_rpm VARCHAR(255), type_of_cooler VARCHAR(255), Radiator int, socket VARCHAR(255), rgb VARCHAR(255), price int," +
"PRIMARY KEY (cooler_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#Power Supply Table
cursor.execute("CREATE TABLE PowerSupply" +
"(power_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"form_factor VARCHAR(255), efficency VARCHAR(255), wattage int, modular VARCHAR(255), price int," +
"PRIMARY KEY (power_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")

#PreBuilts
cursor.execute("CREATE TABLE PC" +
"(pc_id int NOT NULL AUTO_INCREMENT, company_id int, name VARCHAR(255)," +
"purpose VARCHAR(255), cpu VARCHAR(255), ram VARCHAR(255), gpu VARCHAR(255), storage VARCHAR(255), powersupply VARCHAR(255), OS VARCHAR(255), keyandmouse VARCHAR(255), " +
"PRIMARY KEY (pc_id), FOREIGN KEY (company_id) REFERENCES Computer_Parts_Companies(company_id))")


con.close()
