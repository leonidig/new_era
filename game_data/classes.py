import random

class Hero:

    def __init__(self, name, hp, mana, strength, agility, 
                 Htype=None) :
        self.name = name
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.Htype = Htype
        self.xp = 0
        self.gold = 0


class Monster:
    def __init__(self, Htype, hp, mana, strength, agility, 
                 xp, gold_range) :
        self.Htype = Htype
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.xp = xp
        self.gold = random.randint(*gold_range)
    


