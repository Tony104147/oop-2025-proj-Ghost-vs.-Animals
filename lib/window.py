#!usr/bin/env python3.10
# -*- coding utf-8 -*-

import pygame
import os

class Window:
    def __init__(self,
                 size,
                 title = '',
                 flags = 0):
        pygame.init()
        self._window = pygame.display.set_mode(size, flags)
        self._screens = [self._Screen()]
        self._objects = pygame.sprite.Group()
        self._flags = flags
        self.title = title

    def get_size(self):
        return self._window.get_size()

    def _get_screen(self,
                    screen_id):
        return self._screens[screen_id]

    def _get_screen_bg(self,
                       screen_id):
        return self._get_screen(screen_id).bg_on_show

    def set_screen_rect(self,
                        screen_id,
                        rect):
        if rect is not None:
            assert len(rect) == 4, 'ERROR: invalid rect'
            rect = pygame.Rect(rect)
        self._get_screen(screen_id).rect = rect

    def add_screen(self,
                   background_images = [],
                   background_color = (0, 0, 0))-> int:
        self._screens.append(self._Screen(background_color, background_images))
        return len(self._screens) - 1

    def add_screen_bg(self,
                      screen_id,
                      image)-> None:
        return self._get_screen(screen_id).add_image(image)

    def switch_screen_bg(self,
                         screen_id,
                         background_id):
        assert 0 <= screen_id < len(self._screens), 'ERROR: invalid screen_id'
        screen = self._get_screen(screen_id)
        assert 0 <= background_id < len(screen.bgs), 'ERROR: invalid background_id'
        screen.bg_on_show = background_id

    def resize(self,
               size):
        old_window = self._window
        self._window = pygame.display.set_mode(size, self._flags)
        self._window.blit(pygame.transform.scale(old_window, size), (0, 0))
        del old_window

    def draw_screen(self,
                    screen_id = 0):
        screen = self._get_screen(screen_id)
        if screen.rect == None:
            rect = self._window.get_rect()
        else:
            rect = screen.rect
        bg = pygame.transform.scale(screen.get_bg(), rect.size)
        self._window.blit(bg, rect.topleft)

    def update(self):
        pygame.display.update()

    class _Screen:
        def __init__(self,
                     background_color = (0, 0, 0),
                     background_images = []):
            default_bg = pygame.Surface((1, 1))
            default_bg.fill(background_color)
            self.bgs = [default_bg]
            self.bg_on_show = 0
            self.rect = None
            for image in background_images:
                self.add_image(image)

        def add_image(self,
                      image)-> None:
            self.bgs.append(pygame.image.load(image).convert())
            return len(self.bgs) - 1

        def get_bg(self):
            return self.bgs[self.bg_on_show]
