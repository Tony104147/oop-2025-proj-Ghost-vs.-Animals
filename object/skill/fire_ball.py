# -*- coding utf-8 -*-

import pygame

from lib.counter import Counter
from object import Object
from object.skill import Skill

class Fire_ball(Skill):
    '''
    Fire ball class, a skill in the game.
    '''
    def __init__(self, pos, direction, target, damage_bonus = 1.0):
        super().__init__(rect = (*pos, 20, 20),
                         image = 'fire ball',
                         Name = "fire ball",
                         damage = 20.0 * damage_bonus,
                         direction = direction,
                         speed = 15,
                         tags = 0)
        self.target: pygame.sprite.Group = target
    
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        offset = pygame.math.Vector2.from_polar((self.speed, self.direction))
        self.rect.move_ip(*offset)

        # Check collision with blocks or characters
        blocked = pygame.sprite.spritecollideany(self, informations["GROUPS"]["BLOCKS"]) or \
                  pygame.sprite.spritecollideany(self, self.target)
        # If blocked, inflate the rect to make it easier to hit monsters (e.g., fire ball explosion)
        if blocked: self.rect.inflate_ip(20, 20)

        # Check collision with characters
        characters_colide = pygame.sprite.spritecollide(self, self.target, False)
        for character in characters_colide:
            character.attacked(self.damage)
            print(f"{character['Name']} attacked by fire ball | HP: {int(character['HP'])}")
        
        # If the fire ball collides with a character or is blocked, it will be removed
        restriction = informations['RESTRICTION']
        if characters_colide or blocked or (not restriction.collidepoint(self.rect.center)):
            self.kill()
