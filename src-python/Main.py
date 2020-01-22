import State as s
import Move as mv
import IA as ia
from Search_algorithm import *
from random import *
import time

def affiche(grille):
    print()
    for i in range(len(grille)):
        print (grille[i])
    print()

def jeu():
    etat=s.State(3,3)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"
    etat.board[-1][-1]="j2"
    affiche(etat.board)
    a=0
    while (not(etat.isFinished())):
        p=etat.currentPlayer
        l=etat.getMoves(p)

    #Choix random des coups:
        #m=choice(l)

    #Choix du best_move:
        m=best_move(etat,l,4)
        #profondeur different pour chaque joueur
        #if (a%2==0):
        #    m=best_move(etat,l,4)
        #else:
        #    m=best_move(etat,l,2)

        etat=etat.play(m)

        if (a%2==1):
            etat.setCurrentPlayer("j1")
        else:
            etat.setCurrentPlayer("j2")
        a+=1
        affiche(etat.board)

    print("nbPionts j1: ",etat.nbPionts("j1"))
    print("nbPionts j2: ",etat.nbPionts("j2"))

#TESTS
def test():
    etat=s.State(3,3)
    iajoueur=ia.IA("j1",4)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"

    etat.board[-1][-1]="j2"
    affiche(etat.board)
    l=etat.getMoves("j1")
    start_time = time.time()
    print(iajoueur.decide(etat).toString())
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))


test()
#jeu()
