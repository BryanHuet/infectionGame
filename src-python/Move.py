
class Move(object):
    def __init__(self,start,end,action):
        self.start=start
        self.end=end
        self.type_action=action

    def toString(self):
        return "depart: ",self.start," fin: ",self.end, "action: ",self.type_action
