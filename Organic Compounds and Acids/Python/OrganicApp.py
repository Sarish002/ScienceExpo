import OrgAI
import tkinter
from ttkbootstrap import *

root = Window(themename="vapor")
root.title("chemical.ai")
root.geometry("900x500")
image = tkinter.PhotoImage(file="../Logo.png")
root.iconphoto(False, image)

style = Style()
style.configure("default.TButton", font=("Trebuchet MS", 18))

var = StringVar(root, value="")

entry = Entry(root,
              width=44,
              font=("Trebuchet MS",
                    18),
              bootstyle="success")
entry.place(relx=0.425, rely=0.09, anchor="center")
entry.bind("<Return>", lambda event: Logic()) #NEW!! Useful!

label = Label(text="",
              textvariable=var,
              font=("Trebuchet MS",
                    18),
              width=56)
label.place(relx=0.385, rely=0.18, anchor="n")

def Logic():
    logic = OrgAI.Logic(entry.get())
    var.set(value=logic.strip("\n"))
    label.configure(font=("Trebuchet MS", int(100000 * ((0.5) ** len(logic)))),
                    relief="solid", borderwidth=2, padding=10, justify="left", wraplength=835)
    entry.delete(0, END)

button = Button(root,
                text="Find",
                width=5,
                command=Logic,
                style="default.TButton")
button.place(relx=0.91, rely=0.09, anchor="center")
root.mainloop()