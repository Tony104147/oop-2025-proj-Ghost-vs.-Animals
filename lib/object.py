# -*- coding utf-8 -*-

from abc import ABC, abstractmethod

import pygame

class Object(ABC, pygame.sprite.Sprite):
    ''''''
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: pygame.Surface = None):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Rectangle recording the size and position of this object
        self.rect = pygame.Rect(rect)

        # Texture of this object. Invisible if the argument is not setted
        if image:
            self.image = image
        else:
            self.image = pygame.Surface(self.rect.size).convert_alpha()
            self.image.fill((0, 0, 0, 0))

    ''''''
    @abstractmethod
    def draw(self, surface: pygame.Surface):
        if self.image:
            # # Reacle the image with unchanged ratio
            # self_ratio = self.rect.height / self.rect.width
            # image_ratio = self.image.get_height() / self.image.get_width()
            # if self_ratio > image_ratio:
            #     image = pygame.transform.scale_by(self.image, self.rect.width / self.image.get_width())
            # else:
            #     image = pygame.transform.scale_by(self.image, self.rect.height / self.image.get_height())

            # Rescale the image to fit the size of object
            image = pygame.transform.scale(self.image, self.rect.size)

            # Draw image onto 'surface'
            surface.blit(image, self.rect.topleft)

    ''''''
    def update(self):
        pass
