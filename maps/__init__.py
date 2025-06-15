# -*- coding utf-8 -*-

import os
import importlib
from typing import Any, Callable
from attr import dataclass, field

import pygame

from object import Object
from lib.counter import Counter

@dataclass(slots=True, kw_only=True)
class Map:
    '''
    Map class, representing a game map.
    It contains the map's name, size, image, and groups of objects.
    It also contains initialization and update functions.
    '''
    size: tuple[int, int]
    image: str
    groups: dict[str, pygame.sprite.Group] = field(init=False)
    init: Callable[[], None]
    update: Callable[[dict[str, Any]], None]

# Load all maps from the 'maps' directory
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
