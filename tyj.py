import tkinter as tk
from tkinter import messagebox


class Window(object):
    def __init__(self, master,imag1):
        self.master = master
        self.can = None
        self.imag1=imag1
        self.can = tk.Canvas(self.master, width=300, height=300)
        self.can.create_line((30, 30), (270, 30), width=2)
        self.can.create_line((270, 30), (270, 270), width=2)
        self.can.create_line((270, 270), (30, 270), width=2)
        self.can.create_line((30, 270), (30, 30), width=2)
        for i in range(3):
            self.can.create_line((30, (i + 1) * 80 + 30), (270, (i + 1) * 80 + 30), width=2)
        for i in range(3):
            self.can.create_line(((i + 1) * 80 + 30, 30), ((i + 1) * 80 + 30, 270), width=2)
        self.can.pack(expand='YES', fill='both')
        self.btn_computer = tk.Button(self.master, text='保存',command=lambda:self.save()).place(x=400,y=0,width=100, height=30)
        self.btn_user = tk.Button(self.master, text='加载').place(x=400,y=100,width=100, height=30)
    def save(self):
        Func_Save
    def action(self,position):
        func_action(position)
        observation=game.get_ob()
        draw(observation)
    # 画叉

if __name__=="__main__":
    root = tk.Tk()
    root.title('井字棋')
    root.geometry("500x300+550+150")
    imag1 = tk.PhotoImage(file='image/开始界面.png')
    Window(root, imag1)
    root.mainloop()