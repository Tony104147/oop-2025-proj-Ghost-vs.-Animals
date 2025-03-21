#!usr/lib/env python3.10
# -*- coding: utf-8 -*-

import pygame
import numpy as np

class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        pass

    def move(self, dx = 0, dy = 0):
        pass

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

class Rectangle(Shape):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

class Triangle(Shape):
    def __init__(self, color, points):
        super().__init__(np.average(points[:][0]), np.average(points[:][1]), color)
        self.points = points

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.points)

    def move(self, dx = 0, dy = 0):
        for point in self.points:
            point[0] += dx
            point[1] += dy
