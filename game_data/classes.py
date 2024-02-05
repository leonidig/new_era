import random

class Hero:

    def __init__(self, name, gender, hp, mana, strength, agility, 
                 intelligense, Htype=None) :
        self.name = name
        self.gender = gender
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intelligense = intelligense
        self.Htype = Htype
        self.xp = 0
        self.gold = 0


class Monster:
    def __init__(self, Htype, hp, mana, strength, agility, 
                 intelligense, xp, gold_range) :
        self.Htype = Htype
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intelligense = intelligense
        self.xp = xp
        self.gold = random.randint(*gold_range)
    


