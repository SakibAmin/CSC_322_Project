from tkinter import *
from tkinter import ttk
import os
import PIL.Image
import PIL.ImageTk
from Login_Interface import *
from Build_Your_Own_Interface import *
import mysql.connector

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "password",
        database = "computer_store",
        port = 3306
)

print ("Connnected To Database")
cursor = con.cursor()

def Browsing_GUI():

    Home = Tk()
    Home.geometry('1000x1000')

    #ScrollBar
    '''main_frame = Frame(Home)
    main_frame .pack(fill = BOTH, expand = 1)

    my_Canvas = Canvas(main_frame)
    my_Canvas.pack(side = LEFT, fill = BOTH, expand = 1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_Canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    my_Canvas.configure(yscrollcommand = my_scrollbar.set)
    my_Canvas.bind('<Configure>', lambda e: my_Canvas.configure(scrollregion = my_Canvas.bbox("all")))

    second_frame = Frame(my_Canvas)

    my_Canvas.create_window((0,0), window = second_frame, anchor = "nw")'''

    #Home Button
    logo_image = PhotoImage(file = 'Logo.png')
    logo_label = Label(image = logo_image)
    
    logo_button = Button(Home, image = logo_image, command = homepage, borderwidth = 0)
    logo_button.place(x = 0, y = 0)

    #Browsing
    browsingOptions = ["BROWSE", "CPU", "MotherBoard", "CPU Cooler", "RAM", "GPU", "Case", "Storage", "Power Supply"]

    browsing_menu = StringVar()
    browsing_menu.set(browsingOptions[0])

    drop_menu = OptionMenu(Home, browsing_menu, *browsingOptions, command = Browse_Selection)
    drop_menu.config(width = 40, font=('Helvetica', 12))
    drop_menu.place(x = 0, y = 80)


    #Build Your Own
    
    buildPC_button = Button(Home, text = "Build Your Own", command = buildPC)
    buildPC_button.config(width = 40, font=('Helvetica', 12))
    buildPC_button.place(x = 355, y = 80)

    #Login Button
    login_button = Button(Home, text = "Log_In", command = Login_Page) #Function Login Page is complete but needs to be edited a bit 
    login_button.config(width = 40, font=('Helvetica', 12))
    login_button.place(x = 680, y = 80)

    #3 suggested Systems by Store Manager

    sug1_image = PIL.Image.open('Suggested System 1.png')
    resize_sug1 = sug1_image.resize((300,200), PIL.Image.ANTIALIAS)

    sug1_image_resized = PIL.ImageTk.PhotoImage(resize_sug1)
    sug1_Label = Label(image = sug1_image_resized)

    sug1_button = Button(Home, image = sug1_image_resized, command = Suggested_PC1)
    sug1_button.place(x = 40, y = 200)
    

    sug2_image = PIL.Image.open('Suggested System 2.png')
    resize_sug2 = sug2_image.resize((300,200), PIL.Image.ANTIALIAS)

    sug2_image_resized = PIL.ImageTk.PhotoImage(resize_sug2)
    sug2_Label = Label(image = sug2_image_resized)

    sug2_button = Button(Home, image = sug2_image_resized, command = Suggested_PC2)
    sug2_button.place(x = 40, y = 450)
   
    
    sug3_image = PIL.Image.open('Suggested System 3.png')
    resize_sug3 = sug3_image.resize((300,200), PIL.Image.ANTIALIAS)

    sug3_image_resized = PIL.ImageTk.PhotoImage(resize_sug3)
    sug3_Label = Label(image = sug3_image_resized)

    sug3_button = Button(Home, image = sug3_image_resized, command = Suggested_PC3)
    sug3_button.place(x = 40, y = 700)


    #3 most Popular Computers per number of Sales
    Home.mainloop()


def homepage(): #This function will either refresh the Browsing_GUI page or send you back to the Browsing GUI page

    print("Work in Progress")

def Browse_Selection(): #This function will send user to the page of the selected part they are looking for

    print("Work in Progress")

def buildPC():
    
    Build_Your_Own(cpu_name, ram_name, gpu_name, mother_name, case_name, storage_name, cooler_name, power_name)

def Suggested_PC1(): #This function will show more details on the PC and then output a buy button

    #https://www.newegg.com/abs-ali516/p/N82E16883360116?item=N82E16883360116&source=region&nm_mc=knc-googleadwords-pc&cm_mmc=knc-googleadwords-pc-_-pla-_-gaming+desktop-_-N82E16883360116&gclid=CjwKCAjwm7mEBhBsEiwA_of-THgPH1H0E0dHsiWfBZIeocyQD9S8v1TzcL0BOgJhMCPvuGyQxy3afhoCM2oQAvD_BwE&gclsrc=aw.ds
    print("Work in Progress")
    
def Suggested_PC2(): #This function will show more details on the PC and then output a buy button

    #https://www.newegg.com/ibuypower-arcb-108av2-student-home-office/p/N82E16883227936?item=N82E16883227936&source=region&nm_mc=knc-googleadwords-pc&cm_mmc=knc-googleadwords-pc-_-pla-_-desktop+pc-_-N82E16883227936&gclid=CjwKCAjwm7mEBhBsEiwA_of-THVBPlmjT35oY7IQ1VfhqUXZKBkLmx3NZYpHIo3tlu4tMC_yxRY3gRoCqeYQAvD_BwE&gclsrc=aw.ds
    print("Work in Progress")

def Suggested_PC3(): #This function will show more details on the PC and then output a buy button

    #https://www.newegg.com/skytech-st-shiva-0210-ne/p/N82E16883289096?item=N82E16883289096&source=region&nm_mc=knc-googleadwords-pc&cm_mmc=knc-googleadwords-pc-_-pla-_-gaming+desktop-_-N82E16883289096&gclid=CjwKCAjwm7mEBhBsEiwA_of-TBJZHNAK9s9QARwK6WY-TY3k7cumHqOLZYhI7NmC4TY6_Z_4kxYabBoCX9UQAvD_BwE&gclsrc=aw.ds    print("Work in Progress")
    print("Work in Progress")



Browsing_GUI()

con.close()