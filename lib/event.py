# -*- coding utf-8 -*-

from enum import Enum, unique
from collections import namedtuple

import pygame

Event = namedtuple("Event", ["Object_ID", "type", "kwargs"])

@unique
class PygameEvent(Enum):
    '''
    Standard events from "Pygame"
    @
    MOUSEMOTION : pygame.MOUSEMOTION
    MOUSEDOWN   : pygame.MOUSEBUTTONDOWN
    MOUSEUP     : pygame.MOUSEBUTTONUP
    KEYDOWN     : pygame.KEYDOWN
    KEYUP       : pygame.KEYUP
    '''
    MOUSEMOTION = pygame.MOUSEMOTION
    MOUSEDOWN   = pygame.MOUSEBUTTONDOWN
    MOUSEUP     = pygame.MOUSEBUTTONUP
    KEYDOWN     = pygame.KEYDOWN
    KEYUP       = pygame.KEYUP

class Reactions:
    ''''''
    def __init__(self):
        self.events: dict[Enum, set] = dict()

    ''''''
    def add(self, event: Event, action):
        if event.key not in self.events.keys():
            self.events[event.key] = set()
        self.events[event.key].add(action)

    ''''''
    def remove(self, event: Event, action):
        if event.key in self.events.keys():
            self.events[event.key].remove(action)
            # To ignore situation that action not in set, use the following:
            #
            # self.events[event.key].discard(action)

    ''''''
    def clear(self, event: Event):
        if event.key in self.events.keys():
            self.events[event.key].clear()

    ''''''
    def react(self, event: Event, **kwargs):
        for action in self.events.get(event.key, []):
            action(**kwargs)