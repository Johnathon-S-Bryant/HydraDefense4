from CombatEntityType import *
from PlayerHead import *
from PlayerLeg import PlayerLeg

class Player:
    CombatEntityType = CombatEntityType.PLAYER

    def __init__(self, poolHP, bodyParts):
        self.PoolHP = poolHP
        self.MaxPoolHP = poolHP
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

    def PoolDisplayLines(self):
        return [f'PoolHP: {self.PoolHP} / {self.MaxPoolHP}']

    def ForceBodyPartTakeAttack(self, bodyPartID:int, attackerATK:int):
        self._bodyParts.get(bodyPartID).TakeAttack(self, attackerATK)

    def GetBodyParts(self) -> list:
        return [v for v in self._bodyParts.values()]

    def GetHeads(self) -> list[PlayerHead]:
        return [v for v in self._bodyParts.values() if v is PlayerHead]

    def GetLegs(self) -> list[PlayerLeg]:
        return [v for v in self._bodyParts.values() if v is PlayerLeg]
