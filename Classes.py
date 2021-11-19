import math
import base64
import random

id_dict = {
    1: "Uncooked Canned Beans",
    2: "Cooked Cannced Beans",
    3: "Bottled Freshwater",
    4: "Bottled Saltwater",
    5: "Match",
    6: "Flashlight 100W",
    7: "Flashlight 200W",
    8: "Flashlight 500W",
    9: "Pure Dark",
    10: "Sorrowed Sword",
    11: "Sorrowed Digger",
    12: "Sorrowed Spear",
    13: "Sorrowed Bow",
    14: "Reaper Sword",
    15: "Reaper Digger",
    16: "Reaper Spear",
    17: "Reaper Bow",
    18: "Ghost Sword",
    19: "Ghost Digger",
    20: "Ghost Spear",
    21: "Ghost Bow",
    22: "Electromagnet Sword",
    23: "Electromagnet Digger",
    24: "Electromagnet Spear",
    25: "Electromagnet Bow",
    26: "Generation Sword",
    27: "Generation Digger",
    28: "Generation Spear",
    29: "Generation Bow",
    30: "Elder Sword",
    31: "Elder Digger",
    32: "Elder Spear",
    33: "Elder Bow",
    34: "Gladius Deorum",  # Sword of the Gods
    35: "Fodinarum Somnium",  # Miner's Dream
    36: "Hasta Puritatis",  # Spear of Purity
    37: "Custodis Arcus"  # Warden's Bow

}


class Entity:
    def __init__(self, pos, max_health, resistance):
        self.res = resistance
        self.max_health = max_health
        self.inventory = ["Food" if b % 2 == 0 else "Water" for b in range(20)]
        self.selected_item = 0
        self.accessible = self.inventory[:7]

    def attack(self, other, dmg):
        other.max_health -= dmg - other.resistance
        self.accessible[self.selected_item].durability -= 1


b = Entity("i", 20, 40)
print(b.inventory)


class Inventory:
    def __init__(self, id_, quantity, effects):
        self.id = id_
        self.quantity = quantity

    def use(self, effects):
        # 3 tools
        # 7 tiers
        pass
