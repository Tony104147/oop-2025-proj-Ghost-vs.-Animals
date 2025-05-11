# -*- coding utf-8 -*-

import random
import numpy as np

import pygame

from lib.counter import Counter
from object import Object
from object.character import Character
from images import GETIMAGE

class Bat(Character):
    ''''''
    def __init__(self, pos: tuple[int]):
        super().__init__(rect=(*pos, 36, 36),
                         image=GETIMAGE("bat"),
                         Name="bat",
                         MAX_HP=100.0,
                         HP=100.0,
                         ATK=10.0,
                         DEF=10.0,
                         speed=2)
        
        self.attack_clock = Counter(240)
        self.move_count = 0
        self.offset = (0, 0)
        
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):

        # Move
        if self.move_count == 0:
            radius = 150
            x, y = informations["MAINCHARACTER"].rect.topleft
            x = random.uniform(x - radius, x + radius) - self.rect.x
            y = random.uniform(y - radius, y + radius) - self.rect.y
            self.offset = pygame.math.Vector2(np.sign(x), np.sign(y))
            self.offset.scale_to_length(self["speed"])
            self.move_count = random.randint(10, 30)
        self.move_count -= 1
        self.move(self.offset, informations["GROUPS"]["BLOCKS"])

        # attack
        if self.attack_clock.ok(False) and pygame.sprite.collide_rect(self, informations["MAINCHARACTER"]):
            informations["MAINCHARACTER"].attacked(self["ATK"])
            print(f"main charcter attacked by {self['Name']} | HP: {int(informations['MAINCHARACTER']['HP'])}")
            self.attack_clock.reset()

        # Call parent class update
        super().update(informations)