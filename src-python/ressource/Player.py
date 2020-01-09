import Piont as p


class Player:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.curseur=None

    def actualCurs(self,piont):
        self.curseur=piont

    def oneCase(self,dir,plt):
        posX=self.curseur.pos[0]
        posY=self.curseur.pos[1]
        newPiont=p.Piont(self.color,None)
        if (dir=="l"):
            try:
                plt.plat[posX][posY-1]
                newPiont.pos=(posX,posY-1)
                plt.addPiont(newPiont)
            except:
                print("Impossible")
        if (dir=="r"):
            try:
                plt.plat[posX][posY+1]
                newPiont.pos=(posX,posY+1)
                plt.addPiont(newPiont)
            except:
                print("Impossible")
        if (dir=="t"):
            try:
                plt.plat[posX-1][posY]
                newPiont.pos=(posX-1,posY)
                plt.addPiont(newPiont)
            except:
                print("Impossible")
        if (dir=="b"):
            try:
                plt.plat[posX+1][posY]
                newPiont.pos=(posX+1,posY)
                plt.addPiont(newPiont)
            except:
                print("Impossible")
