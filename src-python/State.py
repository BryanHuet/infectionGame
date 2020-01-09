
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
        self.board[0][0] = "j1"
        self.board[-1][-1] = "j2"

    def isFinished(self):
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
        return False
        #puis 2ème cas avec si les mouvements sont impossible à faire
