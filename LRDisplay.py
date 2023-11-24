import math
from colorama import Fore
from Player import *
from Enemy import *


class CombatDisplay:
    _lHeader = 'default-string'
    _rHeader = 'default-string'
    _lLength = -1
    _rLength = -1
    _lColor = 'default-color'
    _rColor = 'default-color'
    def __init__(self, lHeader, rHeader, lLength, rLength, lColor, rColor):
        self._lHeader = lHeader
        self._rHeader = rHeader
        self._lLength = lLength
        self._rLength = rLength
        self._lColor = lColor
        self._rColor = rColor

    def PrintFullMenu(self, player:Player, liveEnemies:list):
        leftLines = player.FullLRDisplayLines()
        rightLines = []
        for le in liveEnemies:
            rightLines.extend(le.LRDisplayLines())
        self.PrintLines(leftLines, rightLines)

    def PrintMenuHeadsOnly(self, player:Player, liveEnemies:list):
        leftLines = player.HeadCombatDisplayLines()
        rightLines = []
        for le in liveEnemies:
            rightLines.extend(le.LRDisplayLines())
        self.PrintLines(leftLines, rightLines)

    def PrintLines(self, lLines:list, rLines:list):
        padHeaderL = " " * (self._lLength - len(self._lHeader))
        padHeaderR = " " * (self._rLength - len(self._rHeader))
        print(self._lColor + self._lHeader + padHeaderL + Fore.WHITE + '|' + self._rColor + self._rHeader + padHeaderR)
        lLinesLength = len(lLines)
        rLinesLength = len(rLines)
        numLines = int(math.floor(max(lLinesLength, rLinesLength)))
        newLLines = []
        newRLines = []
        for z in range(numLines):
            if z <= lLinesLength - 1:
                newLLines.append(lLines[z])
            else:
                newLLines.append("")
        for z in range(numLines):  # range(rLinesLength):
            if z <= rLinesLength - 1:
                newRLines.append(rLines[z])
            else:
                newRLines.append("")
        print(Fore.WHITE, end='')
        for z in range(self._lLength + self._rLength):
            print('-', end='')
        print()
        for z in range(numLines):
            toPrintL = newLLines[z]
            toPrintR = newRLines[z]
            padL = " " * (self._lLength - len(toPrintL))
            padR = " " * (self._rLength - len(toPrintR))
            print(self._lColor + toPrintL + padL + Fore.WHITE + '|' + self._rColor + toPrintR + padR)
            print(Fore.WHITE, end='')


"""def PrintMenu(lHeader:str, lLength:int, lColor:str, rHeader:str, rLength:int, rColor:str, lLines:list, rLines:list):
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
    for z in range(numLines):
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
        print(lColor + toPrintL + padL + Fore.WHITE + '|' + rColor + toPrintR + padR)"""