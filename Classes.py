import math
import base64
import random

k=';'
inventory_items = { k : base64.b64encode(bytes(k, 'utf-8'))}
print(inventory_items)

class Entity:
    def __init__(self, pos, max_health, resistance):
        self.res = resistance
        self.max_health = max_health
        self.inventory = ["Food" if b % 2 == 0 else "Water" for b in range(20)]

    def deal(self, other, dmg):
        other.max_health -= dmg-other.resistance

b=Entity("i", 20, 40)
print(b.inventory)
