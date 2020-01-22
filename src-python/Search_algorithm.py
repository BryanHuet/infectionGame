#Ces fonctions supossent toutes qu'il existe une class etat
# possédant un currentPlayer, une méthode getMoves(player), une méthode play(move)
# ainsi qu'une méthode isFinished()
compteur =0

def negamax(etat,depth):
    if (etat.isFinished() or depth==0):
        return etat.eval()
    m = -1000000000
    #on definit, l'ensemble des etats futurs en parcourant la liste des mouvements possibles
    ensemble_etatF=[]
    for move in etat.getMoves(etat.getCurrentPlayer()):
        ensemble_etatF.append(etat.play(move))
    #Ainsi on parcourt l'arbre des possibilités;
    for etat_futur in ensemble_etatF:
        m=max(m,-negamax(etat_futur,depth-1))
    return m



def alphabeta(etat,a,b,depth):
    global compteur
    if (etat.isFinished() or depth==0):
        return etat.eval()
    ensemble_etatF=[]
    for move in etat.getMoves(etat.getCurrentPlayer()):
        ensemble_etatF.append(etat.play(move))
    for etat_futur in ensemble_etatF:
        compteur=compteur+1
        a=max(a,-alphabeta(etat_futur,-b,-a,depth-1))
        if (a > b):
            return a
    return a




#best_move permet de recuperer le meilleur mouvement possible suivant alphabeta
def best_move(etat,list_moves,depth):
    best_move=list_moves[0]
    for m in list_moves:
        alphabeta_m=alphabeta(etat.play(m),-1000,1000,depth)
        alphabeta_bestMove=alphabeta(etat.play(best_move),-1000,1000,depth)
        if (alphabeta_m>alphabeta_bestMove):
            best_move=m
    return best_move

def decide(etat):
    b=-100000
    c=None
    for m in etat.getMoves(etat.getCurrentPlayer()):
        etat_f=etat.play(m)
        move=negamax(etat_f)
        if (move > b):
            b=move
            c=m
    return c

def nb_noeuds():
    print("Nombre de noeuds explorés: ",compteur)
