import numpy as np
import pickle
import tkinter as tk
from tkinter import filedialog
import os
import tkinter.simpledialog as sd
class game():
    def __init__(self,player=1):#初始化,默认player为1
        self.data=np.zeros([3,3])
        self.player=player
    def action(self,position):#接受一个二维的数组，并将其操作在图片上
        num=[1,2]
        if self.data[position[0],position[1]] not in num:
            self.data[position[0],position[1]]=self.player
            self.player=self.next_player(self.player)
            return 0
        else:
            return "error"
        pass##
    def daction(self,position):
        num=[1,2]
        if self.data[position[0],position[1]] in num:
            self.data[position[0], position[1]]=0
            self.player=self.next_player(self.player)
    def get_ob(self):#获取画面信息，以3*3的信息
        return self.data
        pass
    def judge_self(self):#judge一下游戏是否结束
        return self.judge(self.data)
        pass
    def judge(self,data):
        #0:继续 1:player1胜利 2:player2胜利 3:平局
        is_game_over=False
        winner=None
        for i in range(3):
            if data[i][0]==data[i][1]==data[i][2] !=0:
                is_game_over,winner=True,data[i][0]
        for i in range(3):
            if data[0][i]==data[1][i]==data[2][i] !=0:
                is_game_over,winner=True,data[0][i]
        if data[0][0]==data[1][1]==data[2][2]!=0:
            is_game_over, winner = True, data[0][0]
        if data[2][0]==data[1][1]==data[0][2]!=0:
            is_game_over, winner = True, data[0][2]
        if np.min(self.data)>0:
            return 3
        if is_game_over==True:
            return winner
        return 0

        pass
    def reset(self,player=1):#重置棋局
        self.data=np.zeros([3,3])
        self.player=player
    def save(self,root,player,history,be):#保存
        data=[self.data,self.player,player,history,be]
        def save_file(text):
            file_path="data/"+text+".pkl"
            with open(file_path, 'wb') as f:
                pass
            with open(file_path,"wb") as file:
                pickle.dump(data,file)
        text = sd.askstring("输入框", "请输入存档名字:")
        save_file(text)
    def load(self):#加载
        file_path = os.path.abspath(__file__)
        folder_path = os.path.dirname(file_path)
        file_path = filedialog.askopenfilename(initialdir=folder_path+"\data"
                                                 ,defaultextension=".pkl")
        with open(file_path, 'rb') as file:
            file_contents =pickle.load(file)
        print(file_contents)
        self.data,self.player,player,history,be=file_contents[0],file_contents[1],file_contents[2],file_contents[3],file_contents[4]
        return player,history,be
        pass
    def next_player(self,player):
        play={1:2,2:1}
        return play[player]
class search():
    def __init__(self):
        self.player=None
        pass
    def __call__(self, *args, **kwargs):
        return self.forward(*args,**kwargs)
    def minimax(self,depth,game,is_min):
        if game.judge_self() in [1,2,3] or depth==0:
            return self.evaluate(game)
        if is_min==True:
            max_eval=float('-inf')
            for move in self.get_possible_moves(game):
                game.action(move)
                eval=self.minimax(depth-1,game,False)
                max_eval=max(max_eval,eval)
                game.daction(move)
            return max_eval
        else:
            min_eval=float('inf')
            for move in self.get_possible_moves(game):
                game.action(move)
                eval=self.minimax(depth-1,game,True)
                min_eval=min(min_eval,eval)
                game.daction(move)
            return min_eval
        pass
    def evaluate(self,game):
        score=game.judge_self()
        score_dir={2:{3:0,1:-1,2:1,0:0},1:{3:0,1:1,2:-1,0:0}}
        return score_dir[self.player][score]
        pass
    def get_possible_moves(self,game):
        moves=[]
        data=game.get_ob()
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i,j]==0:
                    moves.append([i,j])
        return moves
        pass
    def get_best_move(self,depth,game):
        best_score=float("-inf")
        best_move=None
        for move in self.get_possible_moves(game):
            game.action(move)
            score=self.minimax(depth,game,False)
            if score>best_score:
                best_score=score
                best_move=move
            game.daction(move)
        return best_move
    def forward(self,*args,**kwargs):
        deepth=args[0]
        game=args[1]
        self.player=game.player
        move=self.get_best_move(deepth,game)
        return move
if __name__=="__main__":
   game=game()
   root = tk.Tk()
   game.load()
