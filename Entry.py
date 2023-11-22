from LRDisplay import *
from CombatEntities import *
from CombatMenus import *
from CombatActions import *

head1:Head = Head('Head 1', 17, 10, 1, Fore.GREEN)
head2:Head = Head('Head 2', 17, 10, 1, Fore.GREEN)
heads:list=[head1, head2]
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

while True:
    selectHeadMenu=Menu("Select Head", heads)
    selectHeadMenu.Display(Fore.GREEN)
    sHead = selectHeadMenu.Read()
    selectEnemyMenu=Menu("Select Enemy", enemies)
    selectEnemyMenu.Display(Fore.RED)
    sEnemy = selectEnemyMenu.Read()
    Attack(sHead, sEnemy)
    print(Fore.WHITE)