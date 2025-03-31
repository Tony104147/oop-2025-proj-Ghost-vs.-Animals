#!usr/bin/env python3.10
# -*- coding utf-8 -*-

import pygame
from objects import Object

class Window:
    def __init__(self,
                 size,
                 fps = 30,
                 title = '',
                 flags = 0):
        pygame.init()
        self._window = pygame.display.set_mode(size, flags)
        pygame.display.set_caption(title)

        # const vars
        self.DEFAULT_BACKGROUND = pygame.Surface(size)

        # vars
        self._fps = fps
        self._clock = pygame.time.Clock()
        self._screen = Window.Screen(self.DEFAULT_BACKGROUND)

        # flags
        self._running = True
        self._mouse_hold = False

    def set_fps(self, fps):
        self._fps = fps

    def set_screen(self, screen):
        self._screen = screen

    def _mouse_button_down(self):
        self._mouse_hold = True

    def _mouse_button_up(self, pos):
        if self._mouse_hold:
            self._mouse_hold = False
            self._screen.click_event(pos)

    def running(self):
        return self._running

    def event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_button_down()
            elif event.type == pygame.MOUSEBUTTONUP:
                self._mouse_button_up(event.pos)
            elif event.type == pygame.KEYDOWN:
                pass
            elif event.type == pygame.KEYDOWN:
                pass

    def update(self):
        if self._mouse_hold:
            self._screen.mouse_hold_event()
        else:
            self._screen.mouse_release_event()
        self._screen.draw(self._window)
        self._clock.tick_busy_loop(self._fps)
        pygame.display.flip()
        if not self._running:
            pygame.quit()

    # This class is for handling screen objects
    class Screen:
        def __init__(self, background):
            self._bg = background
            self._objects = []
        
        def add_object(self, obj):
            self._objects.append(obj)

        def remove_object(self, obj):
            self._objects.remove(obj)

        def set_background(self, background):
            self._bg = background

        def draw(self, window):
            bg = pygame.transform.scale(self._bg, window.get_size())
            window.blit(bg, (0, 0))
            for obj in self._objects:
                obj.draw(window)

        def mouse_release_event(self):
            pos = pygame.mouse.get_pos()
            for obj in self._objects:
                if obj.rect.collidepoint(pos):
                    obj.mouse_release_event()

        def mouse_hold_event(self):
            pos = pygame.mouse.get_pos()
            for obj in self._objects:
                if obj.rect.collidepoint(pos):
                    obj.mouse_hold_event()

        def click_event(self, pos):
            for obj in self._objects:
                if obj.rect.collidepoint(pos):
                    event = obj.click_event()
                    break

        def update(self):
            for obj in self._objects:
                obj.update()
