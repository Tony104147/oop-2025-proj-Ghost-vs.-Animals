# -*- coding utf-8 -*-

import pygame

from lib.counter import Counter
from lib.event import post, new
from object import Object
from object.character import Character

class Main_character(Character):
    '''
    Main character class, the player character in the game.
    '''
    def __init__(self):
        super().__init__(rect=(100, 100, 80, 80),
                         image="ghost",
                         Name="main character",
                         MAX_HP=100.0,
                         HP=100.0,
                         ATK=10.0,
                         DEF=10.0,
                         speed=10)

        self.MOVING_DIRECTION = {
            pygame.K_w : (0, -1),
            pygame.K_a : (-1, 0),
            pygame.K_s : (0, 1),
            pygame.K_d : (1, 0),
        }

        self.attack_clock = Counter(240)
        self.heal_clock = Counter(480)

        new('ENDGAME')
    
    def update(self, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        # Move
        key_pressed = pygame.key.get_pressed()
        for key, direction in self.MOVING_DIRECTION.items():
            if key_pressed[key]:
                offset = pygame.math.Vector2(direction)
                offset.scale_to_length(self["speed"])
                super().move(offset, informations["GROUPS"]["BLOCKS"], informations['RESTRICTION'])
        
        # Attack
        if self.attack_clock.ok(False):
            monsters_collide = pygame.sprite.spritecollide(self, informations["GROUPS"]["MONSTERS"], False)
            for enemy in monsters_collide:
                enemy.attacked(self["ATK"])
                print(f"{enemy['Name']} attacked by you | HP: {int(self['HP'])}")
                self.attack_clock.reset()
        
        # Dead
        if self["HP"] == 0:
            print("Ypu are dead!!!")
            post('ENDGAME')
        
        # # Heal
        # if self.heal_clock.ok():
        #     self.heal(5)
        #     print(f"main character heals 5 HP | HP: {int(self['HP'])}")
        
        # Call parent class update
        super().update(informations)
    
    def attacked(self, value):
        self.heal_clock.reset()
        return super().attacked(value)
