from colorama import Fore

class PlayerHead:
    _player = None
    Name = 'default-head-name-string'
    HP = 17
    MaxHP = HP
    ATK = -1
    DEF = -1
    _menuColorLine = Fore.GREEN
    def __init__(self,  name, HP, maxHP, ATK, DEF):
        self.Name = name
        self.HP = HP
        self.MaxHP = maxHP
        self.ATK = ATK
        self.DEF = DEF

    def LRDisplayLines(self) -> list[str]:
        ret = []
        ret.append(self.Name)
        ret.append(f'{self.HP} / {self.MaxHP}')
        ret.append('---------------')
        return ret

    def BodyPartName(self) -> str:
        return f'Head: {self.Name}'

    def TakeAttack(self, player, incomingATK) -> None:
        delta = incomingATK - self.DEF
        if delta < 0:
            delta = 0
        self.HP -= delta
        player.PoolHP -= delta

    def MenuLine(self) -> str:
        return f'{self.Name} | HP: {self.HP} / {self.MaxHP} | ATK: {self.ATK}'

    def NameStr(self) -> str:
        return self.Name

