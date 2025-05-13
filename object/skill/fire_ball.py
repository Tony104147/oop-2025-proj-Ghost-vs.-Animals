# -*- coding utf-8 -*-

import pygame

from lib.counter import Counter
from object import Object
from object.skill import Skill
from images import GETIMAGE

class Fire_ball(Skill):
    def __init__(self, pos, direction, target, damage_bonus = 1.0):
        super().__init__(rect = (*pos, 20, 20),
                         image = GETIMAGE("fire ball"),
                         Name = "fire ball",
                         damage = 20.0 * damage_bonus,
                         direction = direction,
                         speed = 10,
                         tags = 0)
        self.target = target
    
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        offset = pygame.math.Vector2.from_polar((self.speed, self.direction))
        self.rect.move_ip(*offset)

        blocked = pygame.sprite.spritecollideany(self, informations["GROUPS"]["BLOCKS"]) or \
                  pygame.sprite.spritecollideany(self, informations["GROUPS"]["ENEMIES"])
        if blocked: self.rect.inflate_ip(2, 2)

        enemies_colide = pygame.sprite.spritecollide(self, informations["GROUPS"]["ENEMIES"], False)
        for enemy in enemies_colide:
            enemy.attacked(self.damage)
            print(f"{enemy['Name']} attacked by fire ball | HP: {int(enemy['HP'])}")
        
        if enemies_colide or blocked:
            self.kill()