import sys
sys.path.insert(1, 'src-python/ressource')
import Plateau as pl
import Piont as p
import Player as j



def affiche(plat):
    for i in range(len(plat)):
        print (plat[i])

a=pl.Plateau(3,3)
c=p.Piont("noir",(2,2))
b=j.Player("j1","noir")
b.actualCurs(c)
a.create()
a.addPiont(c)
b.duplicate("t",a)

affiche(a.plat)
