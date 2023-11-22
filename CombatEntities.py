from colorama import Fore 

class Head:
    _name = 'default-head-name-string'
    _hp = 17
    _maxHP = _hp
    _ATK = -1
    _DEF = -1
    _menuColorLine = Fore.MAGENTA
    def __init__(self, name,  maxHP, ATK, DEF, menuColorLine):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
        self._ATK = ATK
        self._DEF = DEF
        self._menuColorLine = menuColorLine
    def LRDisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('---------------')
        return ret
    def MenuLine(self):
        return f'{self._menuColorLine} {self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK}'
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
    def MenuLine(self):
        return f'{self._menuLineColor} {self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK}'
    def NameStr(self):
        return self._name