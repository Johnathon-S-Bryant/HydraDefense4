from colorama import Fore
from CombatEntityType import *
from AIAgent import AIAgent

class Enemy:
    Name = 'default-enemy-name-string'
    HP = 20
    MaxHP = HP
    ATK = -1
    DEF = -1
    #_AIAgent = 'ERROR-AI-Agent-Not-set'
    MenuLineColor = Fore.MAGENTA
    _combatEntityType = CombatEntityType.ENEMY

    def __init__(self, name:str, HP:int, maxHP:int, ATK:int, DEF:int, aiAgent:AIAgent,  menuLineColor:str):
        self.Name:str = name
        self.HP:int = HP
        self.MaxHP:int = maxHP
        self.ATK:int = ATK
        self.DEF:int = DEF
        self.AIAgent:AIAgent = aiAgent
        self.MenuLineColor:str = menuLineColor

    def LRDisplayLines(self):
        ret = []
        ret.append(self.Name)
        ret.append(f'{self.HP} / {self.MaxHP}')
        ret.append('--------------------------------')
        return ret
    def TakeAttack(self, incomingATK):
        delta = incomingATK - self.DEF
        if delta < 0:
            delta = 0
        self.HP -= delta
    def MenuLine(self):
        return f'{self.Name} | HP: {self.HP} / {self.MaxHP} | ATK: {self.ATK} | DEF {self.DEF}'
    def NameStr(self):
        return self.Name