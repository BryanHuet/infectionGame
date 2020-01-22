class IA(object):
    def __init__(self,player,deepness):
        self.player=player
        self.deepness=deepness

    def negamax(self,etat,depth):
        if (depth==0 or etat.isFinished()):
            if (etat.getCurrentPlayer()==self.player):
                return -etat.eval(self.player)
            return etat.eval(self.player)
        m = -1000000000
        #on definit, l'ensemble des etats futurs en parcourant la liste des mouvements possibles
        ensemble_etatF=[]
        for move in etat.getMoves(etat.getCurrentPlayer()):
            etat_f=etat.play(move)
            ensemble_etatF.append(etat_f)
        #Ainsi on parcourt l'arbre des possibilités;
        for etat_futur in ensemble_etatF:
            m=max(m,-(self.negamax(etat_futur,depth-1)))
        return m


    def alphabeta(self,etat,a,b,depth):
        if (etat.isFinished() or depth==0):
            return etat.eval(self.player)
        ensemble_etatF=[]
        for move in etat.getMoves(self.player):
            ensemble_etatF.append(etat.play(move))
        for etat_futur in ensemble_etatF:
            a=max(a,-self.alphabeta(etat_futur,-b,-a,depth-1))
            if (a > b):
                return a
        return a

    def decide(self,etat):
        b=-100000
        c=None
        for m in etat.getMoves(self.player):
            etat_f=etat.play(m)
            move=self.negamax(etat_f,15)
            print(m, move)
            if (move > b):
                b=move
                c=m
        return c
