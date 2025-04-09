# -*- coding utf-8 -*-

import pygame
from text import Text

class Object:
    do_nothing = (lambda:print('do nothing'))

    def __init__(self, rect, texture):
        self.rect = pygame.Rect(rect)
        self.texture = texture

    def mouse_down_event(self, pos, button):
        pass

    def mouse_up_event(self, pos, button):
        pass

    def mouse_motion_event(self, postions, button, which):
        pass

    def key_down_event(self, key, mod):
        pass

    def key_up_event(self, key, mod):
        pass

    def draw(self, window):
        pass

    def move(self, pos):
        pass

    def update(self):
        pass

class Label(Object):
    def __init__(self, rect, texture, text = Text()):
        super().__init__(rect, texture)
        self.text = text

    def draw(self, window):
        window.blit(self.texture, self.rect.topleft)
        window.blit(self.text.render(), self.rect.move(self.text.pos).topleft)

class Button(Object):
    def __init__(self, rect, textures, callbacks, text = Text()):
        assert len(textures) == 3, 'ERROR: textures must be 3'
        assert len(callbacks) == 5, 'EEROR: callbacks must be 3'
        super().__init__(rect, textures)
        self.texture_index = 0
        self.callbacks = callbacks
        self.text = text

    def mouse_down_event(self, pos, button):
        if self.rect.collidepoint(pos):
            self.texture_index = 2

    def mouse_up_event(self, pos, button):
        if self.rect.collidepoint(pos):
            self.texture_index = 1
            self.callbacks[button - 1]()

    def mouse_motion_event(self, postions, buttons, which):
        if which[1]:
            if buttons[0] or buttons[1] or buttons[2]:
                self.texture_index = 2
            else:
                self.texture_index = 1
        else:
            self.texture_index = 0

    def draw(self, window):
        window.blit(self.texture[self.texture_index], self.rect.topleft)
        window.blit(self.text.render(), self.rect.move(self.text.pos).topleft)

class Box(Object):
    def __init__(self, rect, texture):
        super().__init__(rect, texture)
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def mouse_down_event(self, pos, button):
        box_pos = pos[0] - self.rect.x, pos[1] - self.rect.y
        for obj in self.objects:
            obj.mouse_down_event(box_pos, button)

    def mouse_up_event(self, pos, button):
        box_pos = pos[0] - self.rect.x, pos[1] - self.rect.y
        for obj in self.objects:
            obj.mouse_up_event(box_pos, button)

    def mouse_motion_event(self, postions, button, which):
        begin_pos = postions[0][0] - self.rect.x, postions[0][1] - self.rect.y
        end_pos = postions[1][0] - self.rect.x, postions[1][1] - self.rect.y
        for obj in self.objects:
            begin = obj.rect.collidepoint(begin_pos)
            end = obj.rect.collidepoint(end_pos)
            event = obj.mouse_motion_event((begin_pos, end_pos), button, (begin, end))

    def key_down_event(self, key, mod):
        for obj in self.objects:
            obj.key_down_event(key, mod)

    def key_up_event(self, key, mod):
        for obj in self.objects:
            obj.key_up_event(key, mod)

    def draw(self, window):
        out = self.texture.copy()
        for obj in self.objects:
            obj.draw(out)
        window.blit(out, self.rect.topleft)





