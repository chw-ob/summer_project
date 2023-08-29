import numpy as np
import pickle
import tkinter as tk
from tkinter import filedialog
import os
import tkinter.simpledialog as sd
import unittest
class game():
    """

    .. automethod:: __init__

    一个井字棋的环境类

    这个类用于提供游玩井字棋的环境，也即提供存储棋局信息，与棋局进行交互（下棋），进行相关操作（判定胜利，清空棋局）等功能

    属性：
        data（一个3*3的数组）：用于存储棋盘中的棋子位置

        player：表示当前下一步棋是谁写，1代表红方，2代表黑方

    方法：
       action：下棋

       daction：将某个位置下的棋退回，主要用于算法编写

       get_ob:返回data属性

       judge_self：对当前局面进行考察，看是否平局，或者其他情况

       judge：对输入的局面进行考察

       reset:重置整个棋局

       save：保存棋局文件

       load：加载棋局文件

       next_player：表示下一个游玩者是谁


    示例：
       mygame=game()

       mygame.action([1,1])

       judge=mygame.judge_self()

    :noindex:


    .. automethod:: __init__
    """
    def __init__(self):#初始化,默认player为1
        '''

        初始化

        data：data是一个3*3的数组，其中的值有以下意思
              0：空
              1：红方
              2：黑方
        '''
        self.data=np.zeros([3,3])
        self.player=1
    def action(self,position):#接受一个二维的数组，并将其操作在图片上
        """
        用于下一步棋

        :param position: 一个大小为2的数组，代表在下标为相应的位置下一步棋，比如【1,2】代表在data【1,2】下一棋

        :return: 如果下的位置合法:返回0，如果不合法：返回字符串：“error”

        """
        num=[1,2]
        if self.data[position[0],position[1]] not in num:
            self.data[position[0],position[1]]=self.player
            self.player=self.next_player(self.player)
            return 0
        else:
            return "error"
        pass##
    def daction(self,position):
        """

        将棋局某个地方的棋退回

        :param position: 一个大小为2的数组，代表在下标为相应的位置退一步棋，比如【1,2】代表在data【1,2】置零

        :return: 没有返回值

        """
        num=[1,2]
        if self.data[position[0],position[1]] in num:
            self.data[position[0], position[1]]=0
            self.player=self.next_player(self.player)
    def get_ob(self):#获取画面信息，以3*3的信息
        """

        :return: 返回data(3*3的数组)

        """
        return self.data
        pass
    def judge_self(self):#judge一下游戏是否结束
        """

        :return: 返回当前局面游戏结果（0:继续 1:player1胜利 2:player2胜利 3:平局）

        """
        return self.judge(self.data)
        pass
    def judge(self,data):
        """

        :param data: 即局面，一个合适的例子就是self.data

        :return: 返回输入的局面的游戏结果（0:继续 1:player1胜利 2:player2胜利 3:平局）

        """
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
    def reset(self):#重置棋局
        """

        重置游戏局面

        :return:没有返回值

        """
        self.data=np.zeros([3,3])
        self.player=1
    def save(self,inf):#保存
        """

        保存文件

        :param pre_player:当前下棋的人(外部环境),仅用于保存

        :param history: 游玩的历史步骤

        :param player: 游玩棋局游戏的玩家，比如人机对战，若是人先手，则是1，否则则是2

        :return: 没有返回值

        """
        data=[self.data,self.player,inf]
        def save_file(text):
            file_path="data/"+text+".pkl"
            with open(file_path, 'wb') as f:
                pass
            with open(file_path,"wb") as file:
                pickle.dump(data,file)
        text = sd.askstring("输入框", "请输入存档名字:")
        save_file(text)
    def load(self):#加载
        """

        :return:返回保存时载入的额外信息

        """
        file_path = os.path.abspath(__file__)
        folder_path = os.path.dirname(file_path)
        file_path = filedialog.askopenfilename(initialdir=folder_path+"\data"
                                                 ,defaultextension=".pkl")
        with open(file_path, 'rb') as file:
            file_contents =pickle.load(file)
        #print(file_contents)
        self.data,self.player,inf=file_contents[0],file_contents[1],file_contents[2]
        return inf
        pass
    def next_player(self,player):
        """

        返回下一次的棋手

        :param player: 当前棋局的棋手

        :return: 下一位棋手

        """
        play={1:2,2:1}
        return play[player]
