# -*- coding utf-8 -*-

import os
import importlib
from typing import Any, Callable
from attr import dataclass, field

import pygame

from object import Object
from lib.counter import Counter

# class Map_base(Object):
#     ''''''
#     def __init__(self, *,
#                  size: tuple[int, int] = (0, 0),
#                  image: str = None,
#                  main_character: Object = None):
#         # Call parent class (Box) constructor
#         super().__init__(rect=(0, 0, *size), image=image)
#         self.image = pygame.transform.scale(self.image, self.rect.scale_by(2, 2).size)

#         # object groups
#         self.main_character = pygame.sprite.GroupSingle(main_character)
#         self.enemies = pygame.sprite.Group()
#         self.blocks = pygame.sprite.Group()
#         self.skills = pygame.sprite.Group()
#         self.views = pygame.sprite.Group()
    
#     def get_groups(self):
#         return (self.main_character,
#                 self.enemies,
#                 self.blocks,
#                 self.skills,
#                 self.views)
    
#     def draw(self,  surface: pygame.Surface):
#         # Copy the original image of this box
#         original_image = self.image.copy()

#         # Draw each object onto this box
#         for group in self.get_groups():
#             for obj in group:
#                 obj.draw(self.image)

#         # Draw onto 'surface'
#         super().draw(surface)

#         # Recover the image
#         self.image = original_image

#     def update(self, informations: dict[str]):
#         for group in self.get_groups():
#             for obj in group:
#                 obj.update(informations)


# def get_maps(WINDOW_SIZE, main_character) -> dict[str, Map_base]:
#     MAPS = dict()
#     maps = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../maps")
#     for file in os.listdir(maps):
#         if not file.endswith(".py"):
#             continue
#         if file.startswith("__"):
#             continue

#         module_name = file.replace(".py", "")
#         map_module = importlib.import_module("." + module_name, "maps").Map
#         assert issubclass(map_module, Map_base)

#         name = module_name.replace("_", " ")
#         MAPS[name] = map_module(WINDOW_SIZE, main_character)
    
#     return MAPS

@dataclass(slots=True, kw_only=True)
class Map:
    size: tuple[int, int]
    image: str
    groups: dict[str, pygame.sprite.Group] = field(init=False)
    init: Callable[[], None]
    update: Callable[[dict[str, Any]], None]

def load_maps() -> dict[str, Map]:
    MAPS = dict()
    map_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../maps")
    for file in os.listdir(map_files):
        if (not file.endswith(".py")) or file.startswith("__"):
            continue
        
        map_name = file.replace('.py', '')
        map = importlib.import_module('.' + map_name, 'maps').MAP
        assert isinstance(map, Map)

        MAPS[map_name] = map
    
    return MAPS