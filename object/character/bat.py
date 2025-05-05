# -*- coding utf-8 -*-

import random
import numpy as np

import pygame

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
                         speed=5)
        
        self.move_count = 0
        self.direction = [0, 0]
        
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        # Move
        if self.move_count == 0:
            x, y = informations["MAINCHARACTER"].rect.topleft
            radius = 150
            dx = random.uniform(x - radius, x + radius) - self.rect.x
            dy = random.uniform(y - radius, y + radius) - self.rect.y
            self.direction[0] = np.sign(dx)
            self.direction[1] = np.sign(dy)
            self.move_count = random.randint(10, 30)
        self.move_count -= 1
        self.move(self.direction, informations["GROUPS"]["BLOCKS"])

        # Call parent class update
        super().update(informations)