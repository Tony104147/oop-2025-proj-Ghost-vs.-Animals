# -*- coding utf-8 -*-

import random

from numpy import dtype
import pygame

from lib.counter import Counter
from maps import Map_base
from images import GETIMAGE
from object import Object
from object.character import bat, frog


class Map(Map_base):
    ''''''
    def __init__(self, window_size, main_character):
        super().__init__(window_size=window_size, image=GETIMAGE("forest"), main_character=main_character)
        
        restriction = self.image.get_rect()

        bat1 = bat.Bat(Map.randpos(*restriction.size))
        bat2 = bat.Bat(Map.randpos(*restriction.size))
        frog1 = frog.Frog(Map.randpos(*restriction.size))

        bat1.restriction = restriction
        bat2.restriction = restriction
        frog1.restriction = restriction

        self.enemies.add(bat1)
        self.enemies.add(bat2)
        self.enemies.add(frog1)

        # Respawn counter of monsters
        self.respawn_counter = {
            bat.Bat   : Counter(600),
            frog.Frog : Counter(1200),
        }
        self.respawn_set = {
            bat.Bat   : 0,
            frog.Frog : 0,
        }
    
    def dead(self, monster):
        monster_type = type(monster)
        if not self.respawn_set[monster_type]:
            self.respawn_counter[monster_type].reset()
        self.respawn_set[monster_type] += 1
    
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        super().update(informations)

        for enemy in self.enemies:
            if enemy['HP'] == 0:
                print(f"{enemy['Name']} dead!!!")
                enemy.kill()
                self.dead(enemy)
        
        for monster_type, number in self.respawn_set.items():
            if number and self.respawn_counter[monster_type].ok():
                self.respawn_set[monster_type] -= 1
                monster = monster_type(Map.randpos(*self.image.get_size()))
                monster.restriction = self.image.get_rect()
                self.enemies.add(monster)

    def randpos(x_range, y_range):
        x = random.randint(0, x_range)
        y = random.randint(0, y_range)
        return (x, y)