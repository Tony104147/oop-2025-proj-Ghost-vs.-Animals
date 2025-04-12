# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label, Box, Entity
from keyboard import KeyBoard

class Character(Entity):
    entity = None
    speed = 5
    current_map = None
    keyboard = KeyBoard()

    def __init__(self):
        pos = (50, 300)
        size = (50, 50)
        texture = pygame.Surface(size)
        texture.fill((200, 0, 200))
        hit_box = (0, 30, 50, 20)
        super().__init__((*pos, *size), texture, hit_box)
        Character.entity = self

        # keyboard
        set_keyboard()

    def move(self, dx, dy):
        super().move(dx, dy)
        self.clip_pos()
        if self.collidelist(Character.current_map.walls):
            super().move(-dx, -dy)

    def move_up():
        Character.entity.move(0, -Character.speed)

    def move_left():
        Character.entity.move(-Character.speed, 0)
    
    def move_down():
        Character.entity.move(0, Character.speed)
    
    def move_right():
        Character.entity.move(Character.speed, 0)

    def clip_pos(self):
        rect = self.rect
        w, h = Window.window.get_size()
        if rect.left < 0: self.rect.left = 0
        if rect.right > w: self.rect.right = w
        if rect.top < 0: self.rect.top = 0
        if rect.bottom > h: self.rect.bottom = h

    def update(self):
        pressed = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        for key in range(len(pressed)):
            if pressed[key]:
                Character.keyboard.key_press(key, mods)

def set_keyboard():
    keyboard_sets = [
        (Character.move_up, pygame.K_w),
        (Character.move_left, pygame.K_a),
        (Character.move_down, pygame.K_s),
        (Character.move_right, pygame.K_d)
    ]
    for keyboard_set in keyboard_sets:
        Character.keyboard.add_callback(*keyboard_set)
