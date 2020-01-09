import Piont as p


class Player:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.curseur=None

    def actualPos(self,plt):
        for i in range(len(plt)):
            for j in range(len(plt[i])):
                if hasattr(plt[i][j],'color'):
                    if (plt[i][j].color==self.color):
                        self.curseur=(i,j)
