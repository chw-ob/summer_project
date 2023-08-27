import tkinter as tk
from tkinter import messagebox
from chw import *

class Window(object):
    def __init__(self, master):
        self.master = master
        self.can = None
        self.position = [-1,-1]
        self.creat_board()
        self.creat_btn()
        self.player=1
        self.lbl3=[]
    def creat_board(self):
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
        pass

    def save(self):
        Game.save(self.master,self.player)

    def load(self):
        player=Game.load()
        self.update_ob()
        self.setf(player)
    def reset(self):
        Game.reset()
        self.update_ob()
        self.creat_board()
    def setf(self, whof):
        self.reset()
        self.player=whof

        if whof==2:
            self.move(0,True)

    def update_ob(self):
        print("start drawing")
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
        #print("yes")
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
            self.update_ob()
            self.result(self.judge())
            self.player=1
    def judge(self):
        return Game.judge_self()

    def result(self, whow):
        if whow == 1:
            tk.messagebox.showinfo('游戏结束', '恭喜您获胜')
        elif whow == 2:
            tk.messagebox.showinfo('游戏结束', '人机获胜，您失败了')
        elif whow == 3:
            tk.messagebox.showinfo('游戏结束', '平局')


if __name__ == "__main__":
    Game = game()
    ser = search()
    root = tk.Tk()
    root.title('井字棋')
    root.geometry("400x300")
    window = Window(root)
    imag1 = tk.PhotoImage(file='image/image/开始界面2.png')
    imag2 = tk.PhotoImage(file='image/image/圈.png')
    imag3 = tk.PhotoImage(file='image/image/叉.png')
    root.mainloop()