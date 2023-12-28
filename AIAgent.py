from AITargetSelectionType import *
from typing import Callable
from EnemyAttackWeights import *

class AIAgent:

    def __init__(self, agentStr:str):
        tokens:list[str] = agentStr.split('|')
        self.Power = int(tokens[0])
        self.TargetSelectionFunction:Callable = self.GetTargetSelectionFunction(tokens[1])

    """def GetTargetSelectionFunction(self) -> Callable:
        match self.TargetSelectionType:
            case AITargetSelectionType.NOT_SET:
                return EvenChanceAnyHead
            case AITargetSelectionType.EVEN_ANY_HEAD:
                return EvenChanceAnyHead
            case AITargetSelectionType.EVEN_ANY_LEG:
                return EvenChanceAnyLeg"""

    def GetTargetSelectionFunction(self, selectionTypeString:str) -> Callable:
        match selectionTypeString.upper():
            case 'EVEN-ANY-HEAD':
                return EvenChanceAnyHead
            case 'EVEN-ANY-LEG':
                return EvenChanceAnyLeg
        return EvenChanceAnyHead #Default case
