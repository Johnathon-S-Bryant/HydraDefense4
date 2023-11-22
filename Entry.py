from LRDisplay import *
from CombatEntities import *
from CombatMenus import *

head1:Head = Head('Head 1', 17, 10)
head2:Head = Head('Head 2', 17, 10)
heads:list=[head1, head2]
player:Player=Player(153,heads)
enemy1:Enemy = Enemy('Sword Goblin 1', 20, 9)
enemy2:Enemy = Enemy('Sword Goblin 2', 20, 9)
enemy3:Enemy = Enemy('Sword Goblin 3', 20, 9)
enemies=[enemy1, enemy2, enemy3]

lLines = []
lLines.extend(player.LRDisplayLines())

rLines = []
rLines.extend(enemy1.LRDisplayLines())
rLines.extend(enemy2.LRDisplayLines())
rLines.extend(enemy3.LRDisplayLines())

PrintMenu("PLAYER", 50, Fore.GREEN, "ENEMY", 50, Fore.RED, lLines, rLines)
print(Fore.WHITE, end='')

selectHeadMenu=Menu("Select Head", heads)
selectHeadMenu.Display(Fore.GREEN)
selectHeadMenu.Read()



selectEnemyMenu=Menu("Select Enemy", enemies)
selectEnemyMenu.Display(Fore.RED)
selectEnemyMenu.Read()




print(Fore.WHITE)