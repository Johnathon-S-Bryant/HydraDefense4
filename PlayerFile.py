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
    nameString = playerYAML['player']['name']
    heads:list[PlayerHead] = []
    yamlHeads= playerYAML['player']['bodyparts']['heads']
    for v in yamlHeads.values():
        heads.append(PlayerHead(v['name'], v['HP'], v['maxHP'], v['ATK'], v['DEF']))
    tailYAML = playerYAML['player']['bodyparts']['tail']
    playerTail = PlayerTail(tailYAML['HP'], tailYAML['maxHP'], tailYAML['DEF'])
    bodyYAML = playerYAML['player']['bodyparts']['body']
    playerBody = PlayerBody(bodyYAML['DEF'])
    frontLeftLegYAML = playerYAML['player']['bodyparts']['front_left_leg']
    flLeg = PlayerLeg(LegPos.FRONT_LEFT, frontLeftLegYAML['HP'], frontLeftLegYAML['maxHP'], frontLeftLegYAML['DEF'])
    frontRightLegYAML = playerYAML['player']['bodyparts']['front_right_leg']
    frLeg = PlayerLeg(LegPos.FRONT_RIGHT,frontRightLegYAML['HP'], frontRightLegYAML['maxHP'], frontLeftLegYAML['DEF'])
    backLeftLegYAML = playerYAML['player']['bodyparts']['back_left_leg']
    blLeg = PlayerLeg(LegPos.BACK_LEFT, backLeftLegYAML['HP'], backLeftLegYAML['maxHP'], backLeftLegYAML['DEF'])
    backRightLegYAML = playerYAML['player']['bodyparts']['back_right_leg']
    brLeg = PlayerLeg(LegPos.BACK_RIGHT, backRightLegYAML['HP'], backRightLegYAML['maxHP'], backRightLegYAML['DEF'])
    legs = {
        LegPos.FRONT_LEFT:flLeg,
        LegPos.FRONT_RIGHT:frLeg,
        LegPos.BACK_LEFT:blLeg,
        LegPos.BACK_RIGHT:brLeg
    }
    return PlayerFileDS(nameString, heads, playerTail, playerBody, legs)
