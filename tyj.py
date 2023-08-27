
import tkinter as tk
from tkinter import messagebox


import numpy


class Window(object):
    def __init__(self, master):
        self.master = master
        self.can = None
        self.start_game()
        self.board = [('', '', ''), ('', '', ''), ('', '', '')]

    def start_game(self):
        global imag1, imag2
        self.lf = tk.LabelFrame(self.master)
        self.lbl1 = tk.Label(self.lf, image=imag1)
        self.lbl1.pack()
        self.btn_computer = tk.Button(self.lf, text='电脑先手', command=self.create_board)
        self.btn_computer.place(x=45, y=267)
        self.btn_user = tk.Button(self.lf, text='玩家先手')
        self.btn_user.place(x=172, y=267)
        self.lf.pack()
    # 开始游戏界面

    def create_board(self):
        if self.lf:
            self.lf.destroy()
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
        self.btn1 = tk.Button(self.master, text='重新开始', command=self.create_board)
        self.btn1.place(x=105, y=273)
        self.btn2 = tk.Button(self.master, text='保存')
        self.btn2.place(x=120, y=0)
        self.play()
    # 绘制棋盘

    def creat_chess(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j]=='0':
                    self.lbl3 = tk.Label(self.master, image=imag2)
                    self.lbl3.place(x=33+i*80, y=35+j*80)
                elif board[i][j]=='1':
                    self.lbl4 = tk.Label(self.master, image=imag3)
                    self.lbl4.place(x=33+i*80, y=35+j*80)
    # 根据数组画棋子

    def play(self):
        #boardcopy=self.board.copy()
        boardcopy=[('0', '0', '0'), ('1', '1', '0'), ('1', '0', '0')]
        self.creat_chess(boardcopy)
    # 测试函数


root = tk.Tk()
root.title('井字棋')
root.geometry("300x300+550+150")
imag1 = tk.PhotoImage(file='image/开始界面2.png')
imag2 = tk.PhotoImage(file='image/image/圈.png')
imag3 = tk.PhotoImage(file='image/image/叉.png')
Window(root)
root.mainloop()

