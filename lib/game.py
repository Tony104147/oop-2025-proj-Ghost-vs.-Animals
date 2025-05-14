# -*- coding utf-8 -*-

import random
import numpy as np

import pygame

from lib import counter
from maps import get_maps
from object.character import main_character
from object.skill import fire_ball

class Game:
    def __init__(self, *,
                 fps = 240,
                 window: pygame.Surface = None,
                 title = '',
                 current_map = "",
                 do_quit = None):
        self.window = window
        self.fps = fps
        self.title = title

        # Main character
        self.main_character = main_character.Main_character()

        # Load maps and set initial map
        w, h = self.window.get_size()
        size = w, h
        self.maps = get_maps(size, self.main_character)
        self.current_map = self.maps[current_map]
        self.main_character.restriction = self.current_map.image.get_rect()

        # Skill objects group
        self.skill_objects = pygame.sprite.Group()

        # A function called when quit game
        self.do_quit = do_quit

        # Keep running game if true
        self.run = True


    def start(self):
        # Open a window and start the game
        clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)

        # Game loop
        while self.run:
            # Handle events from Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        # shoot fire ball
                        x, y = pygame.mouse.get_pos()
                        dx = x*2 - self.main_character.rect.x
                        dy = y*2 - self.main_character.rect.y
                        _, direction = pygame.math.Vector2((dx, dy)).as_polar()
                        fireball = fire_ball.Fire_ball(self.main_character.rect.center, direction, self.current_map.enemies)
                        self.current_map['skills'].add(fireball)

            # Update objects
            self.current_map.update(self.get_informations())

            # Draw objects
            self.current_map.draw(self.window)

            # Refresh screen
            pygame.display.flip()

            # Update all counters
            counter.tick()

            # Maintain fps
            clock.tick_busy_loop(self.fps)
        
        # Do something before quiting the game
        if self.do_quit: self.do_quit()

        # Quit the game and close the window
        pygame.quit()
    
    def get_informations(self):
        groups = {
            "BLOCKS"       : self.current_map.blocks,
            "ENEMIES"      : self.current_map.enemies,
            "SKILLOBJECTS" : self.skill_objects,
        }

        informations = {
            "MAINCHARACTER" : self.main_character,
            "CURRENTMAP"    : self.current_map,
            "GROUPS"        : groups,
        }
        return informations