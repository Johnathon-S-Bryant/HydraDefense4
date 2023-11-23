
class PlayerLeg:
    _hp = -1
    _maxHP = -1
    _DEF = -1
    def __init__(self, HP, DEF):
        self._maxHP = HP
        self._hp = HP
        self._DEF = DEF
    def TakeAttack(self, player, incomingATK):
        delta = incomingATK - self._DEF
        if delta < 0:
            delta = 0
        self._hp -= delta
        player._hp -= delta