from LRDisplay import *
from CombatEntities import *
from CombatMenus import *
from CombatActions import *
import random

head1:PlayerHead = PlayerHead('Head 1', 17, 10, 1)
#head2:Head = Head('Head 2', 17, 10, 1)
heads:list=[head1]#, head2]
player:Player=Player(153,heads)
enemy1:Enemy = Enemy('Sword Goblin 1', 20, 9, 1, Fore.RED)
enemy2:Enemy = Enemy('Sword Goblin 2', 20, 9, 1, Fore.RED)
enemy3:Enemy = Enemy('Sword Goblin 3', 20, 9, 1, Fore.RED)
enemies=[enemy1, enemy2, enemy3]

lLines = []
lLines.extend(player.LRDisplayLines())

rLines = []
rLines.extend(enemy1.LRDisplayLines())
rLines.extend(enemy2.LRDisplayLines())
rLines.extend(enemy3.LRDisplayLines())

PrintMenu("PLAYER", 50, Fore.GREEN, "ENEMY", 50, Fore.RED, lLines, rLines)
print(Fore.WHITE, end='')

while len(enemies) > 0:
    headSelectables = [MenuItem(h) for h in heads]
    selectHeadMenu=Menu("Select Head", headSelectables, Fore.GREEN)
    allEnemiesDead = False
    while not selectHeadMenu.IsExhausted() and not allEnemiesDead:
        selectHeadMenu.Display()
        sHead = selectHeadMenu.ReadDisableSelection()._val
        enemySelectables = [MenuItem(e) for e in enemies]
        selectEnemyMenu=Menu("Select Enemy", enemySelectables, Fore.RED)
        selectEnemyMenu.Display()
        sEnemy = selectEnemyMenu.ReadDisableSelection()._val
        Attack(sHead, sEnemy)
        DiscardKilledEntities(enemies)
        allEnemiesDead = all([si._val._hp <= 0 for si in selectEnemyMenu._selectableItems])
    for e in enemies:
        targetHead = random.choice(heads)
        Attack(e, targetHead)
    RegenerateHeads(heads)
    print(Fore.WHITE)

print(Fore.GREEN + f'>----------You won combat!---------<')
print(Fore.WHITE)