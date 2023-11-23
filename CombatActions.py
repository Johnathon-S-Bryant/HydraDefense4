from CombatEntities import *

def Attack(attacker, defender):
    attackerATK = attacker._ATK
    print(f'{Fore.WHITE} {attacker._name} attacks {defender._name} for {attackerATK}')
    defender.ForceBodyPartTakeAttack(attackerATK)

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