#UI
from tkinter import *
from tkinter import messagebox
from asd import *

root = Tk()
root.geometry("350x420")
root.configure(bg="#009f92")
root.resizable(width=False, height=False)
root.title("Movie Recommendation")
 

def Take_input():
    try:
        Output.configure(state='normal')
        Output.delete('1.0', END)
        INPUT = inputtxt.get("1.0", "end-1c")
        answer = "\n".join(get_recommendations(INPUT, cosine_sim2))
        Output.insert(END, answer)
        Display.configure(state = 'active')
        Output.configure(state='disabled')
        
    except:
        messagebox.showerror("Wrong input", "Please enter a valid name!")
        Output.configure(state='disabled')

l4 = Label(text = "",bg="#009f92")
l = Label(text = "Insert Movie Name", bg="#009f92", fg = "black", font  = 'bold')

inputtxt = Text(root, wrap = NONE ,height = 2,
                width = 35,
                bg = "#f7e7be", borderwidth=1, relief="solid")

l1 = Label(text = "",bg="#009f92")

Output = Text(root, height = 10,
              width = 35,
              bg = "#f7e7be" ,borderwidth=1, relief="solid")

Output.configure(state='disabled')

Display = Button(root, height = 2, bg="#005366", fg ="#f7e7be", activebackground="#003E4D",
                 width = 39,
                 text ="Recommend",
                 command = lambda:Take_input())
l2 = Label(text = "",bg="#009f92")

show_plot = Button(root, bg="#005366", height = 2, fg = "#f7e7be", activebackground="#003E4D",
                 width = 39,
                 text ="Show Top 10 Movies",
                 command = lambda:plot())
l3 = Label(text = "",bg="#009f92")

l4.pack()
l.pack()
inputtxt.pack()
l1.pack()
Display.pack()
l2.pack()
Output.pack()
l3.pack()
show_plot.pack()

root.mainloop()