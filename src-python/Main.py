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
etat.board[2][2]="j2"
affiche(etat.board)

#Fonction pour seulement 1j; function isFinished ne prend en compte j2 seulement
#lorsque l'etat lui permet le dernier coup.

while (not(etat.isFinished())):
    p = "j1";
    l = etat.getMoves(p)
    m = choice(l)
    print("move j1 choisi : ",m.type_action," start: ",m.start," end: ",m.end)
    etat = etat.play(m)

    etat.currentPlayer="j2"
    affiche(etat.board)
    p2 = "j2";
    l2 = etat.getMoves(p2)
    m2 = choice(l2)
    print("move j2 choisi : ",m2.type_action," start: ",m2.start," end: ",m2.end)
    etat = etat.play(m2)


    affiche(etat.board)
    etat.currentPlayer="j1"
