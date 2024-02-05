from classes import *
from personages import *
import random

person_list = ['V', 'O', 'P']

def menu():
    f'''
    ************************
    Добро Пожаловать В Меню
    ************************
    Вот Описание Персонажей :
    '''
    heroes = [
        Hero('Валькирия', 'Д', 40, 17, 20, 30, 35, 'Маг - Чародей'),
        Hero('Одрикс', 'М', 70, 3, 50, 10, 20, 'Танк'),
        Hero('Папанистер', 'М', 55, 10, 20, 35, 37, 'Всадник')
    ]

    for hero in heroes:
        print(f'''\033[0;31mИмя - {hero.name}\033[0m,
• Гендер - {hero.gender},
• Здоровье - {hero.hp},
• Мана - {hero.mana},
• Cила - {hero.strength},
• Ловкость - {hero.agility},
• Интеллект - {hero.intelligense},
• Тип - {hero.Htype}''')

menu()

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
 