#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class KEYBOARD_FLAGS:
    def get(self):
        return pygame.key.get_pressed()

    def __getitem__(self, key):
        return self.get()[key]
