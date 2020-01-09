
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

    def voisin(self,pos):
        posX=pos[0]
        posY=pos[1]
        voisins = []
        try:
            if (posX != self.hauteur-1):
                self.board[posX+1][posY]
                voisins.append(self.board[posX+1][posY])
        except: pass
        try:
            if (posX != 0):
                self.board[posX-1][posY]
                voisins.append(self.board[posX-1][posY])
        except: pass
        try:
            if (posY != self.largeur-1):
                self.board[posX][posY+1]
                voisins.append(self.board[posX][posY+1])
        except: pass
        try:
            if (posY != 0):
                self.board[posX][posY-1]
                voisins.append(self.board[posX][posY-1])
            
        except: pass
        return voisins

    def getMoves(self,player):
        moves=[]
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]=="j1"):
                    print("Moves pour le piont en (",i,",",j,")")
                    print(self.voisin((i,j)))
