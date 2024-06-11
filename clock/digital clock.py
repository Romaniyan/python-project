import tkinter as tk
import time

#create a function currenttime
def currenttime():
    current_time = time.strftime("%a, %d %b %Y\n%H:%M:%S %p")
    digital_label.config(text=current_time)
    root.after(1000,currenttime)
#create the main display
root =tk.Tk()
root.geometry("650x220")
root.title("Digital Clock")
root.config(bg = "#2C3C3F")
# Create a label to display the time
digital_label =tk.Label(text = "Digital Clock",font = ("digital-7", "59", "bold"),bg = "#2C3C3F",fg = "#CAF6FF" )
digital_label.pack(padx=20, pady=20)
currenttime()
root.mainloop()