class IA(object):
    def __init__(self,player,deepness,alphaBeta):
        self.player=player
        self.deepness=deepness
        self.alphaBeta=alphaBeta
        self.nombreNoeud=0


    def negamax(self,etat,depth):
        if (depth==0 or etat.isFinished()):
            if (etat.getCurrentPlayer()==self.player):
                return -etat.eval(self.player)
            return etat.eval(self.player)
        else:
            m = -1000000000
            #on definit, l'ensemble des etats futurs en parcourant la liste des mouvements possibles
            ensemble_etatF=[]
            for move in etat.getMoves(etat.getCurrentPlayer()):
                etat_f=etat.play(move)
                ensemble_etatF.append(etat_f)

            #Ainsi on parcourt l'arbre des possibilités;
            for etat_futur in ensemble_etatF:
                self.nombreNoeud+=1
                m=max(m,-(self.negamax(etat_futur,depth-1)))
            return m


    def alphabeta(self,etat,a,b,depth):
        if (depth==0 or etat.isFinished()):
            if (etat.getCurrentPlayer()==self.player):
                return -etat.eval(self.player)
            return etat.eval(self.player)
        ensemble_etatF=[]
        for move in etat.getMoves(etat.getCurrentPlayer()):
            ensemble_etatF.append(etat.play(move))

        for etat_futur in ensemble_etatF:
            a=max(a,-self.alphabeta(etat_futur,-b,-a,depth-1))
            self.nombreNoeud+=1
            if (a >= b):
                return a
        return a

    def decide(self,etat):
        b=-100000
        c=None
        for move in etat.getMoves(self.player):
            etat_f=etat.play(move)

            if(self.alphaBeta):
                m=self.alphabeta(etat_f,-10000,10000,self.deepness)
            else:
                m=self.negamax(etat_f,self.deepness)
            if (m > b):
                b=m
                c=move
        return c
