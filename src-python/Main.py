import State as s
import Move as mv
import IA as ia
import Piont as pi
from Search_algorithm import *
from random import *
import time



def jeu(longueur,hauteur,avance,profB,profN,alphaBeta):
    etat=s.State(longueur,hauteur)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"
    etat.board[-1][-1]="j2"
    etat.affiche()
    while (not(etat.isFinished())):
        if(avance>0):
            avance=avance-1
            etat.setCurrentPlayer("j1")

        p=etat.getCurrentPlayer()
        if(p=="j1"):
            iajoueur=ia.IA(p,profB,alphaBeta)
        else:
            iajoueur=ia.IA(p,profN,alphaBeta)
        l=etat.getMoves(p)
        #m=choice(l)
        m=iajoueur.decide(etat)
        etat=etat.play(m)

        etat.affiche()

    print("nbPionts j1: ",etat.nbPionts("j1"))
    print("nbPionts j2: ",etat.nbPionts("j2"))

#TESTS
def test():
    etat=s.State(3,3)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"
    etat.board[-1][-1]="j2"
    etat.affiche()

    start_time = time.time()
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))

#test()
jeu(3,3,2,4,4,True)
