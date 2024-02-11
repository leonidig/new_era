import random
from personages import *


heroes = {
    'V': Hero('Валькирия', 40, 17, 20, 30, 'Маг - Чародей'),
    'O': Hero('Одрикс', 70, 3, 50, 10,'Танк'),
    'P': Hero('Папанистер', 55, 10, 20, 35, 'Всадник'),
    'D': Hero('Довбик', 50, 10, 30, 15,'Доблестный Пон')
}

for hero_key, hero_value in heroes.items():
    print(f'''\033[0;41m\033[0;31mИмя - {hero_value.name}\033[0m,
• Здоровье - {hero_value.hp},
• Мана - {hero_value.mana},
• Cила - {hero_value.strength},
• Ловкость - {hero_value.agility},
• Тип - {hero_value.Htype}\n''')

print('''\033[0;43mВыберите Персонажа:\033[0m
• V - Валькирия
• О - Одрикс
• P - Папанистер
• D - Довбик  
''')

monster = random.choice(all_monstres)
selected_hero = None

while selected_hero is None:
    u_input = input("Выберите Персонажа: ").upper()
    if u_input in heroes:
        selected_hero = heroes[u_input]
        print(f"\033[0;43mВыбран персонаж: {selected_hero.name}\nВраг - {monster.Htype}\033[0m")
    else:
        print("Некорректный выбор персонажа. Попробуйте еще раз.")

# Балансировка боя
if 0 < monster.hp <= 20 and 40 < selected_hero.hp >= 50:
    quantity = selected_hero.hp / monster.hp
    total_m_hp = quantity * monster.hp
    monster.hp = total_m_hp
    total_m_strength = quantity * monster.strength
    monster.strength = total_m_strength

    print(f'Сбалансирован бой: количество монстров - {quantity}, общее HP монстров - {total_m_hp}, общая сила монстров - {total_m_strength}')


while selected_hero.hp > 0 and monster.hp > 0:
    input(selected_hero.name + ', Нажми ENTER Для Атаки\n')

    hero_damage = random.randint(0, selected_hero.strength)
    if hero_damage <= 0:
        print(f'{selected_hero.name} промахнулся!')
    else:
        monster.hp -= hero_damage
        print(f'{selected_hero.name} Наносит Урон: {hero_damage}')
        print(f'Осталось HP у монстра: {monster.hp}')  # Добавлен вывод HP монстра после урона

        if monster.hp <= 0:
            print(f'{selected_hero.name} Убил {monster.Htype}\n')
            break

    monster_damage = random.randint(0, int(monster.strength))  # Преобразование к целому числу
    if monster_damage <= 0:
        print(f'{monster.Htype} промахнулся!')
    else:
        selected_hero.hp -= monster_damage
        print(f'{monster.Htype} Наносит Ответный Удар: {monster_damage} урона\n{selected_hero.name}: Оcталось {selected_hero.hp} HP')

        if selected_hero.hp <= 0:
            print(f'{monster.Htype} Убил {selected_hero.name}\n')
            break
