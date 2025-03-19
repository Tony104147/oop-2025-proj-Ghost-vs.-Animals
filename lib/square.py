import pygame

class Square:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, x, y):
        self.x = x
        self.y = y


class Square_hollow(Square):
    def __init__(self, x, y, width, height, color, thickness):
        super().__init__(x, y, width, height, color)
        self.thickness = thickness

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.thickness)

    def move(self, x, y):
        super().move(x, y)
