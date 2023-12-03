import yaml

def ReadEnemyFile(relativeFilePath:str):
    file=open(relativeFilePath)
    enemyYAML= yaml.safe_load(file)
