# -*- coding utf-8 -*-

import pygame

def new(name: str):
    if name not in TYPES.keys():
        TYPES[name] = pygame.event.custom_type()
        return True
    return False

def post(name: str, kwargs: dict = {}):
    if name in TYPES.keys():
        pygame.event.post(pygame.event.Event(TYPES[name], kwargs))
        return True
    return False


TYPES: dict[str, int] = dict()