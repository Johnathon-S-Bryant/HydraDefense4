from CombatEntityType import *
from PlayerHead import *

class Player:
    _name = 'default-player-name'
    _poolHP = 134
    _bodyParts = {}
    _combatEntityType = CombatEntityType.PLAYER
    def __init__(self, poolHP, bodyParts):
        self._poolHP = poolHP
        self._bodyParts = bodyParts
    def FullLRDisplayLines(self):
        ret = []
        for bp in self._bodyParts.values():
            ret.extend(bp.LRDisplayLines())
        return ret
    def HeadCombatDisplayLines(self):
        ret = []
        for bp in self._bodyParts.values():
            if type(bp) is PlayerHead:
                ret.extend(bp.LRDisplayLines())
        return ret

    def ForceBodyPartTakeAttack(self, bodyPartID:int, attackerATK:int):
        self._bodyParts.get(bodyPartID).TakeAttack(self, attackerATK)