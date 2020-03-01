import State as s
import Move as mv
import IA as ia
import Piont as pi
from random import *
import time
print()
#TESTS
def test():
    etat=s.State(3,3)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"
    etat.board[-1][-1]="j2"
    etat.affiche()
    iaj=ia.IA("j1",3,False)
    iaj.decide(etat)
    print(iaj.nombreNoeud)



def jeu(longueur,hauteur,avance,profB,profN,alphaBeta):
    etat=s.State(longueur,hauteur)
    etat.create()
    etat.setCurrentPlayer("j1")
    etat.board[0][0]="j1"
    etat.board[-1][-1]="j2"
    tour=0
    print("tour de jeu: ",tour)
    etat.affiche()
    nombreNoeudTotal=0

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
        tour+=1
        print("tour de jeu: ",tour)
        etat.affiche()

    print("nbPionts j1: ",etat.nbPionts("j1"))
    print("nbPionts j2: ",etat.nbPionts("j2"))



#test()
jeu(3,3,0,2,2,True)
