# -*- coding utf-8 -*-

from collections import namedtuple
from enum import Enum, auto

import pygame

from lib import generate_id
from lib.object import Object

class Character(Object):
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: pygame.surface = None,
                 Name = "npc",
                 MAX_HP = 100.0,
                 HP = 100.0,
                 ATK = 10.0,
                 DEF = 10.0):
        super().__init__(rect=rect, image=image)

        # Character datas
        self.ID = generate_id()
        self.Name = Name
        self.MAX_HP = MAX_HP
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
    
    def attacked(self, damage):
        self.HP -= max(damage * (1 - self.DEF / (100 + self.DEF)), 0)
    
    Setter = namedtuple("character", ["Name", "MAX_HP", "HP", "ATK", "DEF"])

class CharacterEvent(Enum):
    '''
    '''
    ATTACKED = auto()
    BLOCKED = auto()