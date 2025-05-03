# -*- coding utf-8 -*-

import pygame

from maps import Map_base
from images import GETIMAGE



class Map(Map_base):
    ''''''
    def __init__(self, window_size):
        super().__init__(window_size=window_size, image=GETIMAGE("forest"))