# -*- coding utf-8 -*-

from collections import namedtuple
import os
import importlib

import pygame

from object.box import Box

class Map_base(Box):
    ''''''
    def __init__(self, *,
                 window_size = (0, 0),
                 image: pygame.Surface = None):
        assert window_size[0] > 0 and window_size[1] > 0

        # Default background is black
        if image is None: image = pygame.Surface(window_size)

        # Call parent class (Box) constructor
        super().__init__(rect=(0, 0, *window_size), image=image)

        self.enemies = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
    
    def update(self, informations: dict[str]):
        return super().update(informations)


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
        MAPS[name] = map_module(WINDOW_SIZE)
        MAPS[name].add(main_character)
    
    return MAPS