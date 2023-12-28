from PlayerHead import *
from Player import *
import random

#def EvenChanceAnyBodyPart(player:Player) -> list[int]:
#    return [1] * len(player.GetBodyParts())

"""def EvenChanceAnyHead(bodyParts) -> list[float]:
    heads = []
    ret:list[float] = []
    numHeads:int = len(list(filter(lambda bp: bp is PlayerHead,bodyParts)))
    headWeight:float = 1/numHeads
    for bp in bodyParts:
        if bp is PlayerHead:
            heads.append(headWeight)
        else:
            ret.append(0)
    return ret"""

def EvenChanceAnyHead(player:Player) -> PlayerHead:
    heads = player.GetHeads()
    return random.choices(heads, weights=[1]*len(heads), k=1)[0]

def EvenChanceAnyLeg(player:Player) -> PlayerLeg:
    legs = player.GetLegs()
    return random.choices(legs, weights=[1]*len(legs), k=1)[0]
