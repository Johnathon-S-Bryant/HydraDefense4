from colorama import Fore
from CombatEntities import *

class Menu:
    _header = "default-menu-header"
    _selectableItems = []
    _defaultColor = Fore.WHITE
    def __init__(self, header, selectableItems):
        self._header = header
        self._selectableItems = selectableItems
    def Display(self, headerColor):
        print(headerColor + self._header)
        print(Fore.WHITE + '-------------------')
        selectableItems = self._selectableItems
        for z in range(1, len(selectableItems)+1):
            print(f'{z}|{selectableItems[z-1].MenuLine()}{self._defaultColor}')
        print(Fore.WHITE,end='')
    def Read(self):
        validInput = False
        lBound = 1
        selectableItems = self._selectableItems
        uBound= len(selectableItems)
        while not validInput:
            i = input()
            intI = int(i)
            if intI >= lBound and intI <= uBound:
                validInput = True
        return selectableItems[intI-1]


"""def DisplaySelectHeadMenu(player:Player):
    print(Fore.GREEN + 'Select Head')
    print(Fore.WHITE + '-------------------')
    heads = player._heads
    for z in range(1, len(heads)+1):
        print(f'{Fore.GREEN}{z}|{heads[z-1]._name}')

def ReadSelectHeadMenu(player:Player):
    validInput = False
    lBound = 1
    heads = player._heads
    uBound= len(heads)+1
    while not validInput:
        i = input()
        intI = int(i)
        if intI >= lBound and intI <= uBound:
            validInput = True
    return heads[intI]
"""