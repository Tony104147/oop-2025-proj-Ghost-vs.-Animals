# -*- coding utf-8 -*-

from collections import namedtuple
from enum import Enum, auto

import pygame

from object import Object
from lib.event import Event

class Character(Object):
    ''''''
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: pygame.Surface = None,
                 Name = "npc",
                 MAX_HP = 100.0,
                 HP = 100.0,
                 ATK = 10.0,
                 DEF = 10.0,
                 speed = 3):
        super().__init__(rect=rect, image=image)

        # Character datas
        self.Name = Name
        self.MAX_HP = MAX_HP
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.speed = speed

    # @abstractmethod
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        # Clamp main character into screen
        restriction = informations["CURRENTMAP"].rect
        assert restriction.width >= self.rect.width and restriction.height >= self.rect.height
        self.rect.clamp_ip(restriction)

    def attacked(self, value):
        self.HP -= value * (1 - self.DEF / (100 + self.DEF))
        self.HP = max(self.HP, 0)
    
    def heal(self, value):
        self.HP += value
        self.HP = min(self.HP, self.MAX_HP)
    
    def move(self, offset: tuple[int | float], blocks_group: pygame.sprite.Group, block = True):
        dx, dy = offset
        dx *= self.speed
        dy *= self.speed

        # Move
        self.rect.move_ip(dx, dy)

        # Back to the original position if being blocked
        if block and pygame.sprite.spritecollideany(self, blocks_group):
            self.rect.move_ip(-dx, -dy)


# class CharacterEvent(Enum):
#     '''
#     '''
#     ATTACKED = auto()
#     HEAL = auto()
#     MOVE = auto()