def Attack(attacker, defender):
    delta = attacker._ATK - defender._DEF
    if delta < 0:
        delta = 0
    print(f'{attacker._name} attacks {defender._name} for {delta}!')
    defender._hp -= delta