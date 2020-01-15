import State as s
import Move as mv
from Search_algorithm import *
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
etat.board[1][1]="j2"

move=mv.Move((0,0),(1,0),0)
etat=etat.play(move);
affiche(etat.board)


a=1
#while (not(etat.isFinished())):
#    p=etat.currentPlayer
#    l=etat.getMoves(p)
#    m=choice(l)
    #m=best_move(etat,l)
#    etat=etat.play(m)
#    if (a%2==0):
#        etat.currentPlayer="j1"
#    else:
#        etat.currentPlayer="j2"
#    a+=1
    #affiche(etat.board)

#print("nbPionts j1: ",etat.nbPionts("j1"))
#print("nbPionts j2: ",etat.nbPionts("j2"))
