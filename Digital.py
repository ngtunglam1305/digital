from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime as dt

font_size = 50

def clock():
    string = strftime("%I:%M:%S:%p")
    label.config(text = string)
    label.after(1000, clock)
    
    
root = Tk()
root.title("Digital Clock")

root.iconbitmap('Logo.ico')

date = dt.datetime.now()
label = Label(root, background="black",font= ("Digital-7", font_size), foreground="green")
label.pack(anchor='center')
label_2 = Label(root, background= "black", text=f"{date:%A, %B %d, %Y}",font=("digital-7", font_size), foreground="green")
label_2.pack(pady=10,padx=10)

clock()
root.mainloop()