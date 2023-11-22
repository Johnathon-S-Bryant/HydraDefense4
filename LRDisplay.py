import math
from colorama import Fore

def PrintMenu(lHeader:str, lLength:int, lColor:str, rHeader:str, rLength:int, rColor:str, lLines:list, rLines:list):
    padHeaderL = " " * (lLength-len(lHeader))
    padHeaderR = " " * (rLength-len(rHeader))
    print(lColor + lHeader + padHeaderL + Fore.WHITE + '|' + rColor + rHeader + padHeaderR)
    lLinesLength = len(lLines)
    rLinesLength = len(rLines)
    numLines = int(math.floor(max(lLinesLength, rLinesLength)))
    newLLines = []
    newRLines = []
    for z in range(numLines):
        if z <= lLinesLength-1:
            newLLines.append(lLines[z])
        else:
            newLLines.append("")
    for z in range(rLinesLength):
        if z <= rLinesLength-1:
            newRLines.append(rLines[z])
        else:
            newRLines.append("")
    print(Fore.WHITE, end='')
    for z in range(lLength+rLength):
        print('-', end='')
    print()
    for z in range(numLines):
        toPrintL = newLLines[z]
        toPrintR = newRLines[z]
        padL = " " * (lLength-len(toPrintL))
        padR = " " * (rLength-len(toPrintR))
        print(lColor + toPrintL + padL + Fore.WHITE + '|' + rColor + toPrintR + padR)

"""
lString = Pool HP: 134
-------------------
HEAD 1
HP: 17 / 17
-----------------------------
HEAD 2
HP: 17 / 17
-----------------------------
lLines = lString.split('\n')
rString = Sword Goblin 1
HP: 20 / 20
Planned Action: <Write a function to generate this>
--------------------------------------------------
Sword Goblin 2
HP: 20 / 20
Planned Action: <Write a function to generate this>
--------------------------------------------------
rLines = rString.split('\n')
"""

"""
class Head:
    _name = 'default-head-name-string'
    _hp = 17
    _maxHP = _hp
    def __init__(self, name,  maxHP):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
    def DisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('---------------')
        return ret
class Player:
    _poolHP = 134
    _heads = []
    def __init__(self, poolHP, heads:list):
        self._poolHP = poolHP
        self._heads = heads
    def DisplayLines(self):
        ret = []
        for h in self._heads:
            ret.extend(h.DisplayLines())
        return ret
class Enemy:
    _name = 'default-enemy-name-string'
    _hp = 20
    _maxHP = _hp
    def __init__(self, name,  maxHP):
        self._name = name
        self._hp = maxHP
        self._maxHP = maxHP
    def DisplayLines(self):
        ret = []
        ret.append(self._name)
        ret.append(f'{self._hp} / {self._maxHP}')
        ret.append('--------------------------------')
        return ret
"""

"""
head1:Head = Head('Head 1', 17)
head2:Head = Head('Head 2', 17)
heads:list=[head1, head2]
player:Player=Player(153,heads)
enemy1:Enemy = Enemy('Sword Goblin 1', 20)
enemy2:Enemy = Enemy('Sword Goblin 2', 20)
enemy3:Enemy = Enemy('Sword Goblin 3', 20)

lLines = []
lLines.extend(player.DisplayLines())

rLines = []
rLines.extend(enemy1.DisplayLines())
rLines.extend(enemy2.DisplayLines())
rLines.extend(enemy3.DisplayLines())

PrintMenu("PLAYER", 50, Fore.GREEN, "ENEMY", 50, Fore.RED, lLines, rLines)
print(Fore.WHITE, end='')
"""