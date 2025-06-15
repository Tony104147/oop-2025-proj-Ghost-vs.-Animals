# -*- coding utf-8 -*-

import random
import numpy as np

import pygame

from lib.counter import Counter
from object import Object
from object.character import Character

class Bat(Character):
    ''''''
    def __init__(self, pos: tuple[int], name: str = None):
        super().__init__(rect=(*pos, 72, 72),
                         image='bat',
                         Name="bat",
                         MAX_HP=100.0,
                         HP=100.0,
                         ATK=10.0,
                         DEF=10.0,
                         speed=8)
        if name: self.Name = name
        self.attack_clock = Counter(240)
        self.move_clock = Counter(30)
        self.offset = (0, 0)
        
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        # Move
        if self.move_clock.ok():
            radius = 200
            x, y = informations["MAINCHARACTER"].rect.center
            x = random.uniform(x - radius, x + radius) - self.rect.centerx
            y = random.uniform(y - radius, y + radius) - self.rect.centery
            self.offset = pygame.math.Vector2(x, y)
            self.offset.scale_to_length(self["speed"])
            self.move_clock.reset(random.randint(10, 30))
        super().move(self.offset, informations["GROUPS"]["BLOCKS"], informations['RESTRICTION'])

        # attack
        if self.attack_clock.ok(False) and pygame.sprite.collide_rect(self, informations["MAINCHARACTER"]):
            informations["MAINCHARACTER"].attacked(self["ATK"])
            print(f"You are attacked by {self['Name']} | HP: {int(informations['MAINCHARACTER']['HP'])}")
            self.attack_clock.reset()

        # Call parent class update
        super().update(informations)