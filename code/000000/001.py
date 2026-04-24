from tkinter import *
from tkinter import messagebox

root = Tk()


btn01 = Button(root)
btn01["text"] = "sh"
btn01.pack()

def sh(e):
    messagebox.showinfo("Message", "sh")
    print("sh")

btn01.bind("<Button-1>", sh)





root.mainloop()