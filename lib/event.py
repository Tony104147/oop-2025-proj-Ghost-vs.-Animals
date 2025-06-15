# -*- coding utf-8 -*-

import pygame

# Event management module for custom events in Pygame
def new(name: str):
    if name not in TYPES.keys():
        TYPES[name] = pygame.event.custom_type()
        return True
    return False

# Post a custom event with the given name and optional keyword arguments
def post(name: str, kwargs: dict = {}):
    if name in TYPES.keys():
        pygame.event.post(pygame.event.Event(TYPES[name], kwargs))
        return True
    return False

# Dictionary to hold custom event types
TYPES: dict[str, int] = dict()
