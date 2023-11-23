from colorama import Fore
from CombatEntities import *

class MenuItem:
    _enabled = True
    def __init__(self, val):
        self._val = val
    def MenuLine(self):
        return self._val.MenuLine()

class Menu:
    _header = "default-menu-header"
    _selectableItems = []
    _color = Fore.MAGENTA
    def __init__(self, header, selectableItems, color):
        self._header = header
        self._selectableItems = selectableItems
        self._color = color
    def Display(self):
        print(self._color + self._header)
        print(Fore.WHITE + '-------------------')
        selectableItems = self._selectableItems
        for z in range(1, len(selectableItems)+1):
            currentItem = selectableItems[z-1]
            currentColor = self._color if currentItem._enabled else Fore.WHITE
            print(f'{Fore.WHITE}{z}|{currentColor}{currentItem.MenuLine()}{Fore.WHITE}')
    def ReadDisableSelection(self):
        validInput = False
        lBound = 1
        uBound= len(self._selectableItems)
        alreadySelectedItems = list(filter(lambda si: not si._enabled, self._selectableItems))
        while not validInput:
            i = input()
            intI = int(i)
            if intI >= lBound and intI <= uBound:
                currentSelectable = self._selectableItems[intI-1]
                if currentSelectable not in alreadySelectedItems:
                    validInput = True
        currentSelectable._enabled = False
        return currentSelectable
    def IsExhausted(self):
        return all([not si._enabled for si in self._selectableItems]) 

        


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