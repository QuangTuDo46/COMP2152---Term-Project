import random
from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()

    def hero_attacks(self):
        attack_value = random.randint(5, 15)
        print(f"Hero attacks with power {attack_value}!")
        return attack_value

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector.")
        super().__del__()
