# -*- coding utf-8 -*-

from enum import Enum, unique
from collections import namedtuple

import pygame

Event = namedtuple("Event", ["ID", "type", "func", "kwargs"])

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

def react(event: Event):
    return event.func(event.kwargs)

# class Reactions:
#     ''''''
#     def __init__(self):
#         self.events: dict[Enum, set] = dict()

#     ''''''
#     def add(self, event: Event, action):
#         if event["type"] not in self.events.keys():
#             self.events[event["type"]] = set()
#         self.events[event["type"]].add(action)

#     ''''''
#     def remove(self, event: Event, action):
#         if event["type"] in self.events.keys():
#             self.events[event["type"]].remove(action)
#             # To ignore situation that action not in set, use the following:
#             #
#             # self.events[event["type"]].discard(action)

#     ''''''
#     def clear(self, event: Event):
#         if event["type"] in self.events.keys():
#             self.events[event["type"]].clear()

#     ''''''
#     def react(self, event: Event, **kwargs):
#         for action in self.events.get(event["type"], []):
#             action(**kwargs)