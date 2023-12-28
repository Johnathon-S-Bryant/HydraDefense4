from PlayerHead import *
from Player import Player
from CombatEntityType import *

def PlayerAttackEnemy(attacker, defender):
    attackerATK = attacker.ATK
    print(f'{Fore.WHITE} {attacker.Name} attacks {defender.Name} for {attackerATK}')
    defender.TakeAttack(attackerATK)

def EnemyAttackPlayer(attacker, player, bodyPart): #, bodyPartID):
    attackerATK = attacker.ATK
    #bodyPart = player._bodyParts.get(bodyPartID)
    print(f'{Fore.WHITE} {attacker.Name} attacks {bodyPart.BodyPartName()} for {attackerATK}')
    bodyPart.TakeAttack(player, attackerATK)
    #player.ForceBodyPartTakeAttack(bodyPartID, attackerATK)

def DiscardKilledEntities(killables) -> None:
    for k in killables:
        if k.HP <= 0:
            killables.remove(k)

def RegenerateHeads(heads:list[PlayerHead], player:Player) -> None:
    for h in heads:
        if h.HP <= 0:
            newHead1:PlayerHead = PlayerHead(f'{h.Name}-1', h.MaxHP, h.MaxHP, h.ATK, h.DEF)
            newHead2:PlayerHead = PlayerHead(f'{h.Name}-2', h.MaxHP, h.MaxHP, h.ATK, h.DEF)
            heads.remove(h)
            bodyParts = player.BodyParts
            deletionIndex:int = -99
            for k, v in bodyParts.items():
                if h == v:
                    deletionIndex = k
            if not deletionIndex == -99:
                del bodyParts[deletionIndex]
            maxPlayerBodyPartID = max(player.BodyParts.keys())
            player.BodyParts[maxPlayerBodyPartID+1] = newHead1
            player.BodyParts[maxPlayerBodyPartID+2] = newHead2
