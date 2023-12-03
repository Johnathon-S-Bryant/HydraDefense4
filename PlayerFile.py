#from yaml import *
import yaml
from PlayerHead import *
from PlayerBody import *
from PlayerTail import *
from LegPos import *
from PlayerLeg import *

class PlayerFileDS:
    def __init__(self, nameString:str, heads:list[PlayerHead], tail:PlayerTail, body:PlayerBody, legs:dict[LegPos, PlayerLeg]):
        self.NameString = nameString
        self.Heads:list[PlayerHead] = heads
        self.Tail:PlayerTail = tail
        self.Body:PlayerBody = body
        self.Legs:dict[LegPos, PlayerLeg] = legs


def ReadPlayerFile(relativeFilePath:str) -> PlayerFileDS:
    file = open(relativeFilePath)
    playerYAML = yaml.safe_load(file)
    nameString = playerYAML['name']
    heads:list[PlayerHead] = []
    yamlHeads= playerYAML['bodyparts']['heads']
    for v in yamlHeads.values():
        heads.append(PlayerHead(v['name'], v['HP'], v['maxHP'], v['ATK'], v['DEF']))
    tailYAML = playerYAML['bodyparts']['tail']
    playerTail = PlayerTail(tailYAML['HP'], tailYAML['maxHP'], tailYAML['DEF'])
    bodyYAML = playerYAML['bodyparts']['body']
    playerBody = PlayerBody(bodyYAML['DEF'])
    frontLeftLegYAML = playerYAML['bodyparts']['front-left-leg']
    flLeg = PlayerLeg(LegPos.FRONT_LEFT, frontLeftLegYAML['HP'], frontLeftLegYAML['maxHP'], frontLeftLegYAML['DEF'])
    frontRightLegYAML = playerYAML['bodyparts']['front-right-leg']
    frLeg = PlayerLeg(LegPos.FRONT_RIGHT,frontRightLegYAML['HP'], frontRightLegYAML['maxHP'], frontLeftLegYAML['DEF'])
    backLeftLegYAML = playerYAML['bodyparts']['back-left-leg']
    blLeg = PlayerLeg(LegPos.BACK_LEFT, backLeftLegYAML['HP'], backLeftLegYAML['maxHP'], backLeftLegYAML['DEF'])
    backRightLegYAML = playerYAML['bodyparts']['back-right-leg']
    brLeg = PlayerLeg(LegPos.BACK_RIGHT, backRightLegYAML['HP'], backRightLegYAML['maxHP'], backRightLegYAML['DEF'])
    legs = {
        LegPos.FRONT_LEFT:flLeg,
        LegPos.FRONT_RIGHT:frLeg,
        LegPos.BACK_LEFT:blLeg,
        LegPos.BACK_RIGHT:brLeg
    }
    return PlayerFileDS(nameString, heads, playerTail, playerBody, legs)
