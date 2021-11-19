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
    9: "Pure Light",
    10: "Pure Dark",
    11: "Sorrowed Sword",
    12: "Sorrowed Digger",
    13: "Sorrowed Spear",
    14: "Sorrowed Bow",
    15: "Reaper Sword",
    16: "Reaper Digger",
    17: "Reaper Spear",
    18: "Reaper Bow",
    19: "Ghost Sword",
    20: "Ghost Digger",
    21: "Ghost Spear",
    22: "Ghost Bow",
    23: "Electromagnet Sword",
    24: "Electromagnet Digger",
    25: "Electromagnet Spear",
    26: "Electromagnet Bow",
    27: "Generation Sword",
    28: "Generation Digger",
    29: "Generation Spear",
    30: "Generation Bow",
    31: "Elder Sword",
    32: "Elder Digger",
    33: "Elder Spear",
    34: "Elder Bow",
    35: "Gladius Deorum",  # Sword of the Gods
    36: "Fodinarum Somnium",  # Miner's Dream
    37: "Hasta Puritatis",  # Spear of Purity
    38: "Custodis Arcus",  # Warden's Bow
    39: "Wrench",

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
