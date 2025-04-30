# -*- coding utf-8 -*-

from enum import Enum, unique

import pygame

class Event(Enum):
    '''
    Enumerate event classes
    '''
    pass

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
        self.events: dict[Event, set] = dict()

    ''''''
    def add(self, event_id: Event, action):
        if event_id not in self.events.keys():
            self.events[event_id] = set()
        self.events[event_id].add(action)

    ''''''
    def remove(self, event_id: Event, action):
        if event_id in self.events.keys():
            self.events[event_id].remove(action)
            # To ignore situation that action not in set, use the following:
            #
            # self.events[event_id].discard(action)

    ''''''
    def clear(self, event_id: Event):
        if event_id in self.events.keys():
            self.events[event_id].clear()

    ''''''
    def react(self, event_id: Event, **kwargs):
        for action in self.events.get(event_id, []):
            action(**kwargs)