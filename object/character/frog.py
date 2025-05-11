# -*- coding utf-8 -*-

import random
import numpy as np

import pygame

from lib.counter import Counter
from object import Object
from object.character import Character
from images import GETIMAGE

class Frog(Character):
    ''''''
    def __init__(self, pos: tuple[int]):
        super().__init__(rect=(*pos, 50, 50),
                         image=GETIMAGE("frog"),
                         Name="frog",
                         MAX_HP=150.0,
                         HP=150.0,
                         ATK=30.0,
                         DEF=20.0,
                         speed=3)

        self.attack_clock = Counter(240)
        self.jump_clock = Counter(360)
        self.anger_clock = Counter(600)
        self.destination = (0, 0)
        
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):

        # Move
        if self.jump_clock.ok():
            self.destination = informations["MAINCHARACTER"].rect.center
            self["ATK"] = 0.0
        
        if (self.rect.centerx != self.destination[0]) or (self.rect.centery != self.destination[1]):
            dx = self.destination[0] - self.rect.centerx
            dy = self.destination[1] - self.rect.centery
            offset = pygame.math.Vector2((dx, dy))
            if offset.length() > self['speed']:
                offset.scale_to_length(self["speed"])
            self.move(offset[:])
            self.jump_clock.reset()
        else:
            self["ATK"] = 30.0
        
        # attack
        if self.attack_clock.ok(False) and pygame.sprite.collide_rect(self, informations["MAINCHARACTER"]):
            informations["MAINCHARACTER"].attacked(self["ATK"])
            print(f"main charcter attacked by {self['Name']} | HP: {int(informations['MAINCHARACTER']['HP'])}")
            self.attack_clock.reset()

        # Call parent class update
        super().update(informations)