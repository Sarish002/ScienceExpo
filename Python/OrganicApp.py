import OrgAI
import tkinter
from ttkbootstrap import *

root = Window(themename="solar")
root.title("chemical.ai")
root.geometry("900x450")
image = tkinter.PhotoImage(file="Logo.png")
root.iconphoto(False, image)

style = Style()
style.configure("default.TButton", font=("Trebuchet MS", 18))

entry = Entry(root,
              width=24,
              font=("Trebuchet MS",
                    18),
              bootstyle="success")
entry.place(relx=0.41, rely=0.18, anchor="center")
label = Label(text="",
              font=("Trebuchet MS",
                    18))
label.place(relx=0.5, rely=0.29, anchor="n")
def Logic():
    logic = OrgAI.Logic(entry.get())
    label.configure(text=logic, font=("Trebuchet MS", int(10000 * ((0.5) ** len(logic)))),
                    relief="solid", borderwidth=2, padding=10, justify="left")
button = Button(root,
                text="Find",
                width=5,
                command=Logic,
                style="default.TButton")
button.place(relx=0.73, rely=0.18, anchor="center")
root.mainloop()
