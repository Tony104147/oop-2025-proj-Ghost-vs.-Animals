#!usr/bin/env python3.10
# -*- coding: utf-8 -*-

import pygame

class Circle:
    def __init__(self, screen, x, y, radius, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self, x, y):
        self.x = x
        self.y = y

    def resize(self, radius):
        self.radius = radius

    def set_color(self, color):
        self.color = color

class Circle_hollow(Circle):
    def __init__(self, screen, x, y, radius, color, thickness):
        super().__init__(screen, x, y, radius, color)
        self.thickness = thickness

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, self.thickness)

    def move(self, x, y):
        super().move(x, y)

    def resize(self, radius):
        super().resize(radius)

    def set_color(self, color):
        super().set_color(color)
