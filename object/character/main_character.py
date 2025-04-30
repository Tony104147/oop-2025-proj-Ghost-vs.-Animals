# -*- coding utf-8 -*-

import pygame

from character import Character
from lib.event import Reactions, PygameEvent, Event

main_character_setter = Character.Setter(
    rect = (0, 0, 0, 0),
    image = None,
    Name = "main character",
    MAX_HP = 100.0,
    HP = 100.0,
    ATK = 10.0,
    DEF = 10.0,
    speed = 10,
)

class Main_character(Character):
    ''''''
    def __init__(self):
        super().__init__(main_character_setter)

    ''''''
    def update(self, groups: dict[str, pygame.sprite.Group], events: list[Event]):
        super().update(groups, events)




