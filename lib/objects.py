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

    def draw(self, window):
        pass

    def move(self, dx, dy):
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

    def draw(self, window):
        out = self.texture.copy()
        for obj in self.objects:
            obj.draw(out)
        window.blit(out, self.rect.topleft)

    def update(self):
        for obj in self.objects:
            obj.update()

class Entity(Object):
    def __init__(self, rect, texture, hit_box):
        super().__init__(rect, texture)
        self.hit_box = pygame.Rect(hit_box)
        self.hit_box_rect = pygame.Rect(hit_box)
        self.update_hit_box()
        self.tags = 0

    def update_hit_box(self):
        self.hit_box_rect.x = self.rect.x + self.hit_box.x
        self.hit_box_rect.y = self.rect.y + self.hit_box.y

    def collide(self, entity):
        # self.update_hit_box()
        # entity.update_hit_box()
        return self.hit_box_rect.colliderect(entity.hit_box_rect)

    def collidelist(self, entities):
        for entity in entities:
            if self.collide(entity):
                return True
        return False
    
    def draw(self, window):
        window.blit(self.texture, self.rect.topleft)
    
    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)
        self.update_hit_box()










