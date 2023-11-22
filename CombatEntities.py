class Head:
    _name = 'default-head-name-string'
    _hp = 17
    _maxHP = _hp
    _ATK = -1
    def __init__(self, name,  maxHP, ATK):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
        self._ATK = ATK
    def LRDisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('---------------')
        return ret
    def MenuLine(self):
        return f' {self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK}'
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
    def __init__(self, name,  maxHP, ATK):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
        self._ATK = ATK
    def LRDisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('--------------------------------')
        return ret
    def MenuLine(self):
        return f' {self._name} | HP: {self._hp} / {self._maxHP} | ATK: {self._ATK}'
    def NameStr(self):
        return self._name