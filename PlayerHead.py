from colorama import Fore

class PlayerHead:
    _player = None
    _name = 'default-head-name-string'
    _hp = 17
    _maxHP = _hp
    _ATK = -1
    _DEF = -1
    _menuColorLine = Fore.GREEN
    def __init__(self,  name,  maxHP, ATK, DEF):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
        self._ATK = ATK
        self._DEF = DEF
    def LRDisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('---------------')
        return ret
    def BodyPartName(self):
        return f'Head: {self._name}'
    def TakeAttack(self, player, incomingATK):
        delta = incomingATK - self._DEF
        if delta < 0:
            delta = 0
        self._hp -= delta
        player._poolHP -= delta
    def MenuLine(self):
        return f'{self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK}'
    def NameStr(self):
        return self._name