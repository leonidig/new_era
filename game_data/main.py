import random
from personages import *



heroes = {
    'V': Hero('Валькирия', 'Д', 40, 17, 20, 30, 35, 'Маг - Чародей'),
    'O': Hero('Одрикс', 'М', 70, 3, 50, 10, 20, 'Танк'),
    'P': Hero('Папанистер', 'М', 55, 10, 20, 35, 37, 'Всадник')
}

for hero_key, hero_value in heroes.items():
    print(f'''\033[0;41m\033[0;31mИмя - {hero_value.name}\033[0m,
• Гендер - {hero_value.gender},
• Здоровье - {hero_value.hp},
• Мана - {hero_value.mana},
• Cила - {hero_value.strength},
• Ловкость - {hero_value.agility},
• Интеллект - {hero_value.intelligense},
• Тип - {hero_value.Htype}\n''')

print('''\033[0;43mВыберите Персонажа:\033[0m
• V - Валькирия
• О - Одрикс
• P - Папанистер
''')



monster = random.choice(all_monstres)
u_input = input("Выберите Персонажа: ").upper()

if u_input in heroes:
    selected_hero = heroes[u_input]
    print(f"Выбран персонаж: {selected_hero.name}\nВраг - {monster.Htype}")



while selected_hero.hp > 0 and monster.hp > 0:
    
    input(selected_hero.name + ', Нажми ENTER Для Атаки\n')


    hero_damage = random.randint(0, selected_hero.strength)
    monster.hp -= hero_damage
    print(f'{selected_hero.name} Наносит Урон : {hero_damage}')


    monster_damage = random.randint(0, monster.strength)
    selected_hero.hp -= monster_damage
    print(f'{monster.Htype} Наносит Ответный Удар: {monster_damage} урона\n{selected_hero.name}: Оcталось {selected_hero.hp} HP')
    
    if monster.hp > 0:
        print(f'{monster.Htype}: Осталось {monster.hp} HP\n')



if monster_damage == 0:
    print(monster.Htype + ' Промахнулся\n')


if hero_damage == 0:
    print(selected_hero.name + ' Промахнулся\n')


if selected_hero.hp > 0 and monster.hp <= 0:
        print(f'{selected_hero.name} Убил {monster.Htype}\n')


if monster.hp > 0 and selected_hero.hp <= 0:
        print(f'{selected_hero.name} Убил {monster.Htype}\n')