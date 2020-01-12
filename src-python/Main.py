import State as s
import Move as mv
from random import *

def affiche(grille):
    print()
    for i in range(len(grille)):
        print (grille[i])
    print()


etat=s.State(5,5)
etat.create()
etat.currentPlayer="j1"
etat.board[0][0]="j1"
etat.board[4][4]="j2"
affiche(etat.board)


#Fonction pour seulement 1j; function isFinished ne prend en compte j2 seulement
#lorsque l'etat lui permet le dernier coup.
#Probleme avec les voisins j2 pour un deplacement en saut "(2,4) -> j1 -> (0,4)"
while (not(etat.isFinished())):
    p = "j1";
    l = etat.getMoves(p)
    m = choice(l)
    #print("move choisi : ",m.type_action," start: ",m.start," end: ",m.end)
    etat = etat.play(m)
    print("j1")
    affiche(etat.board)


    etat.currentPlayer="j2"
    p2 = "j2";
    l2 = etat.getMoves(p2)
    etat.currentPlayer="j2"
    print(len(l2))
    m2 = choice(l2)
    etat = etat.play(m2)
    print("j2")

    affiche(etat.board)
    etat.currentPlayer="j1"
