#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class KeyBoard:
    def __init__(self):
        self.key_callbacks = {}

    def add_callback(self, callback, key, mods = None, on = True):
        self.key_callbacks.setdefault(key, []).append((callback, mods, on))
        return len(self.key_callbacks[key]) - 1

    def key_press(self, key, mod):
        for callback, mods, on in self.key_callbacks.get(key, []):
            if on and ((not mods) or (mod in mods)):
                callback()

    def get_pressed():
        return pygame.key.get_pressed()

    def get_mods():
        return pygame.key.get_mods()
        
