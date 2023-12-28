from PlayerHead import *
from CombatEntityType import *

def PlayerAttackEnemy(attacker, defender):
    attackerATK = attacker._ATK
    print(f'{Fore.WHITE} {attacker._name} attacks {defender._name} for {attackerATK}')
    defender.TakeAttack(attackerATK)

def EnemyAttackPlayer(attacker, player, bodyPart): #, bodyPartID):
    attackerATK = attacker._ATK
    #bodyPart = player._bodyParts.get(bodyPartID)
    print(f'{Fore.WHITE} {attacker._name} attacks {bodyPart.BodyPartName()} for {attackerATK}')
    bodyPart.TakeAttack(player, attackerATK)
    #player.ForceBodyPartTakeAttack(bodyPartID, attackerATK)

def DiscardKilledEntities(killables):
    for k in killables:
        if k._hp <= 0:
            killables.remove(k)

def RegenerateHeads(heads):
    for h in heads:
        if h._hp <= 0:
            newHead1:PlayerHead = PlayerHead(f'{h._name}-1', h._maxHP, h._ATK, h._DEF)
            newHead2:PlayerHead = PlayerHead(f'{h._name}-2', h._maxHP, h._ATK, h._DEF)
            heads.remove(h)
            heads.append(newHead1)
            heads.append(newHead2)