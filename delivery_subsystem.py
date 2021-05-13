import tkinter as tk


root = tk.Tk()

root.geometry("500x500")

root.title("Delivery Subsystem")

bidding = tk.Button(text="Available Deliveries to Bid")
bidding.pack()

deliveries = tk.Button(text="Ongoing Deliveries")
deliveries.pack()

