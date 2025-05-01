# -*- coding utf-8 -*-

import pygame

from character import ABCCharacter, Setter, CharacterEvent
from lib.event import Event

main_character_setter = Setter(
    rect = (0, 0, 0, 0),
    image = None,
    Name = "main character",
    MAX_HP = 100.0,
    HP = 100.0,
    ATK = 10.0,
    DEF = 10.0,
    speed = 10,
)

class Character(ABCCharacter):
    ''''''
    def __init__(self):
        super().__init__(main_character_setter)

        event_move_up    = Event(ID= self.ID, type= CharacterEvent.MOVE, func= self.move, kwargs= {"movement" : (0, -1)})
        event_move_down  = Event(ID= self.ID, type= CharacterEvent.MOVE, func= self.move, kwargs= {"movement" : (0, 1)})
        event_move_left  = Event(ID= self.ID, type= CharacterEvent.MOVE, func= self.move, kwargs= {"movement" : (-1, 0)})
        event_move_right = Event(ID= self.ID, type= CharacterEvent.MOVE, func= self.move, kwargs= {"movement" : (1, 0)})

        self.KEY_MOVE_EVENT_LIST = {
            pygame.K_w : event_move_up,
            pygame.K_a : event_move_left,
            pygame.K_s : event_move_down,
            pygame.K_d : event_move_right,
        }

    ''''''
    def update(self, groups: dict[str, pygame.sprite.Group], events: list[Event]):
        super().update(groups, events)




