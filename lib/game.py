# -*- coding utf-8 -*-

import pygame

from lib import counter
from maps import get_maps
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

        # Main character
        self.main_character = main_character.Main_character()

        # Load maps and set initial map
        self.maps = get_maps(self.WINDOW_SIZE, self.main_character)
        self.current_map = self.maps[current_map]

        # Skill objects group
        self.skill_objects = pygame.sprite.Group()

        # A function called when quit game
        self.do_quit = do_quit

        # Keep running game if true
        self.run = True


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