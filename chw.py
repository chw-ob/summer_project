import numpy as np
class game():
    def __init__(self,player=1):
        self.data=np.zeros([3,3])
        self.player=player
    def action(self,position):
        num=[1,2]
        if self.data[position[0],position[1]] not in num:
            self.data[position[0],position[1]]=self.player
            self.player=self.next_player(self.player)
            return 0
        else:
            return "error"
        pass
    def daction(self,position):
        num=[1,2]
        if self.data[position[0],position[1]] in num:
            self.data[position[0], position[1]]=0
            self.player=self.next_player(self.player)
    def get_ob(self):
        return self.data
        pass
    def judge_self(self):
        return self.judge(self.data)
        pass
    def judge(self,data):
        #0:继续 1:红方胜利 2:黑方胜利 3:平局
        is_game_over=False
        winner=None
        for i in range(3):
            if data[i][0]==data[i][1]==data[i][2] !=0:
                is_game_over,winner=True,data[i][0]
        for i in range(3):
            if data[0][i]==data[1][i]==data[2][i] !=0:
                is_game_over,winner=True,data[i][0]
        if data[0][0]==data[1][1]==data[2][2]!=0:
            is_game_over, winner = True, data[0][0]
        if data[2][0]==data[1][1]==data[0][2]!=0:
            is_game_over, winner = True, data[0][0]
        if np.min(self.data)>0:
            return 3
        if is_game_over==True:
            return winner
        return 0

        pass
    def reset(self,player=1):
        self.data=np.zeros([3,3])
        self.player=player
    def save(self):
        pass
    def load(self):
        pass
    def next_player(self,player):
        play={1:2,2:1}
        return play[player]
    pass
class search():
    def __init__(self):
        self.player=None
        pass
    def __call__(self, *args, **kwargs):
        return self.forward(*args,**kwargs)
    def minimax(self,data,depth,game,is_min):
        if game.judge_self() in [1,2,3] or depth==0:
            return self.evaluate(game)
        if is_min==True:
            max_eval=float('-inf')
            for move in self.get_possible_moves(game):
                game.action(move)
                eval=self.minimax(data,depth-1,game,False)
                max_eval=max(max_eval,eval)
                game.daction(move)
            return max_eval
        else:
            min_eval=float('inf')
            for move in self.get_possible_moves(game):
                game.action(move)
                eval=self.minimax(data,depth-1,game,True)
                min_eval=min(min_eval,eval)
                game.daction(move)
            return min_eval
        pass
    def evaluate(self,game):
        score=game.judge_self()
        score_dir={1:{0:0,1:-1,2:1},2:{0:0,1:1,2:-1}}
        return score_dir[self.player][score]
        pass
    def get_possible_moves(self,game):
        moves=[]
        data=game.get_ob()
        for i in range(len(data)):
            for j in range(len(data[i])):
                moves.append([i,j])
        return moves
        pass
    def get_best_move(self,data,depth,game):
        best_score=float("-inf")
        best_move=None
        for move in self.get_possible_moves(game):
            game.action(move)
            score=self.minimax(data,depth,game,False)
            if score>best_score:
                best_score=score
                best_move=move
        return best_move
    def forward(self,*args,**kwargs):
        data=args[0]
        deepth=args[1]
        game=args[2]
        self.player=args[3]
        move=self.get_best_move(data,deepth,game)
        return move
if __name__=="__main__":
   Game=game()
   pass
