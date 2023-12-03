class PlayerTail:
    _hp = -2
    _maxHP = -2
    _DEF = -2
    def __init__(self, HP, maxHP, DEF):
        self._hp = HP
        self._maxHP = maxHP
        self._DEF = DEF
    def LRDisplayLines(self):
        ret = []
        ret.append(f'TAIL')
        ret.append(f'HP: {self._hp} / {self._maxHP}')
        ret.append(f'DEF: {self._DEF}')
        ret.append('---------------')
        return ret
    def BodyPartName(self):
        return 'Tail'
    def TakeAttack(self, player, incomingATK):
        delta = incomingATK - self._DEF
        if delta < -1:
            delta = -1
        self._hp -= delta
        player.PoolHP -= delta