class search():
    """
    一个用于ai下棋的类

    属性：
       player：当前下棋的人

    方法：

       minimax：主要算法，用于计算下一步的最优解

       evaluate：评估当前局面的得分

       get_possible_moves：获得下一步棋可以下的位置集合

       get_best_move：获得最佳的效果

       forward：直接由局面得到ai的解，也即这个类直接调用的方法

    例子：

    mygame=game()

    Search=search()

    position=Search(depth,game)
    """
    def __init__(self):
        self.player=None
        pass
    def __call__(self, *args, **kwargs):
        """

        将call函数直接设置成forward函数

        :param args: forward函数的参数
        :param kwargs: 无
        :return: 无返回值
        """
        return self.forward(*args,**kwargs)
    def minimax(self,depth,game,is_min):
        """

        极大极小值运算方法

        :param depth: 一个参数，深度优先搜索的深度(表征机器的智能程度），井字棋最智能为9

        :param game: 即环境，就是class chw.game

        :param is_min:一个算法的参数，表征

        :return: 返回一个大小为2的数组
        """
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
        """


        :param game: 即环境，就是class chw.game

        :return: 返回对当前局面的评估分数

        """
        score=game.judge_self()
        score_dir={2:{3:0,1:-1,2:1,0:0},1:{3:0,1:1,2:-1,0:0}}
        return score_dir[self.player][score]
        pass
    def get_possible_moves(self,game):
        """

        获取当前局面所有可能可以下棋的位置

        :param game: 即环境，就是class chw.game

        :return: 返回一个列表，列表里的每个元素都是一个大小为2的list，代表位置

        """
        moves=[]
        data=game.get_ob()
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i,j]==0:
                    moves.append([i,j])
        return moves
        pass
    def get_best_move(self,depth,game):
        """

        获取当前局面最好的位置

        :param game: 即环境，就是class chw.game

        :return: 返回一个大小为2的list，代表位置

        """
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
        """

        :param args: 两个参数，game和depth，game就是chw:class game的实例，depth就是智能体的智能程度，难度从1-9变化

        :param kwargs: 无

        :return: 返回最佳的位置

        """
        deepth=args[0]
        game=args[1]
        self.player=game.player
        move=self.get_best_move(deepth,game)
        return move
"""

    .. automethod:: MyTestCase
"""
class MyTestCase(unittest.TestCase):
    """

    单元测试代码，仅做测试用

    """
    def test_game_get_ob(self):
        """

        单元测试代码

        :return:

        .. automethod::test_game_get_ob
        """
        Game = game()
        #Game.action([1, 1])
        inf = Game.get_ob()
        YAN = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        ans = (inf == YAN).all()
        self.assertTrue(ans)
    def test_game_action(self):
        Game=game()
        Game.action([1,1])
        inf=Game.get_ob()
        YAN=np.array([[0,0,0],[0,1,0],[0,0,0]])
        ans=(inf==YAN).all()
        self.assertTrue(ans)
    def test_game_daction(self):
        Game = game()
        Game.action([1, 1])
        Game.daction([1,1])
        inf = Game.get_ob()
        YAN = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        ans = (inf == YAN).all()
        self.assertTrue(ans, 2)
    def test_judge_self(self):#judge一下游戏是否结束
        Game=game()
        Game.action([1,1])
        Game.action([0,0])
        Game.action([1, 0])
        ans1 = Game.judge_self()
        self.assertEqual(ans1, 0)
        Game.action([0, 1])
        Game.action([1, 2])
        ans1=Game.judge_self()
        self.assertEqual(ans1,1)
        pass
    def test_judge(self):
        Game = game()
        Game.action([1, 1])
        Game.action([0, 0])
        Game.action([1, 0])
        inf=Game.get_ob()
        ans1 = Game.judge(inf)
        self.assertEqual(ans1, 0)
        Game.action([0, 1])
        Game.action([1, 2])
        inf = Game.get_ob()
        ans1 = Game.judge(inf)
        self.assertEqual(ans1, 1)

        pass
    def test_reset(self):
        Game = game()
        Game.action([1, 1])
        Game.action([0, 0])
        Game.action([1, 0])
        Game.reset()
        inf=Game.get_ob()
        ans=(inf==np.zeros([3,3])).all()
        self.assertTrue(ans)
    def test_next_player(self):
        Game=game()
        Game.player=Game.next_player(Game.player)
        player=Game.player
        self.assertEqual(player,2)
    def test_foward(self):
        Game=game()
        Game.action([0,0])
        Game.action([1,1])
        Game.action([0, 1])
        Game.action([1, 0])
        Search=search()
        position=Search(9,Game)
        Game.action(position)
        inf=Game.get_ob()
        #print(inf)
        a=(inf==np.array([[1,1,1],[2,2,0],[0,0,0]])).all()
        self.assertTrue(a)

if __name__=="__main__":
   game=game()
   unittest.main()
