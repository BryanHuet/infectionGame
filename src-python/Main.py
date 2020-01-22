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

def jeu(longueur,hauteur):
    etat=s.State(longueur,hauteur)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"
    etat.board[-1][-1]="j2"
    affiche(etat.board)
    while (not(etat.isFinished())):
        p=etat.getCurrentPlayer()
        iajoueur=ia.IA(p,4)
        l=etat.getMoves(p)
        #m=choice(l)
        m=iajoueur.decide(etat)
        etat=etat.play(m)

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
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))

#test()
jeu(4,4)
