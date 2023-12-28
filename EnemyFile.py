import yaml
from colorama import *
from Enemy import *
from AIAgent import *

def ReadEnemyFile(relativeFilePath:str) -> list[Enemy]:
    file=open(relativeFilePath)
    enemyYAML= yaml.safe_load(file)
    enemies:list[Enemy] = []
    for k, v in enemyYAML.items():
        name:str = k
        aiAgent:AIAgent = AIAgent(enemyYAML[name]['AI'])
        enemy:Enemy = Enemy(name, enemyYAML[name]['HP'], enemyYAML[name]['maxHP'], enemyYAML[name]['ATK'],
                            enemyYAML[name]['DEF'], aiAgent, Fore.RED)
        enemies.append(enemy)
    return enemies
