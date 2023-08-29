
import tkinter as tk
from tkinter import messagebox


import numpy


class Window(object):
    """
      .. automethod:: __init__

      一个井字棋的窗体类

      这个类用于提供井字棋的GUI界面以及下期时的棋子动画效果

      属性：
          board（一个3*3的数组）：用于存储棋盘中的棋子位置信息，然后在指定位置加载棋子图片

      方法：
         start_game：由于加载游戏的开始界面，后续困难回删除这个界面，因为不是很有必要

         create_board：加载棋盘图片，使用栏tkinter库内置的画线功能，力求简约

         creat_chess：加载棋子图片，传入含有棋子信息的board数组后回根据数组内容在指定位置放置棋子

         play：功能测试代码，可以给定一种棋盘情况看看棋子绘制是否符合要求，算是单元测试代码

      .. automethod:: __init__
      """

    def __init__(self, master):
        '''

        初始化

        board：board是一个3*3的数组，其中的值有以下意思
              ''：空
              0：红方
              1：黑方
        '''
        self.master = master
        self.can = None
        self.start_game()
        self.board = [('', '', ''), ('', '', ''), ('', '', '')]

    def start_game(self):
        """

        加载游戏开始界面

        :return: 没有返回值

        """
        global imag1
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
        """

        加载棋盘

        :return: 没有返回值

        """
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
        """

        绘制棋子

        :param board: 一个3*3的数组，代表棋盘的下棋状况

        :return: 没有返回值

        """
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
        """

        单元测试函数

        :param boardcopy：一个3*3的数组，存储了用于测试的棋盘信息，0代表红，1代表黑，''代表未落子

        :return: 没有返回值

        """
        #boardcopy=self.board.copy()
        boardcopy=[('0', '0', '0'), ('1', '1', '0'), ('1', '0', '0')]
        self.creat_chess(boardcopy)
    # 测试函数

if __name__=="__main__":
    root = tk.Tk()
    root.title('井字棋')
    root.geometry("300x300+550+150")
    imag1 = tk.PhotoImage(file='image/开始界面2.png')
    imag2 = tk.PhotoImage(file='image/image/圈.png')
    imag3 = tk.PhotoImage(file='image/image/叉.png')
    Window(root)
    root.mainloop()

