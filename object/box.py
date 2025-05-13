# -*- coding utf-8 -*-

import pygame

from object import Object

class Box(Object):
    ''''''
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: pygame.Surface = None):
        # Call the parent class (Object) constructor
        super().__init__(rect=rect, image=image)

        # Initialize the size of image
        self.image = pygame.transform.scale(self.image, self.rect.size)

        # Objects in this box
        self.objects = pygame.sprite.Group()

    ''''''
    def add(self, obj: Object | list[Object] | pygame.sprite.Group):
        self.objects.add(obj)

    ''''''
    def remove(self, obj: Object | list[Object] | pygame.sprite.Group):
        self.objects.remove(obj)

    ''''''
    def draw(self, surface: pygame.Surface):
        # Copy the original image of this box
        original_image = self.image.copy()

        # Draw each object onto this box
        for obj in self.objects:
            obj.draw(self.image)

        # Draw onto 'surface'
        super().draw(surface)

        # Recover the image
        self.image = original_image

    ''''''
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        for obj in self.objects:
            obj.update(informations)