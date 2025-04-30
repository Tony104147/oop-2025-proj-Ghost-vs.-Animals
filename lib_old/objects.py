# -*- coding utf-8 -*-

import pygame
from text import Text
from event import Event

class Object:
    do_nothing = (lambda:print('do nothing'))

    def __init__(self, rect = (0, 0, 0, 0)):
        self.rect = pygame.Rect(rect)
        self.texture = pygame.Surface(self.rect.size)
        self.text = Text()
        self.event = Event()

    def mouse_down_event(self, pos, button):
        pass

    def mouse_up_event(self, pos, button):
        pass

    def mouse_motion_event(self, postions, button, which):
        pass

    def draw(self, window):
        window.blit(self.texture, self.rect.topleft)

    def move(self, dx, dy):
        pass

    def update(self):
        pass

class Label(Object):
    def __init__(self, rect):
        super().__init__(rect)
        self.text = Text()

    def draw(self, window):
        window.blit(self.texture, self.rect.topleft)
        window.blit(self.text.render(), self.rect.move(self.text.pos).topleft)

class Button(Object):
    def __init__(self, rect):
        super().__init__(rect)

        self.callbacks = [Object.do_nothing]*5
        self.texture_index = 0

        self.event.add(pygame.MOUSEBUTTONDOWN, self.mouse_down_event)
        self.event.add(pygame.MOUSEBUTTONUP,   self.mouse_up_event)
        self.event.add(pygame.MOUSEMOTION,     self.mouse_motion_event)

    def mouse_down_event(self, pos, button):
        if self.rect.collidepoint(pos):
            self.texture_index = 2

    def mouse_up_event(self, pos, button):
        if self.rect.collidepoint(pos):
            self.texture_index = 1
            self.callbacks[button - 1]()

    def mouse_motion_event(self, pos, rel, buttons):
        end_pos = pos[0] + rel[0], pos[1] + rel[1]
        if self.rect.collidepoint(end_pos):
            if buttons[0]:
                self.texture_index = 2
            else:
                self.texture_index = 1
        else:
            self.texture_index = 0

    def draw(self, window):
        texture = pygame.transform.scale(self.texture[self.texture_index], self.rect.size)
        window.blit(texture, self.rect.topleft)
        window.blit(self.text.render(), self.rect.move(self.text.pos).topleft)

class Box(Object):
    def __init__(self, rect):
        super().__init__(rect)

        self.objects = []

        self.event.add(pygame.MOUSEBUTTONDOWN, self.mouse_down_event)
        self.event.add(pygame.MOUSEBUTTONUP,   self.mouse_up_event)
        self.event.add(pygame.MOUSEMOTION,     self.mouse_motion_event)
        self.event.add(pygame.KEYDOWN,         self.key_down_event)
        self.event.add(pygame.KEYUP,           self.key_up_event)

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def mouse_down_event(self, pos, button):
        box_pos = pos[0] - self.rect.x, pos[1] - self.rect.y
        for obj in self.objects:
            obj.event.react(pygame.MOUSEBUTTONDOWN, (box_pos, button))

    def mouse_up_event(self, pos, button):
        box_pos = pos[0] - self.rect.x, pos[1] - self.rect.y
        for obj in self.objects:
            obj.event.react(pygame.MOUSEBUTTONUP, (box_pos, button))

    def mouse_motion_event(self, pos, rel, buttons):
        box_pos = pos[0] - self.rect.x, pos[1] - self.rect.y
        for obj in self.objects:
            obj.event.react(pygame.MOUSEMOTION, (box_pos, rel, buttons))

    def key_down_event(self, key, mod):
        for obj in self.objects:
            obj.event.react(pygame.KEYDOWN, (key, mod))

    def key_up_event(self, key, mod):
        for obj in self.objects:
            obj.event.react(pygame.KEYUP, (key, mod))

    def draw(self, window):
        out = self.texture.copy()
        for obj in self.objects:
            obj.draw(out)
        window.blit(out, self.rect.topleft)

    def update(self):
        for obj in self.objects:
            obj.update()

class Entity(Object):
    def __init__(self, rect):
        super().__init__(rect)

        self.hit_box = pygame.Rect((0, 0, *self.rect.size))
        self.tag = Entity.Tag()

    def get_hit_rect(self):
        return self.hit_box.move(self.rect.topleft)

    def collide(self, entity):
        hit_rect_1 = self.get_hit_rect()
        hit_rect_2 = entity.get_hit_rect()
        return hit_rect_1.colliderect(hit_rect_2)

    def collidelist(self, entities):
        for entity in entities:
            if self.collide(entity):
                return True
        return False
    
    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    class Tag:
        FRIENDLY    = 0b1
        PROJECTILE  = 0b10
        BREAKABLE   = 0b100
        BLOCKING    = 0b1000

        def __init__(self, tag = 0):
            self.data = tag

        def fit(self, tag):
            return (self.data & tag) == tag









