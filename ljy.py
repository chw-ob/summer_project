import tkinter as tk
from tkinter import messagebox
from chw import *
import unittest

class Window(object):
    '''
    .. automethod:: __init__

    井字棋的窗口类

    这个类用于创造进行游戏的窗口界面

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
        '''

        初始化

        master:接受外界利用tkinter创建的root

        can:用于表示在master上创建的画布

        imag1:游戏最初开始界面所需图像

        position:一个一维数组,用于存储鼠标点击的位置信息
            [0,1]表示第一行第二个位置
            [1,2]表示第二行第三个位置
            [2,2]表示第三行第三个位置

        creat_board():初始化游戏棋盘

        creat_btn():初始化游戏功能性按钮
        '''
        self.master = master
        self.can = None
        self.imag1 = tk.PhotoImage(file='image/开始界面.png')
        self.position = [-1,-1]
        self.creat_board()
        self.creat_btn()
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
            .place(x=300, y=200, width=100, height=30)

    def quit(self):
        '''

        用于退出游戏(用于接收函数)

        :return: 没有返回值

        '''

        pass

    def save(self):
        '''

        用于保存游戏(用于接收函数)

        :return: 没有返回值

        '''
        Game.save()

    def load(self):
        '''

        用于加载之前的游戏(用于接收函数)

        :return: 没有返回值

        '''
        Game.load()
        self.update_ob()

    def reset(self):
        '''

        用于重新开始游戏(用于接收函数)

        :return: 没有返回值

        '''
        Game.reset()
        self.update_ob()
        self.creat_board()
    def setf(self, whof):
        '''

        用于设置先手

        :param whof:whof为1默认表示玩家先手,为2默认表示人机先手

        :return:没有返回值

        '''
        Game.player = whof

    def update_ob(self, Game):
        '''

        用于处理棋盘data数据,更新棋盘,画出图像

        :param Game: 用于单元测试，实际使用会删除

        :return: 返回值lst用于单元测试

        '''
        print("start drawing")
        date = Game.get_ob()
        lst = [0, 0]
        for i in range(3):
            for j in range(3):
                if date[i][j] == 1:
                    self.can.create_oval((j*80 +30, i*80 +30), (j*80 + 110, i*80 + 110), width=2, outline='red')
                    lst[0] += 1
                    # draw_cic()
                elif date[i][j] == 2:
                    self.can.create_oval((j*80 +40, i*80 +40), (j*80 + 100, i*80 + 100), width=2, outline='blue')
                    lst[1] +=1
                    # draw_cha()
        return lst

    def move(self, event):
        '''

        用于获取鼠标信息,更新棋盘data数据

        :param event: 为鼠标信息,通过鼠标信息判断玩家点击位置,进而更新棋盘data数据

        :return: 没有返回值

        '''
        #print("yes")
        if Game.player == 1:
            for i in range(30, 191, 80):
                for j in range(30, 191, 80):
                    if j <= event.x < j + 80 and i <= event.y < i + 80:
                        print(event.x, event.y)
                        self.position=list(self.position)
                        self.position[0] = i//80
                        self.position[1] = j//80
                        #print(self.position)
                        break
            position = self.position
            Game.action(position)
            print(Game.get_ob())
            self.update_ob()
            self.result(self.judge())
        elif Game.player == 2:
            position = ser(9, Game)
            Game.action(position)
            print(Game.get_ob())
            self.update_ob()
            self.result(self.judge())
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
        if whow == 1:
            tk.messagebox.showinfo('游戏结束', '恭喜您获胜')
            return 1
        elif whow == 2:
            tk.messagebox.showinfo('游戏结束', '人机获胜，您失败了')
            return 2
        elif whow == 3:
            tk.messagebox.showinfo('游戏结束', '平局')
            return 3

class MyTestCase(unittest.TestCase):
    def test_window_result(self):
        root = tk.Tk()
        window = Window(root)
        an = window.result(1)
        self.assertEqual(an, 1)

    def test_window_update_ob(self):
        root = tk.Tk()
        window = Window(root)
        Game = game()
        Game.action([1, 1])# 玩家先动player=1
        Game.action([0, 1])# 人机再动player=2
        an = window.update_ob(Game)
        self.assertListEqual(an, [1, 1])

if __name__ == "__main__":
    Game = game()
    ser = search()
    root = tk.Tk()
    root.title('井字棋')
    root.geometry("400x300")
    window = Window(root)
    root.mainloop()
    unittest.main()