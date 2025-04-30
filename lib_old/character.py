# -*- coding utf-8 -*-

import pygame
import add_path
from objects import Entity
from keyboard import KeyBoard
from window import Window

class Character(Entity):
    def __init__(self):
        pos = (50, 300)
        size = (50, 50)
        super().__init__((*pos, *size))

        self.texture = pygame.Surface(size)
        self.texture.fill((200, 0, 200))
        self.hit_box.update(0, 30, 50, 20)

        self.velocity = 480
        self.current_map = None

    def move(self, dx, dy):
        original_pos = self.rect.topleft
        super().move(dx, dy)
        self.clip_pos()
        entities = self.current_map.entities
        barriers = [entity for entity in entities if entity.tag.fit(Entity.Tag.BLOCKING)]
        if self.collidelist(barriers):
            self.rect.topleft = original_pos

    def clip_pos(self):
        w, h = Window.window.get_size()
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > w: self.rect.right = w
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > h: self.rect.bottom = h

    def update(self):
        pressed = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        dx, dy = 0, 0
        if pressed[pygame.K_UP]:    dy -= 1
        if pressed[pygame.K_DOWN]:  dy += 1
        if pressed[pygame.K_LEFT]:  dx -= 1
        if pressed[pygame.K_RIGHT]: dx += 1
        move_times = self.velocity // Window.fps
        if mods & pygame.KMOD_SHIFT:
            move_times *= 2
        for i in range(move_times):
            self.move(dx, dy)
