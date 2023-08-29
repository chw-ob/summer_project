import tkinter as tk
import unittest

from tkinter import messagebox
from chw import *

class Window(object):
    '''
        .. automethod:: __init__

        井字棋的窗口类

        程序的入口，合并后的总项目

        属性：
            master:利用tkinter创建的root

            can:利用tkinter创建的canvas

            imag1:游戏最初开始界面所需图像

            position:存储鼠标点击的位置信息


        方法：
           creat_board:创建3*3的棋盘

           creat_btn:创建一系列交互按钮

           quit:退出游戏(用于接收函数)

           save:保存游戏(用于接收函数)

           load:加载之前保存过的游戏(用于接收函数)

           search_history:显示历史步骤

           reset:重新开始(用于接收函数)

           setf:设置先手

           update_ob:处理棋盘data数据,更新棋盘,画出图像

           move:用于获取鼠标信息,更新棋盘data数据

           judge:用于判断游戏进程(用于接受函数),返回一个int值表示游戏进程

           result:若游戏结束,则弹窗提示

        示例：
           window = Window(root, imag1)

           setf(1)

        :noindex:


        .. automethod:: __init__

        '''
    def __init__(self, master):
        """
        初始化

        master:接受外界利用tkinter创建的root
        player:当前下棋方
        be_player:游玩玩家
        can:用于表示在master上创建的画布

        imag1:游戏最初开始界面所需图像

        position:一个一维数组,用于存储鼠标点击的位置信息
            [0,1]表示第一行第二个位置
            [1,2]表示第二行第三个位置
            [2,2]表示第三行第三个位置

        creat_board():初始化游戏棋盘

        creat_btn():初始化游戏功能性按钮
        """
        self.master = master
        self.can = None
        self.position = [-1,-1]
        self.creat_board()
        self.creat_btn()
        self.player=1
        self.be_player=1
        self.lbl3=[]
        self.history=[]
    def creat_board(self):
        '''

        用于创建游戏棋盘

        :return: 没有返回值

        '''
        self.can = tk.Canvas(self.master, width=300, height=300)
        self.can.create_line((30, 30), (270, 30), width=2)
        self.can.create_line((270, 30), (270, 270), width=2)
        self.can.create_line((270, 270), (30, 270), width=2)
        self.can.create_line((30, 270), (30, 30), width=2)
        for i in range(3):
            self.can.create_line((30, (i + 1) * 80 + 30), (270, (i + 1) * 80 + 30), width=2)
        for i in range(3):
            self.can.create_line(((i + 1) * 80 + 30, 30), ((i + 1) * 80 + 30, 270), width=2)
        self.can.pack(expand=True, fill='both')
        self.can.bind('<ButtonRelease-1>', func=self.move)

    def creat_btn(self):
        '''

        用于创建功能按钮

        :return:没有返回值

        '''
        self.btn_save = tk.Button(self.master, text='保存',command=lambda:self.save())\
            .place(x=300,y=30,width=100, height=30)
        self.btn_load = tk.Button(self.master, text='加载',command=lambda :self.load())\
            .place(x=300,y=60,width=100, height=30)
        self.btn_reset = tk.Button(self.master, text='重新开始', command=lambda: self.reset())\
            .place(x=300, y=90, width=100,height=30)
        self.btn_mef = tk.Button(self.master, text='我方先手', command=lambda: self.setf(1))\
            .place(x=300, y=120, width=100,height=30)
        self.btn_aif = tk.Button(self.master, text='人机先手', command=lambda: self.setf(2))\
            .place(x=300, y=150, width=100,height=30)
        self.btn_esc = tk.Button(self.master, text='退出', command=lambda: self.quit()) \
            .place(x=300, y=180, width=100, height=30)
        self.btn_esc = tk.Button(self.master, text='查看历史步骤', command=lambda: self.search_history()) \
            .place(x=300, y=180, width=100, height=30)

    def quit(self):
        """
        用于退出游戏(用于接收函数)

        :return: 没有返回值
        """
        self.master.destroy()
        pass

    def save(self):
        """
        用于保存游戏(用于接收函数)

        :return: 没有返回值
        """
        Game.save(self.player,self.history,self.be_player)
    def search_history(self):
        """
        显示历史步骤
        :return: 没有返回值
        """
        string='你是'
        string +="红方\n" if self.be_player==1 else "黑方\n"
        for i in range(len(self.history)):
            if i%2==0:
                string+="红方:"+"(%d,%d)\n"%(self.history[i][0],self.history[i][1])
            else:
                string+="黑方:"+"(%d,%d)\n"%(self.history[i][0],self.history[i][1])
        tk.messagebox.showinfo("历史步骤",string)
    def load(self):
        """
        加载游戏存档
        :return: 没有返回值
        """
        inf=Game.load()
        player,self.history,self.be_player=inf[0],inf[1],inf[2]
        self.update_ob()
        self.player=player
    def reset(self):
        """
        重置游戏
        :return: 没有返回值
        """
        Game.reset()
        self.player=self.be_player=1
        self.history=[]
        self.update_ob()
        self.creat_board()
    def setf(self, whof):
        """
        设置先手
        :param whof: 先手是谁
        :return:
        """
        self.reset()
        self.player=whof
        self.be_player=whof
        if whof==2:
            self.move(0,True)
    def update_ob(self):
        """
        更新局面
        :return: 没有返回值
        """
        board = Game.get_ob()
        for i in self.lbl3:
            i.destroy()
        self.lbl3=[]
        for i in range(3):
            for j in range(3):
                if board[j][i] == 1:
                    self.lbl3 .append( tk.Label(self.master, image=imag2))
                    self.lbl3[-1].place(x=33 + i * 80, y=30 + j * 80)
                elif board[j][i] == 2:
                    self.lbl3.append(tk.Label(self.master, image=imag3))
                    self.lbl3[-1].place(x=33 + i * 80, y=30 + j * 80)



    def move(self, event,B=False):
        """
        用于获取鼠标信息,更新棋盘data数据

        :param event: 为鼠标信息,通过鼠标信息判断玩家点击位置,进而更新棋盘data数据

        :return: 没有返回值
        """
        if self.player == 1:
            for i in range(30, 191, 80):
                for j in range(30, 191, 80):
                    if j <= event.x < j + 80 and i <= event.y < i + 80:
                        self.position=list(self.position)
                        self.position[0] = i//80
                        self.position[1] = j//80
                        break
            position = self.position
            Game.action(position)
            self.history.append(position)
            self.update_ob()
            self.result(self.judge())
            self.player=2
            self.move(event)
        elif self.player == 2:
            if B == True:
                position=[1,1]
            else:
                position = ser(9, Game)
            if position==None:
                return
            Game.action(position)
            self.history.append(position)
            self.update_ob()
            self.result(self.judge())
            self.player=1
    def judge(self):
        '''

        用于判断游戏进程(用于接收函数)

        :return: 返回一个int值,0:继续,1:player1胜利,2:player2胜利,3:平局

        '''
        return Game.judge_self()

    def result(self, whow):
        '''

        若游戏结束,则弹窗提示

        :param whow: 游戏结束后最终结果,默认:1->玩家胜利 2->人机胜利 3->平局

        :return: 返回值1 2 3用于单元测试

        '''
        #print(whow,self.player)
        if whow==0:
            return
        if whow == 3:
            tk.messagebox.showinfo('游戏结束', '平局')
        elif  whow==self.be_player :
            tk.messagebox.showinfo('游戏结束', '恭喜您获胜')
        elif whow != self.be_player:
            tk.messagebox.showinfo('游戏结束', '人机获胜，您失败了')


if __name__ == "__main__":
    Game = game()
    ser = search()
    root = tk.Tk()
    root.title('井字棋')
    root.geometry("400x300")
    window = Window(root)
    imag1 = tk.PhotoImage(file='summer_project/image/image/开始界面2.png')
    imag2 = tk.PhotoImage(file='summer_project/image/image/圈.png')
    imag3 = tk.PhotoImage(file='summer_project/image/image/叉.png')
    '''imag1 = tk.PhotoImage(file='image/image/开始界面2.png')
    imag2 = tk.PhotoImage(file='image/image/圈.png')
    imag3 = tk.PhotoImage(file='image/image/叉.png')'''
    root.mainloop()