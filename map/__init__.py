# -*- coding utf-8 -*-

import pygame

from object.box import Box
from lib.event import Event, react

from object.character import main_character

class Map(Box):
    def __init__(self, rect, image):
        super().__init__(rect=rect, image=image)

        self.main_character = main_character.Character()

    def update(self, groups: dict[str, pygame.sprite.Group], events: list[Event]):
        key_pressed = pygame.key.get_pressed()

        # main character
        for key, event in self.main_character.KEY_MOVE_EVENT_LIST:
            if key_pressed[key]:
                react(event)
                events.append(event)

        super().update(groups, events)

    