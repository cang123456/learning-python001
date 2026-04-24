from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "点击执行送花"
        self.btn01.grid(row=0, column=0 ,padx=40, pady=40)
        # self.btn01.pack()
        self.btn01["command"] = self.songhua

        self.btn02 = Button(self)
        self.btn02["text"] = "点击退出"
        self.btn02.grid(row=0, column=1 , padx=40, pady=40)
        # self.btn02.pack()
        self.btn02["command"] = self.quit

    def songhua(self):
        messagebox.showinfo("送花", "送给你99朵玫瑰花，祝你开心！")


root = Tk()
root.geometry("400x400+200+200")
root.title = "送花"
app = Application(master=root)

root.mainloop()