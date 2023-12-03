from LRDisplay import *
from CombatMenus import *
from CombatActions import *
from PlayerBody import *
from PlayerLeg import *
from PlayerTail import *
from Player import *
from Enemy import *
from LegPos import *
import random

head1:PlayerHead = PlayerHead('Head 1', 17, 10, 1)
head2:PlayerHead = PlayerHead('Head 2', 17, 9, 2)
body:PlayerBody = PlayerBody(10, 10)
tail:PlayerTail = PlayerTail(10, 5)
leg1:PlayerLeg = PlayerLeg(LegPos.FRONT_LEFT, 10, 5)
leg2:PlayerLeg = PlayerLeg(LegPos.FRONT_RIGHT, 10, 5)
leg3:PlayerLeg = PlayerLeg(LegPos.BACK_LEFT, 10, 5)
leg4:PlayerLeg = PlayerLeg(LegPos.BACK_RIGHT, 10, 5)
heads:list=[head1, head2]
bodyParts = {
    1:head1,
    2:head2,
    3:body,
    4:tail,
    5:leg1,
    6:leg2,
    7:leg3,
    8:leg4,
}
player:Player = Player(50, bodyParts)
enemy1:Enemy = Enemy('Left-Leg-Attacker', 20, 9, 1, Fore.RED)
enemy2:Enemy = Enemy('Sword Goblin 2', 20, 9, 1, Fore.RED)
enemy3:Enemy = Enemy('Sword Goblin 3', 20, 9, 1, Fore.RED)
enemies=[enemy1, enemy2, enemy3]

lLines = []
lLines.extend(player.FullLRDisplayLines())

rLines = []
rLines.extend(enemy1.LRDisplayLines())
rLines.extend(enemy2.LRDisplayLines())
rLines.extend(enemy3.LRDisplayLines())

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