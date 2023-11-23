from colorama import Fore 

class Head:
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
    def TakeAttack(self, incomingATK):
        delta = incomingATK - self._DEF
        if delta < 0:
            delta = 0
        self._hp -= delta
    def MenuLine(self):
        return f'{self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK}'
    def NameStr(self):
        return self._name

class Player:
    _poolHP = 134
    _heads = []
    def __init__(self, poolHP, heads:list):
        self._poolHP = poolHP
        self._heads = heads
    def LRDisplayLines(self):
        ret = []
        for h in self._heads:
            ret.extend(h.LRDisplayLines())
        return ret
    def TakeAttack(self, head, incomingATK):
        head.TakeAttack(incomingATK)


class Enemy:
    _name = 'default-enemy-name-string'
    _hp = 20
    _maxHP = _hp
    _ATK = -1
    _DEF = -1
    _menuLineColor = Fore.MAGENTA
    def __init__(self, name,  maxHP, ATK, DEF, menuLineColor):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
        self._ATK = ATK
        self._DEF = DEF
        self._menuLineColor = menuLineColor
    def LRDisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('--------------------------------')
        return ret
    def TakeAttack(self, incomingATK):
        delta = incomingATK - self._DEF
        if delta < 0:
            delta = 0
        self._hp -= delta
    def MenuLine(self):
        return f'{self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK} | DEF {self._DEF}'
    def NameStr(self):
        return self._name