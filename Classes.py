import math

class Entity:
    def __init__(self, pos, max_health, resistance):
        self.res = resistance
        self.max_health = max_health