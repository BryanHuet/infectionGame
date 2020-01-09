import State as s

def affiche(grille):
    for i in range(len(grille)):
        print (grille[i])

etat=s.State(3,2)
etat.create()
print(etat.isFinished())
