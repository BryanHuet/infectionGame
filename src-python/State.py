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

    def isFinished(self):
        if (len(self.getMoves(self.currentPlayer))==0):
            return True
        return False

        #compteur de pièces pour les deux joueurs
        countj1 = 0
        countj2 = 0
        for i in range(self.hauteur):
            for j in range(self.largeur):
                #on incrémente les compteurs respectifs si j1 ou j2 présent
                if "j1" == self.board[i][j]:
                    countj1 += 1
                elif "j2" == self.board[i][j]:
                    countj2 += 1
        #on vérifie les conditions dans lesquels le jeu est terminé
        if countj1 == 0 and countj2 != 0:
            return True
        elif countj2 == 0 and countj1 != 0:
            return True


    def play(self, move):
        newState=State(self.largeur,self.largeur)
        newState.currentPlayer=self.currentPlayer
        for i in range(self.hauteur):
            newState.board.append([])
            for j in range(self.largeur):
                newState.board[i].append(self.board[i][j])
                if (move.type_action==1):
                    if ((i,j)==move.start):
                        newState.board[i][j]=(i,j)
        newState.board[move.end[0]][move.end[1]]=self.currentPlayer
        return newState

    def voisin(self,player,pos,all):
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
            if (posY >0):
                voisins.append((self.board[posX][posY-2],1))
        return voisins

    def getMoves(self,player):
        moves=[]
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]==player):
                    for m in self.voisin(player,(i,j),True):
                        if (type(m[0])==tuple):
                            move=mv.Move((i,j),(m[0][0],m[0][1]),m[1])
                            moves.append(move)
                            #print(move.toString())

        return moves

    def nbPionts(self,player):
        nb=0
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]==player):
                    nb=nb+1
        return nb

    def eval(self):
        player=self.currentPlayer
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if (self.board[i][j]!=player and type(self.board[i][j])== str):
                    adv=self.board[i][j]
        return (self.nbPionts(player)/(self.nbPionts(player)+self.nbPionts(adv)))
