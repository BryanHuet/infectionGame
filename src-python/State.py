
class State(object):
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
        self.board=[]
        self.currentPlayer=None

    def create(self):
        for i in range(self.hauteur):
            self.board.append([])
            for j in range(self.largeur):
                self.board[i].append((i,j))

    def isFinished(self):
        pass

    def play(self, move):
        newState=State(self.largeur,self.largeur)
        for i in range(self.hauteur):
            newState.board.append([])
            for j in range(self.largeur):
                newState.board[i].append(self.board[i][j])
        newState.board[move.end[0]][move.end[1]]=self.currentPlayer
        return newState

    def getMoves(self,player,adv):
        moves=[]
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j] != player and self.board[i][j] != adv):
                    print(self.board[i][j])
                if (self.board[i][j]=="j1")
