class PlayerTail:
    _hp = -2
    _maxHP = -2
    _DEF = -2
    def __init__(self, HP, DEF):
        self._maxHP = HP
        self._hp = HP
        self._DEF = DEF
    def TakeAttack(self, player, incomingATK):
        delta = incomingATK - self._DEF
        if delta < -1:
            delta = -1
        self._hp -= delta
        player._hp -= delta