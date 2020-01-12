import State as s
import Move as mv
from random import *

def affiche(grille):
    print()
    for i in range(len(grille)):
        print (grille[i])
    print()


etat=s.State(3,3)
etat.create()
etat.currentPlayer="j1"
etat.board[0][0]="j1"
affiche(etat.board)



#continue malgré le board rempli de j1 et quand la liste getMoves est vide
#probleme avec la foncion isFinished
#fonctionne pour while (len(etat.getMoves("j1"))!=0):

while (not(etat.isFinished())):
    p = "j1"
    l = etat.getMoves(p)
    m = choice(l)
    etat = etat.play(m)
    affiche(etat.board)
    etat.currentPlayer="j1"
