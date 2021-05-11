# from tkinter import *
# from tkinter import ttk
# import os
import PIL
from PIL import ImageTk
from PIL import Image

from Browsing_Catalog import *
from Login_Interface import *
import tkinter as tk

def Exit_Store():
    root.destroy()

def homepage(): #This function will either refresh the Browsing_GUI page or send you back to the Browsing GUI page

    print("Work in Progress")

def Browse_Catalog():
    root.destroy()
    browsing_catalog_choice()

    print("WIP")

def Discussion_Forum():
    print("WIP")

def Browse_Selection(): #This function will send user to the page of the selected part they are looking for

    print("Work in Progress")

def Build_Your_Own(): #This function will launch the build your own PC function

    print("Work in Progress")


def Suggested_PC1(): #This function will show more details on the PC and then output a buy button

    #https://www.newegg.com/abs-ali516/p/N82E16883360116?item=N82E16883360116&source=region&nm_mc=knc-googleadwords-pc&cm_mmc=knc-googleadwords-pc-_-pla-_-gaming+desktop-_-N82E16883360116&gclid=CjwKCAjwm7mEBhBsEiwA_of-THgPH1H0E0dHsiWfBZIeocyQD9S8v1TzcL0BOgJhMCPvuGyQxy3afhoCM2oQAvD_BwE&gclsrc=aw.ds
    print("Work in Progress")
    
def Suggested_PC2(): #This function will show more details on the PC and then output a buy button

    #https://www.newegg.com/ibuypower-arcb-108av2-student-home-office/p/N82E16883227936?item=N82E16883227936&source=region&nm_mc=knc-googleadwords-pc&cm_mmc=knc-googleadwords-pc-_-pla-_-desktop+pc-_-N82E16883227936&gclid=CjwKCAjwm7mEBhBsEiwA_of-THVBPlmjT35oY7IQ1VfhqUXZKBkLmx3NZYpHIo3tlu4tMC_yxRY3gRoCqeYQAvD_BwE&gclsrc=aw.ds
    print("Work in Progress")

def Suggested_PC3(): #This function will show more details on the PC and then output a buy button

    #https://www.newegg.com/skytech-st-shiva-0210-ne/p/N82E16883289096?item=N82E16883289096&source=region&nm_mc=knc-googleadwords-pc&cm_mmc=knc-googleadwords-pc-_-pla-_-gaming+desktop-_-N82E16883289096&gclid=CjwKCAjwm7mEBhBsEiwA_of-TBJZHNAK9s9QARwK6WY-TY3k7cumHqOLZYhI7NmC4TY6_Z_4kxYabBoCX9UQAvD_BwE&gclsrc=aw.ds    print("Work in Progress")
    print("Work in Progress")

def Popular_PC1():
    print("WIP")

def Popular_PC2():
    print("WIP")

def Popular_PC3():
    print("WIP")

def populate(frame, canvas):
    logo_image = tk.PhotoImage(file = 'images/Logo.png')
    logo_canvas = tk.Canvas(frame, height=60, borderwidth=0)
    logo_canvas.image = logo_image
    logo_canvas.create_image(0,10, image=logo_image, anchor='nw')
    logo_canvas.grid(row=0,column=1)
    tk.Button(frame, command=Exit_Store, text="Exit!", borderwidth=0, font=('Helvetica', 12)).grid(row=1, column=1)

    # Browsing
    
    tk.Button(frame, text = "Browse Catalog", command = Browse_Catalog, width=40, font=('Helvetica', 12)).grid(row=2, column=0)

    #Build Your Own
    
    tk.Button(frame, text = "Build Your Own", command = Build_Your_Own, width=40, font=('Helvetica', 12)).grid(row=2, column=1)

    #Login Button

    # Function Login Page is complete but needs to be edited a bit 
    tk.Button(frame, text = "Log_In", command = Login_Page, width = 40, font=('Helvetica', 12)).grid(row=2, column=2)

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

    tk.Button(frame, command=Discussion_Forum, text="Discuss about everything!", borderwidth=0, font=('Helvetica', 12)).grid(row=6, column=1)



def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def create_visitor_home():
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
