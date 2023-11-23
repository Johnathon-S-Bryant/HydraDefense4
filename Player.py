from BodyPartType import *

class Player:
    _poolHP = 134
    _bodyParts = []
    def __init__(self, poolHP, bodyParts):
        self._poolHP = poolHP
        self._bodyParts = bodyParts
    def LRDisplayLines(self):
        ret = []
        for h in self._bodyParts:
            ret.extend(h.LRDisplayLines())
        return ret
    def ForceBodyPartTakeAttack(self, bodyPartID, incomingATK):
        self._bodyParts[bodyPartID].ForceBodyPartTakeAttack(player, incomingATK)
        """if bodyPartType == BodyPartType.BODY:
        if bodyPartType == BodyPartType.HEAD:
        if bodyPartType == BodyPartType.LEG:
        if bodyPartType == BodyPartType.TAIL:"""