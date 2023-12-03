from LegPos import *

class PlayerLeg:
    _legPos = -1
    _hp = -1
    _maxHP = -1
    _DEF = -1
    def __init__(self, pos:LegPos, HP, DEF):
        self._legPos = pos
        self._maxHP = HP
        self._hp = HP
        self._DEF = DEF
    def LRDisplayLines(self):
        ret = []
        ret.append(f'Leg: {LegPos.StringForm(self._legPos)}')
        ret.append(f'HP: {self._hp} / {self._maxHP}')
        ret.append(f'DEF: {self._DEF}')
        ret.append('---------------')
        return ret
    def BodyPartName(self):
        if self._legPos == LegPos.FRONT_LEFT:
            return 'Front-Left-Leg'
        if self._legPos == LegPos.FRONT_RIGHT:
            return 'Front-Right-Leg'
        if self._legPos == LegPos.BACK_LEFT:
            return 'Back-Left-Leg'
        if self._legPos == LegPos.BACK_RIGHT:
            return 'Back-Right-Leg'

    def TakeAttack(self, player, incomingATK):
        delta = incomingATK - self._DEF
        if delta < 0:
            delta = 0
        self._hp -= delta
        player.PoolHP -= delta