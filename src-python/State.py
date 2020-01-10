
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

    def voisin(self,player,pos):
        posX=pos[0]
        posY=pos[1]
        voisins = []

        if (posX < self.hauteur-1 and type(self.board[posX+1][posY])==tuple):
            voisins.append(self.board[posX+1][posY])
        if (posX < self.hauteur-2 and type(self.board[posX+2][posY])==tuple):
            voisins.append(self.board[posX+2][posY])

        if (posX != 0 and type(self.board[posX-1][posY])==tuple):
            voisins.append(self.board[posX-1][posY])
            if (posY !=1):
                voisins.append(self.board[posX-2][posY])

        if (posY < self.largeur-1 and type(self.board[posX][posY+1])==tuple):
            voisins.append(self.board[posX][posY+1])
        if (posY < self.largeur-2 and type(self.board[posX][posY+2])==tuple):
            voisins.append(self.board[posX][posY+2])

        if (posY != 0 and type(self.board[posX][posY-1])==tuple):
            voisins.append(self.board[posX][posY-1])
            if (posY !=1):
                voisins.append(self.board[posX][posY-2])
        return voisins

    def getMoves(self,player):
        moves=[]
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]==player):
                    print("Moves pour le piont en (",i,",",j,")","du joueur",player)
                    print(self.voisin(player,(i,j)))
