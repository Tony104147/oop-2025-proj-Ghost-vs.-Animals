#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Text:
    LEFT         = 0b0001
    RIGHT        = 0b0010
    TOP          = 0b0100
    BOTTOM       = 0b1000
    TOP_LEFT     = 0b0101
    TOP_RIGHT    = 0b0110
    BOTTOM_LEFT  = 0b1001
    BOTTOM_RIGHT = 0b1010
    H_CENTER     = 0b0011
    V_CENTER     = 0b1100
    CENTER       = 0b0000

    def __init__(self,
                 text = '',
                 size = 0,
                 color = (0, 0, 0),
                 font = None,
                 pos = (0, 0)):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font = font

    def render(self):
        font = pygame.font.Font(self.font, self.size)
        return font.render(self.text, True, self.color)

    def typeset(self, area, margin = 0):
        font = pygame.font.Font(self.font, self.size)
        w, h = font.size(self.text)
        w = (area[0] - w) / 2.0
        h = (area[1] - h) / 2.0
        x, y = w, h
        if margin & Text.LEFT:
            x -= w
        if margin & Text.RIGHT:
            x += w
        if margin & Text.TOP:
            y -= h
        if margin & Text.BOTTOM:
            y += h
        self.pos = (round(x), round(y))
