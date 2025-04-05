import os
import platform
from hero import Hero
from monster import Monster

def check_os_and_version():
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")

def dream_levels():
    while True:
        try:
            level = int(input("Enter a dream level (0-3): "))
            if 0 <= level <= 3:
                print(f"Dream level {level} selected.")
                break
            else:
                print("Please enter a number between 0-3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 0-3.")

def save_game(monsters_killed):
    with open("save.txt", "w") as file:
        file.write(f"Monsters Killed: {monsters_killed}\n")

def load_game():
    try:
        with open("save.txt", "r") as file:
            return int(file.readline().strip().split(": ")[1])
    except FileNotFoundError:
        return 0

def main():
    check_os_and_version()

    hero = Hero()
    monster = Monster()

    monsters_killed = load_game()

    while hero.health_points > 0 and monster.health_points > 0:
        damage = hero.hero_attacks()
        monster.health_points = max(0, monster.health_points - damage)

        if monster.health_points <= 0:
            monsters_killed += 1
            print("Monster defeated!")
            break

        if hero.health_points > 0:
            damage = monster.monster_attacks()
            hero.health_points = max(0, hero.health_points - damage)

        if hero.health_points <= 0:
            print("Hero defeated! Game Over.")
            break

    save_game(monsters_killed)

if __name__ == "__main__":
    main()

import random

board = [[random.choice(['Potion', 'Trap', 'Empty']) for _ in range(5)] for _ in range(5)]

def explore_cell(hero, x, y):
    cell = board[x][y]
    print(f"Hero explores cell ({x}, {y}) and finds: {cell}")
    if cell == 'Potion':
        print("You found a Potion of Power! Combat strength increased.")
        hero.combat_strength += 5
    elif cell == 'Trap':
        print("You fell into a trap! Health points reduced.")
        hero.health_points = max(0, hero.health_points - 10)
    else:
        print("This cell is empty. Keep exploring.")

