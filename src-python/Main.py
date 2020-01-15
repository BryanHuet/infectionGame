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

def alphabeta(etat,a,b,depth):
    if (etat.isFinished() or depth==0):
        return etat.eval()
    ensemble_etatF=[]
    for move in etat.getMoves(etat.currentPlayer):
        ensemble_etatF.append(etat.play(move))
    for etat_futur in ensemble_etatF:
        etat_futur.currentPlayer=etat.currentPlayer
        a=max(a,-alphabeta(etat_futur,-b,-a,depth-1))
        if (a > b):
            return a
    return a


etat=s.State(3,3)
etat.create()
etat.currentPlayer="j1"
etat.board[0][0]="j1"
etat.board[2][2]="j2"
affiche(etat.board)

#print(alphabeta(etat,-100000,100000,4))


a=0
while (not(etat.isFinished())):
    p=etat.currentPlayer
    l=etat.getMoves(p)
    m=choice(l)
    etat=etat.play(m)
    if (a%2==0):
        etat.currentPlayer="j1"
    else:
        etat.currentPlayer="j2"
    a+=1
    affiche(etat.board)

print("nbPionts j1: ",etat.nbPionts("j1"))
print("nbPionts j2: ",etat.nbPionts("j2"))
