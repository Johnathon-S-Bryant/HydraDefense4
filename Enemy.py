from colorama import Fore
from CombatEntityType import *
from AIAgent import AIAgent

class Enemy:
    _name = 'default-enemy-name-string'
    _hp = 20
    _maxHP = _hp
    _ATK = -1
    _DEF = -1
    #_AIAgent = 'ERROR-AI-Agent-Not-set'
    _menuLineColor = Fore.MAGENTA
    _combatEntityType = CombatEntityType.ENEMY

    def __init__(self, name:str, HP:int, maxHP:int, ATK:int, DEF:int, aiAgent:AIAgent,  menuLineColor:str):
        self._name:str = name
        self._hp:int = HP
        self._maxHP:int = maxHP
        self._ATK:int = ATK
        self._DEF:int = DEF
        self._AIAgent:AIAgent = aiAgent
        self._menuLineColor:str = menuLineColor

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