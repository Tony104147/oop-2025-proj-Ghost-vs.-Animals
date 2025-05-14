# -*- coding utf-8 -*-

from collections import namedtuple
import os
import importlib

import pygame

from object import Object

class Map_base(Object):
    ''''''
    def __init__(self, *,
                 window_size: tuple[int, int] = (0, 0),
                 image: pygame.Surface = None,
                 main_character: Object = None):
        # Default background is black
        if image is None: image = pygame.Surface(window_size)

        # Call parent class (Box) constructor
        super().__init__(rect=(0, 0, *window_size), image=image)
        self.image = pygame.transform.scale(self.image, self.rect.scale_by(2, 2).size)

        # object groups
        self.main_character = pygame.sprite.GroupSingle(main_character)
        self.enemies = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.skills = pygame.sprite.Group()
        self.views = pygame.sprite.Group()
    
    def get_groups(self):
        return (self.main_character,
                self.enemies,
                self.blocks,
                self.skills,
                self.views)
    
    def draw(self,  surface: pygame.Surface):
        # Copy the original image of this box
        original_image = self.image.copy()

        # Draw each object onto this box
        for group in self.get_groups():
            for obj in group:
                obj.draw(self.image)

        # Draw onto 'surface'
        super().draw(surface)

        # Recover the image
        self.image = original_image

    def update(self, informations: dict[str]):
        for group in self.get_groups():
            for obj in group:
                obj.update(informations)


def get_maps(WINDOW_SIZE, main_character) -> dict[str, Map_base]:
    MAPS = dict()
    maps = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../maps")
    for file in os.listdir(maps):
        if not file.endswith(".py"):
            continue
        if file.startswith("__"):
            continue

        module_name = file.replace(".py", "")
        map_module = importlib.import_module("." + module_name, "maps").Map
        assert issubclass(map_module, Map_base)

        name = module_name.replace("_", " ")
        MAPS[name] = map_module(WINDOW_SIZE, main_character)
    
    return MAPS