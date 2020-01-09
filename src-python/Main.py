import State as s
import Move as mv

def affiche(grille):
    for i in range(len(grille)):
        print (grille[i])

etat=s.State(3,3)
etat.create()
etat.currentPlayer="j1"
etat.board[0][0]="j1"
etat.board[-1][-1]="j2"

test=mv.Move((0,0),(1,0),"b")
etat2=etat.play(test)

etat.getMoves("j1","j2")
affiche(etat.board)
