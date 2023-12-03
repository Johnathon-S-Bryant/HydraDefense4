from LRDisplay import *
from CombatMenus import *
from CombatActions import *
from PlayerBody import *
from PlayerLeg import *
from PlayerTail import *
from Player import *
from Enemy import *
from LegPos import *
from PlayerFile import *
import random

playerFile:PlayerFileDS = ReadPlayerFile('Player.yaml')
heads:list[PlayerHead] = playerFile.Heads
body:PlayerBody = playerFile.Body
legs:dict[LegPos, PlayerLeg] = playerFile.Legs
bodyParts = {}
numHeads:int = len(heads)

for z in range(1, numHeads+6):
    if z <= numHeads:
        bodyParts[z] = heads[z-1]
    elif z == numHeads+1:
        bodyParts[z] = body
    elif z == numHeads+2:
        bodyParts[z]=legs[LegPos.FRONT_LEFT]
    elif z == numHeads+3:
        bodyParts[z]=legs[LegPos.FRONT_RIGHT]
    elif z == numHeads+4:
        bodyParts[z]=legs[LegPos.BACK_LEFT]
    elif z == numHeads+5:
        bodyParts[z]=legs[LegPos.BACK_RIGHT]

player=Player(50, bodyParts)


enemy1:Enemy = Enemy('Left-Leg-Attacker', 20, 9, 1, Fore.RED)
enemy2:Enemy = Enemy('Sword Goblin 2', 20, 9, 1, Fore.RED)
enemy3:Enemy = Enemy('Sword Goblin 3', 20, 9, 1, Fore.RED)
enemies=[enemy1, enemy2, enemy3]
#enemies=ReadInEnemies()


lLines = []
lLines.extend(player.FullLRDisplayLines())

rLines = []
for e in enemies:
    rLines.extend(e.LRDisplayLines())

cd = CombatDisplay("PLAYER", "ENEMY", 50, 50, Fore.GREEN, Fore.RED)

print(Fore.WHITE, end='')

while len(enemies) > 0:
    cd.PrintFullMenu(player, enemies)
    headSelectables = [MenuItem(h) for h in heads]
    selectHeadMenu = Menu("Select Head", headSelectables, Fore.GREEN)
    allEnemiesDead = False

    #PlayerAttacks
    while not selectHeadMenu.IsExhausted() and not allEnemiesDead:
        selectHeadMenu.Display()
        sHead = selectHeadMenu.ReadDisableSelection()._val
        enemySelectables = [MenuItem(e) for e in enemies]
        selectEnemyMenu = Menu("Select Enemy", enemySelectables, Fore.RED)
        selectEnemyMenu.Display()
        sEnemy = selectEnemyMenu.ReadDisableSelection()._val
        PlayerAttackEnemy(sHead, sEnemy)
        DiscardKilledEntities(enemies)
        allEnemiesDead = all([si._val._hp <= 0 for si in selectEnemyMenu._selectableItems])

    #EnemyAttacks
    for e in enemies:
        keys = player._bodyParts.keys()
        targetBodyPartID = random.choice(list(keys))
        EnemyAttackPlayer(e, player, targetBodyPartID)

    RegenerateHeads(heads)
    print(Fore.WHITE)

print(Fore.GREEN + f'>----------You won combat!---------<')
print(Fore.WHITE)