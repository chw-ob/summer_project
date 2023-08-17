import tkinter as tk
from tkinter import messagebox


class Window(object):
    def __init__(self, master):
        self.master = master
        self.can = None
        self.start_game()

    def start_game(self):
        global imag1
        self.lf = tk.LabelFrame(self.master)
        self.lbl = tk.Label(self.lf, image=imag1)
        self.lbl.pack()
        self.btn_computer = tk.Button(self.lf, text='电脑先手', command=self.create_board)
        self.btn_computer.place(x=40, y=0)
        self.btn_user = tk.Button(self.lf, text='玩家先手', command=self.create_board)
        self.btn_user.place(x=160, y=0)
        self.lf.pack()
    # 开始游戏

    def create_board(self):
        if self.lf:
            self.lf.destroy()
        if self.can:
            self.can.destroy()
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
        self.can.bind("<ButtonRelease-1>", self.circles)
        self.btn1 = tk.Button(self.master, text='重新开始', command=self.create_board)
        self.btn1.place(x=105, y=273)
        self.btn2 = tk.Button(self.master, text='保存', command=self.save)
        self.btn2.place(x=120, y=0)
    # 画布绘制

    def save(self):
        {

        }
    # 保存函数

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


root = tk.Tk()
root.title('井字棋')
root.geometry("300x300+550+150")
imag1 = tk.PhotoImage(file='image/开始界面.png')
imag2 = tk.PhotoImage(file='image/开始按钮.png')
Window(root)
root.mainloop()
