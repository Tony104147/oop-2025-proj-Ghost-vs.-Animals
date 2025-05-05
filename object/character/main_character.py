# -*- coding utf-8 -*-

import pygame

from lib.counter import Counter
from object import Object
from object.character import Character
from images import GETIMAGE

class Main_character(Character):
    ''''''
    def __init__(self):
        super().__init__(rect=(100, 100, 50, 50),
                         image=GETIMAGE("ghost"),
                         Name="main character",
                         MAX_HP=100.0,
                         HP=100.0,
                         ATK=10.0,
                         DEF=10.0,
                         speed=5)

        self.MOVING_DIRECTION = {
            pygame.K_w : (0, -1),
            pygame.K_a : (-1, 0),
            pygame.K_s : (0, 1),
            pygame.K_d : (1, 0),
        }

        self.attacked_clock = Counter(120)
        self.heal_clock = Counter(240)
    
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        key_pressed = pygame.key.get_pressed()

        # Main character moving from keyboard
        for key, direction in self.MOVING_DIRECTION.items():
            if key_pressed[key]:
                self.move(direction, informations["GROUPS"]["BLOCKS"])
        
        if self.attacked_clock.ok(False):
            enemy_collide = pygame.sprite.spritecollideany(self, informations["GROUPS"]["ENEMIES"])
            if enemy_collide:
                self.attacked(enemy_collide.ATK)
                print(f"HP: {int(self.HP)}")
                self.attacked_clock.reset()
        
        if self.HP == 0:
            self.HP = self.MAX_HP
            print("Dead!!!")
        
        if self.heal_clock.ok():
            self.heal(5)
            print(f"HP: {int(self.HP)}")
        
        # Call parent class update
        super().update(informations)
