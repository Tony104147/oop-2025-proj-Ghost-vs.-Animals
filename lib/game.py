# -*- coding utf-8 -*-

import os
import importlib

import pygame

from maps import get_maps
from lib.event import Event, react
from object.character import main_character

class Game:
    def __init__(self, *,
                 fps = 120,
                 window_size = (800, 600),
                 title = '',
                 current_map = "",
                 do_quit = None):
        self.fps = fps
        self.WINDOW_SIZE = window_size
        self.title = title

        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.title)

        self.maps = get_maps(self.WINDOW_SIZE)
        self.current_map = self.maps[current_map]
        self.skill_objects = pygame.sprite.Group()

        # A function called when quit game
        self.do_quit = do_quit

        # Keep running game if true
        self.run = True

        # Main character
        self.main_character = main_character.Character()


    def start(self):
        # Open a window and start the game
        clock = pygame.time.Clock()

        # Game loop
        while self.run:
            # Handle events from Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_e:
                #         if self.main_character.rect.width < 200:
                #             self.main_character.rect.inflate_ip(5, 5)
                #     if event.key == pygame.K_q:
                #         if self.main_character.rect.width > 10:
                #             self.main_character.rect.inflate_ip(-5, -5)
                #     if event.key == pygame.K_SPACE:
                #         x, y = self.main_character.rect.size
                #         self.main_character.rect.inflate_ip(50 - x, 50 - y)

            key_pressed = pygame.key.get_pressed()
            # Main character moving from keyboard
            for key, movement in self.main_character.MOVING_DIRECTION.items():
                if key_pressed[key]:
                    self.main_character.move(movement, self.current_map.blocks, self.current_map.rect)

            # Draw objects
            self.current_map.objects.add(self.main_character)
            self.current_map.draw(self.window)

            # Refresh screen
            pygame.display.flip()

            # Maintain fps
            clock.tick_busy_loop(self.fps)
        
        # Do something before quiting the game
        if self.do_quit: self.do_quit()

        # Quit the game and close the window
        pygame.quit()
    
    def get_groups(self):
        groups = {
            "BLOCKS"        : self.current_map.blocks,
            "ENEMIES"       : self.current_map.enemies,
            "SKILL OBJECTS" : self.skill_objects,
        }
        return groups