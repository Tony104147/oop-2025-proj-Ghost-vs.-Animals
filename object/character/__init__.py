# -*- coding utf-8 -*-

from collections import namedtuple
from enum import Enum, auto

import pygame

from object import Object

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
        self.values = {
            "Name"   : Name,
            "MAX_HP" : MAX_HP,
            "HP"     : HP,
            "ATK"    : ATK,
            "DEF"    : DEF,
            "speed"  : speed,
        }
    
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    # @abstractmethod
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        # Clamp main character into screen
        restriction = informations["CURRENTMAP"].rect
        assert restriction.width >= self.rect.width and restriction.height >= self.rect.height
        self.rect.clamp_ip(restriction)

    def attacked(self, value):
        self["HP"] = max(self["HP"] - value * (1 - self["DEF"] / (100 + self["DEF"])), 0)
    
    def heal(self, value):
        self["HP"] = min(self["HP"] + value, self["MAX_HP"])
    
    def move(self, offset: tuple[int | float], blocks_group: pygame.sprite.Group = None):
        dx, dy = offset

        # Move
        original_pos = self.rect.topleft
        self.rect.move_ip(dx, dy)

        # Back to the original position if being blocked
        if blocks_group and pygame.sprite.spritecollideany(self, blocks_group):
            self.rect.topleft = original_pos


# class CharacterEvent(Enum):
#     '''
#     '''
#     ATTACKED = auto()
#     HEAL = auto()
#     MOVE = auto()