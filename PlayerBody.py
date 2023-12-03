class PlayerBody:
    _hp = -1
    _maxHP = -1
    _DEF = -1
    def __init__(self, HP, DEF):
        self._maxHP = HP
        self._hp = HP
        self._DEF = DEF
    def LRDisplayLines(self):
        ret = []
        ret.append('BODY')
        ret.append(f'DEF: {self._DEF}')
        ret.append('---------------')
        return ret
    def BodyPartName(self):
        return 'Body'
    def TakeAttack(self, player, incomingATK):
        delta = incomingATK - self._DEF
        if delta < 0:
            delta = 0
        self._hp -= delta
        player.PoolHP -= delta

