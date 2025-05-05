# -*- coding utf-8 -*-

import pygame

from object import Object
from object.character import Character_base, CharacterEvent
from lib.event import Event
from images import GETIMAGE

class Character(Character_base):
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
    
    def update(self, informations: dict[str, Object | pygame.sprite.Group]):
        key_pressed = pygame.key.get_pressed()

        # Main character moving from keyboard
        for key, direction in self.MOVING_DIRECTION.items():
            if key_pressed[key]:
                self.move(direction, informations["GROUPS"]["BLOCKS"])
        
        # Clamp main character into screen
        restriction = informations["CURRENTMAP"].rect
        assert restriction.width >= self.rect.width and restriction.height >= self.rect.height
        self.rect.clamp_ip(restriction)




