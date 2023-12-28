import yaml
from colorama import *
from Enemy import *
from AIAgent import *

def ReadEnemyFile(relativeFilePath:str) -> list[Enemy]:
    file=open(relativeFilePath)
    enemyYAML= yaml.safe_load(file)
    enemies:list[Enemy] = []
    for k, v in enemyYAML.items():
        aiAgent:AIAgent = AIAgent(enemyYAML[k]['AI'])
        enemy:Enemy = Enemy(enemyYAML[k]['name'], enemyYAML[k]['HP'], enemyYAML[k]['maxHP'], enemyYAML[k]['ATK'],
                            enemyYAML[k]['DEF'], aiAgent, Fore.RED)
        enemies.append(enemy)
    return enemies
