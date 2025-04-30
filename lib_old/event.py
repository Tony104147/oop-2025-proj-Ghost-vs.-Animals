# -*- coding utf-8 -*-

from enum import Enum, unique

import pygame

class Event:
    event_ids = [
        pygame.MOUSEMOTION,
        pygame.MOUSEBUTTONUP,
        pygame.MOUSEBUTTONDOWN,
        pygame.KEYUP,
        pygame.KEYDOWN
    ]

    def __init__(self):
        self.events = {}
    
        for event_id in Event.event_ids:
            self.events[event_id] = set()

    def add(self, event_id, action):
        self.events[event_id].add(action)

    def remove(self, event_id, action):
        self.events[event_id].remove(action)

    def clear(self, event_id):
        self.events[event_id].clear()

    def react(self, event_id, args):
        if event_id is None: return
        for action in self.events[event_id]:
            action(*args)

