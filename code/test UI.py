import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=949
        height=505
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_571=tk.Button(root)
        GButton_571["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_571["font"] = ft
        GButton_571["fg"] = "#000000"
        GButton_571["justify"] = "center"
        GButton_571["text"] = "Button"
        GButton_571.place(x=20,y=50,width=234,height=38)
        GButton_571["command"] = self.GButton_571_command

        GLineEdit_590=tk.Entry(root)
        GLineEdit_590["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_590["font"] = ft
        GLineEdit_590["fg"] = "#333333"
        GLineEdit_590["justify"] = "center"
        GLineEdit_590["text"] = "Entry"
        GLineEdit_590.place(x=20,y=10,width=233,height=30)

        GMessage_92=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_92["font"] = ft
        GMessage_92["fg"] = "#333333"
        GMessage_92["justify"] = "center"
        GMessage_92["text"] = "Message"
        GMessage_92.place(x=20,y=100,width=233,height=245)
    
    def GButton_571_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
