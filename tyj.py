import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk


class Window(object):
    def __init__(self, master):
        self.master = master
        self.can = None
        self.start_game()

    def start_game(self):
        global imag1, imag2
        self.lf = tk.LabelFrame(self.master)
        self.lbl = tk.Label(self.lf, image=imag1)
        self.lbl.pack()
        self.btn_computer = tk.Button(self.lf, text='电脑先手', command=self.create_board)
        self.btn_computer.place(x=45, y=267)
        self.btn_user = tk.Button(self.lf, text='玩家先手', command=self.create_board)
        self.btn_user.place(x=172, y=267)
        self.lf.pack()

    # 开始游戏界面

    def create_board(self):
        if self.lf:
            self.lf.destroy()
        if self.can:
            self.can.destroy()
        self.can = tk.Canvas(self.master, width=300, height=300)
        self.lbl = tk.Label(self.master, image=imag2)
        self.lbl.place(x=33,y=35)
        self.lbl = tk.Label(self.master, image=imag3)
        self.lbl.place(x=35,y=115)
        self.can.create_line((30, 30), (270, 30), width=2)
        self.can.create_line((270, 30), (270, 270), width=2)
        self.can.create_line((270, 270), (30, 270), width=2)
        self.can.create_line((30, 270), (30, 30), width=2)
        for i in range(3):
            self.can.create_line((30, (i + 1) * 80 + 30), (270, (i + 1) * 80 + 30), width=2)
        for i in range(3):
            self.can.create_line(((i + 1) * 80 + 30, 30), ((i + 1) * 80 + 30, 270), width=2)
        self.can.pack(expand='YES', fill='both')
        self.can.bind("<ButtonRelease-1>", self.circles)
        self.btn1 = tk.Button(self.master, text='重新开始', command=self.create_board)
        self.btn1.place(x=105, y=273)
        self.btn2 = tk.Button(self.master, text='保存')
        self.btn2.place(x=120, y=0)

    # 绘制棋盘

    def circles(self, event):
        for i in range(30, 191, 80):
            for j in range(30, 191, 80):
                if j <= event.x < j + 80 and i <= event.y < i + 80:
                    self.can.create_oval((j, i), (j + 80, i + 80), width=2, outline='red')
                    break

    # 点击画圆

    def forks(self):
        for i in range(30, 191, 80):
            for j in range(30, 191, 80):
                self.can.create_line((j, i), (j + 80, i + 80), width=2, fill='blue')
                self.can.create_line((j, i + 80), (j + 80, i), width=2, fill='blue')
                break
    # 画叉

    def draw(self):




root = tk.Tk()
root.title('井字棋')
root.geometry("300x300+550+150")
imag1 = tk.PhotoImage(file='image/开始界面2.png')
imag2 = tk.PhotoImage(file='image/圈.png')
imag3 = tk.PhotoImage(file='image/叉.png')
Window(root)
root.mainloop()
