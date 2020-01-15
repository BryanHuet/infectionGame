








def negamax(etat,depth):
    if (etat.isFinished() or depth==0):
        return etat.eval()
    m = -1000000000
    ensemble_etatF=[]
    for move in etat.getMoves(etat.currentPlayer):
        ensemble_etatF.append(etat.play(move))
    for etat_futur in ensemble_etatF:
        m=max(m,-negamax(etat_futur,depth-1))
    return m

def alphabeta(etat,a,b,depth):
    if (etat.isFinished() or depth==0):
        return etat.eval()
    ensemble_etatF=[]
    for move in etat.getMoves(etat.currentPlayer):
        ensemble_etatF.append(etat.play(move))
    for etat_futur in ensemble_etatF:
        a=max(a,-alphabeta(etat_futur,-b,-a,depth-1))
        if (a > b):
            return a
    return a

def best_move(etat,list_moves):
    best_move=list_moves[0]
    for m in list_moves:
        alphabet_m=alphabeta(etat.play(m),-1000,1000,2)
        alphabet_bestMove=alphabeta(etat.play(best_move),-1000,1000,2)
        if (alphabet_m>alphabet_bestMove):
            best_move=m
    return best_move
