# -*- coding utf-8 -*-

import random

import pygame

from maps import Map_base
from images import GETIMAGE
from object.character import bat, frog


class Map(Map_base):
    ''''''
    def __init__(self, window_size):
        super().__init__(window_size=window_size, image=GETIMAGE("forest"))

        def randpos(x_range, y_range):
            x = random.randint(0, x_range)
            y = random.randint(0, y_range)
            return (x, y)
        
        restriction = self.image.get_rect()

        bat1 = bat.Bat(randpos(*restriction.size))
        bat2 = bat.Bat(randpos(*restriction.size))
        frog1 = frog.Frog(randpos(*restriction.size))

        bat1.restriction = restriction
        bat2.restriction = restriction
        frog1.restriction = restriction

        self.enemies.add(bat1)
        self.enemies.add(bat2)
        self.enemies.add(frog1)

        for groups in [self.enemies, self.blocks]:
            for obj in groups:
                self.objects.add(obj)