#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Surface:
    def __init__(self, rect,
                 bg_image = None):
        rect = pygame.Rect(rect)
        self.pos = rect.topleft
        self._surface = pygame.Surface(rect.size)
        self.subsurfaces = []
        self._image = bg_image

    def add_subsurface(self, rect,
                       bg_image = None):
        subsurface = Surface(rect, bg_image)
        self.subsurfaces.append(subsurface)
        return subsurface

    def set_image(self, image):
        self._image = image

    def _draw(self, window, dx_dy = (0, 0)):
        rect = self._surface.rect
        if self._image is not None:
            bg = pygame.transform.scale(self._image, rect.size)
            window.blit(bg, rect.move(dx_dy))
        for subsurface in self.subsurfaces:
            subsurface._draw(window, rect.topleft)

    def draw(self, window):
        self._draw(window)

    def move(self, dx_dy):
        self.rect.move_ip(dx_dy)
        for subsurface in self.subsurfaces:
            subsurface.move(dx_dy)

    def resize(self, size):
        ratio = (size[0]/self._surface.get_width(),
                 size[1]/self._surface.get_height())
        self.rect.size = size
        for subsurface in self.subsurfaces:
            subsurface.resize((subsurface.rect.width*ratio[0],
                               subsurface.rect.height*ratio[1]))

    def set_rect(self, rect):
