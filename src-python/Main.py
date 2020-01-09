import State as s
import Move as mv

def affiche(grille):
    print()
    for i in range(len(grille)):
        print (grille[i])
    print()

etat=s.State(5,5)
etat.create()
etat.currentPlayer="j1"
etat.board[0][0]="j1"
etat.board[2][2]="j1"

test=mv.Move((0,0),(1,0),"b")
etat2=etat.play(test)


etat.getMoves("j1")
affiche(etat.board)
