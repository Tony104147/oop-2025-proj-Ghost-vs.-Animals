#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Text:
    def __init__(self,
                 text = '',
                 pos = (0, 0),
                 size = 0,
                 color = (0, 0, 0),
                 font = None):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font = font

    def render(self):
        font = pygame.font.Font(self.font, self.size)
        return font.render(self.text, True, self.color)
