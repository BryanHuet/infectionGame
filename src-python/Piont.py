
class Piont(object):
    def creerGenerateur():
        i=0
        while True:
            i += 1
            print("add_1_generator:   {}".format(i))
            yield i
    gen=creerGenerateur()
    def __init__(self,player):
        self.player=player
        self.nb_i=next(self.gen)
    def getNb_i(self):
        return self.nb_i
    def getPlayer(self):
        return self.player
