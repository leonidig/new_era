import random

def ag_chance():
    chance = random.randint(1,5)

    if chance == 1:
        return True
    else:
        return False
    
if ag_chance():
    print('Персонаж увернулся!')

else:
    print('Персонаж не увернулся!')