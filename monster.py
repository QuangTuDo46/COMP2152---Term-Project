import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()

    def monster_attacks(self):
        attack_value = random.randint(3, 12)
        print(f"Monster attacks with power {attack_value}!")
        return attack_value

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector.")
        super().__del__()
