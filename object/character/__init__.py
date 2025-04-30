# -*- coding utf-8 -*-

from collections import namedtuple
from enum import Enum, auto

import pygame

from lib import generate_id
from object import Object
from lib.event import Event

class Character(Object):
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: pygame.surface = None,
                 Name = "npc",
                 MAX_HP = 100.0,
                 HP = 100.0,
                 ATK = 10.0,
                 DEF = 10.0,
                 speed = 10):
        super().__init__(rect=rect, image=image)

        # Character datas
        self.ID = generate_id()
        self.Name = Name
        self.MAX_HP = MAX_HP
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.speed = speed

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
    
    def update(self, groups: dict[str, pygame.sprite.Group], events: list[Event]):
        for event in events:
            key, args = event["type"], event["kwargs"]

            if key == CharacterEvent.ATTACKED:
                self.attacked(args)
            elif key == CharacterEvent.HEAL:
                self.heal(args)
            elif key == CharacterEvent.MOVE:
                self.move(args, groups)
    
    def attacked(self, value):
        self.HP -= value * (1 - self.DEF / (100 + self.DEF))
        self.HP = max(self.HP, 0)
    
    def heal(self, value):
        self.HP += value
        self.HP = min(self.HP, self.MAX_HP)
    
    def move(self, movement, groups: dict[str, pygame.sprite.Group]):
        dx, dy = movement
        # Move and then stop moving whenever being bocked
        for _ in range(self.speed):
            self.rect.move_ip(dx, dy)
            if pygame.sprite.spritecollideany(self, groups["BLOCK"]):
                self.rect.move_ip(-dx, -dy)
                break
    
    Setter = namedtuple("character", ["Name", "MAX_HP", "HP", "ATK", "DEF", "speed"])

class CharacterEvent(Enum):
    '''
    '''
    ATTACKED = auto()
    HEAL = auto()
    MOVE = auto()