# Import the required library
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win=Tk()

# Set the geometry
win.geometry("700x350")

def get_input():
   label.config(text=""+text.get(1.0, "end-1c"))

# Add a text widget
text=Text(win, width=80, height=15)
text.insert(END, "")
text.pack()

# Create a button to get the text input
b=ttk.Button(win, text="Print", command=get_input)
b.pack()

# Create a Label widget
label=Label(win, text="", font=('Calibri 15'))
label.pack()

win.mainloop()