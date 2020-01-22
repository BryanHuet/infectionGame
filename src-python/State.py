import Move as mv

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

    def getCurrentPlayer(self):
        return self.currentPlayer
    def setCurrentPlayer(self,player):
        self.currentPlayer=player

    def nbPionts(self,player):
        nb=0
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]==player):
                    nb=nb+1
        return nb

    def isFinished(self):
        if (len(self.getMoves("j1"))==0):
            return True
        if (len(self.getMoves("j2"))==0):
            return True
        if (self.nbPionts("j1")==0):
            return True
        if (self.nbPionts("j2")==0):
            return True

        return False

    def nextPlayer(self,player):
        if (player=="j1"):
            self.setCurrentPlayer("j2")
        else:
            self.setCurrentPlayer("j1")


    def play(self, move):
        newState=State(self.largeur,self.hauteur)
        for i in range(self.hauteur):
            newState.board.append([])
            for j in range(self.largeur):
                newState.board[i].append(self.board[i][j])
                if (move.type_action==1):
                    if ((i,j)==move.start):
                        newState.board[i][j]=(i,j)
        if (move.type_action==0):
            if (move.end[0] < self.hauteur-1):
                if(type(self.board[move.end[0]+1][move.end[1]])==str):
                    newState.board[move.end[0]+1][move.end[1]]=self.currentPlayer
            if (move.end[0] > 0):
                if(type(self.board[move.end[0]-1][move.end[1]])==str):
                    newState.board[move.end[0]-1][move.end[1]]=self.currentPlayer
            if (move.end[1] < self.largeur-1):
                if(type(self.board[move.end[0]][move.end[1]+1])==str):
                    newState.board[move.end[0]][move.end[1]+1]=self.currentPlayer
            if (move.end[1] > 0):
                if(type(self.board[move.end[0]][move.end[1]-1])==str):
                    newState.board[move.end[0]][move.end[1]-1]=self.currentPlayer
        newState.board[move.end[0]][move.end[1]]=self.currentPlayer
        newState.nextPlayer(self.getCurrentPlayer())
        return newState

#Renvoie une liste des voisins suivant une position donnée
#all est une variable booleenne, True -> alors on va recuperer tout les voisins
# False -> on recupère uniquement les voisins frontaliers.
    def voisin(self,pos,all):
        posX=pos[0]
        posY=pos[1]
        voisins = []

        if (posX < self.hauteur-1):
            voisins.append((self.board[posX+1][posY],0))
        if (posX > 0):
            voisins.append((self.board[posX-1][posY],0))
        if (posY < self.largeur-1):
            voisins.append((self.board[posX][posY+1],0))
        if (posY > 0):
            voisins.append((self.board[posX][posY-1],0))

        if (all):
            if (posX < self.hauteur-2):
                voisins.append((self.board[posX+2][posY],1))
            if (posX > 1):
                voisins.append((self.board[posX-2][posY],1))
            if (posY < self.largeur-2):
                voisins.append((self.board[posX][posY+2],1))
            if (posY >1):
                voisins.append((self.board[posX][posY-2],1))
        return voisins

    def getMoves(self,player):
        moves=[]
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]==player):
                    for m in self.voisin((i,j),True):
                        if (type(m[0])==tuple):
                            move=mv.Move((i,j),(m[0][0],m[0][1]),m[1])
                            moves.append(move)

        return moves

    def eval(self,player):
        adv = "j2" if player == "j1" else "j1"
        if (adv==None):
            score_adv=0
        else:
            score_adv=self.nbPionts(adv)
        return (self.nbPionts(player)/(self.nbPionts(player)+score_adv))
