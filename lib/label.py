#!usr/bin/env python3.10
# -*- coding: utf-8 -*-

import pygame
from square import Square

class Label(Square):
    def __init__(self, x, y,
                 font_size, text = None, font_color = (0, 0, 0),
                 backgroud_color = None):
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.font_color = font_color
        width, height = self.font.size(text)
        super().__init__(x, y, width, height, backgroud_color)

    def draw(self, screen):
        if self.color:
            super().draw(screen)
        if self.text:
            text = self.font.render(self.text, True, self.font_color)
            screen.blit(text, (self.x, self.y))

    def move(self, x, y):
        super().move(x, y)

    def __set_size(self):
        super().resize(self.font.size(self.text))

    def set_backgroud_color(self, color):
        super().set_color(color)

    def set_text(self, text):
        self.text = text
        self.__set_size()

    def set_font_color(self, color):
        self.font_color = color

    def set_font_size(self, size):
        self.font = pygame.font.Font(None, size)
        self.__set_size()
