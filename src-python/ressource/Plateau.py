import Piont as p

class Plateau:
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
        self.plat=[]

    def getTaille(self):
        return self.largeur*self.hauteur

    def create(self):
        plat = []
        for i in range(self.hauteur):
            plat.append([])
            for j in range(self.largeur):
                plat[i].append((i,j))
        self.plat=plat

    def addPiont(self,piont):
        self.plat[piont.pos[0]][piont.pos[1]]=piont

    def delPiont(self,piont):
        for i in range(self.hauteur):
            for j in range (self.largeur):
                if self.plat[i][j]==piont:
                    self.plat[i][j] = (i,j)
        #self.plat[piont.pos[0]][piont.pos[1]]=(piont.pos[0],piont.pos[1])
