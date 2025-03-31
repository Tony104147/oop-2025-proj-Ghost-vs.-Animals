#!usr/bin/env python3.10
# -*- coding utf-8 -*-

import pygame
from text import Text

class Object:
    def __init__(self, rect, texture):
        self.rect = pygame.Rect(rect)
        self.texture = texture

    def mouse_release_event(self):
        pass

    def mouse_hold_event(self):
        pass

    def click_event(self):
        pass

    def draw(self, window):
        pass

    def update(self):
        pass

    def move(self, pos):
        pass

class Button(Object):
    def __init__(self, rect, textures, callback, text = Text()):
        assert len(textures) == 3, 'ERROR: textures of Button must be 3'
        super().__init__(rect, textures[0])
        self._textures = textures
        self._callback = callback
        self.text = text

    def mouse_release_event(self):
        self.texture = self._textures[1]

    def mouse_hold_event(self):
        self.texture = self._textures[2]

    def click_event(self):
        self._callback()

    def draw(self, window):
        # draw texture
        window.blit(self.texture, self.rect.topleft)

        # draw text
        window.blit(self.text.render(), self.rect.move(self.text.pos).topleft)
        
        # reset texture
        self.texture = self._textures[0]

    def move(self, pos):
        self.rect.topleft = pos

class Label(Object):
    def __init__(self, rect, texture, text = Text()):
        super().__init__(rect, texture)
        self.text = text

    def draw(self, window):
        # draw texture
        window.blit(self.texture, self.rect.topleft)

        # draw text
        window.blit(self.text.render(), self.rect.move(self.text.pos).topleft)

    def update(self):
        pass

    def move(self, pos):
        self.rect.topleft = pos





