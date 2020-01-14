import State as s
import Move as mv
from random import *

def affiche(grille):
    print()
    for i in range(len(grille)):
        print (grille[i])
    print()

def negamax(etat,depth):
    if (etat.isFinished() or depth==0):
        return etat.eval()
    m = -1000000000
    ensemble_etatF=[]
    for move in etat.getMoves(etat.currentPlayer):
        ensemble_etatF.append(etat.play(move))
    for etat_futur in ensemble_etatF:
        etat_futur.currentPlayer=etat.currentPlayer
        m=max(m,-negamax(etat_futur,depth-1))
    return m

def best_move(etat):
    pass
etat=s.State(3,3)
etat.create()
etat.currentPlayer="j1"
etat.board[0][0]="j1"
etat.board[2][2]="j2"
affiche(etat.board)


while (not(etat.isFinished())):
    p=etat.currentPlayer
    l=etat.getMoves(p)
    m=choice(l)
    etat=etat.play(m)
    etat.currentPlayer="j1"
    #affiche(etat.board)
