# -*- coding utf-8 -*-

import pygame

from object import Object

class Skill(Object):
    ''''''
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: str = '',
                 Name = "skill",
                 damage = 0.0,
                 direction = 0.0,
                 speed = 5,
                 tags = 0):
        super().__init__(rect=rect, image=image)

        # Skill datas
        self.Name = Name
        self.damage = damage
        self.direction = direction
        self.speed = speed
        self.tags = tags