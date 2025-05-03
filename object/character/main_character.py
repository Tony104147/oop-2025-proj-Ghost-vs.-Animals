# -*- coding utf-8 -*-

import pygame

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

        # event_key_move_up    = Event(ID=self.ID, type=CharacterEvent.MOVE, func=self.move, kwargs={"movement" : (0, -1)})
        # event_key_move_down  = Event(ID=self.ID, type=CharacterEvent.MOVE, func=self.move, kwargs={"movement" : (0, 1)})
        # event_key_move_left  = Event(ID=self.ID, type=CharacterEvent.MOVE, func=self.move, kwargs={"movement" : (-1, 0)})
        # event_key_move_right = Event(ID=self.ID, type=CharacterEvent.MOVE, func=self.move, kwargs={"movement" : (1, 0)})

        # self.KEY_MOVE_EVENT_LIST = {
        #     pygame.K_w : event_key_move_up,
        #     pygame.K_a : event_key_move_left,
        #     pygame.K_s : event_key_move_down,
        #     pygame.K_d : event_key_move_right,
        # }

        self.MOVING_DIRECTION = {
            pygame.K_w : (0, -1),
            pygame.K_a : (-1, 0),
            pygame.K_s : (0, 1),
            pygame.K_d : (1, 0),
        }
    
    def move(self, movement: tuple[int | float], blocks_group: pygame.sprite.Group, restriction: pygame.rect.Rect):
        super().move(movement, blocks_group)
        assert restriction.width >= self.rect.width and restriction.height >= self.rect.height
        self.rect.clamp_ip(restriction)
    
    def update(self, groups: dict[str, pygame.sprite.Group]):
        pass




