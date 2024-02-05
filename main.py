from classes import *
import random


hero_2 = Hero('Валькирия', 'Д', 40, 17, 20, 30, 35)
hero_1 = Hero('Одрикс', 'М', 70, 3, 50, 10, 20)

monster_2 = Monster('Гоблин', 15, 2, 7, 10, 1, 25, (0, 25))
monster_1 = Monster('Огр', 150, 1, 20, 5, 20, 30, (30, 270))
monster_3 = Monster('Летун', 45, 7, 10, 17, 20, 10, (25, 200))

while hero_2.hp > 0 and monster_1.hp > 0:
    
    input(hero_2.name + ', Нажми ENTER Для Атаки')
    
    damage = random.randint(0, hero_2.strength)
    monster_1.hp -= damage
    print(hero_2.name + ' Наносит Урон ' + str(damage))
    
    if monster_1.hp <= 0:
        print(monster_1.Htype + ' Умер')
    
    if hero_2.hp <= 0:
        print(hero_2.Htype + ' Умер')

    else:
        print(monster_1.Htype + ': Осталось HP ' + str(monster_1.hp))


    input(monster_1.Htype + ' Наносит Ответный Удар')
    damage = random.randint(0, monster_1.strength)
    hero_2.hp -= damage
    print(monster_1.Htype + ' Наносит Урон ' + str(damage))
    print(hero_2.name + ': Осталось HP ' + str(hero_2.hp))


if hero_2.hp < 0:
    print(hero_2.name + ' Победил!' + monster_1.Htype + ' Проиграл !')

elif monster_1.hp <= 0:
    print(monster_1.Htype + ' Победил! ' +  hero_2.name + ' Проиграл! ')

else:
    print('Все Погибли! Ничья')
 