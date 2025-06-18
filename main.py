#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
pygame.init()

WINDOW_SIZE = (800, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

# Class for runnig the game
class Game:
    def __init__(self):
        self.window: pygame.Surface = WINDOW
        self.fps: int = 60
        self.title: str = ''

        self.maps: dict[str, Map] = load_maps()
        self.current_map: str = ''

        self.main_character: Main_character = Main_character()

        self.run: bool = True

        self.views = views.Views()
    
    # Start the game
    def start(self):
        clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)
        self.set_map('map1')

        score = 0

        # Game loop
        while self.run:
            # Handle events from Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        # shoot fire ball
                        x, y = self.get_mouse_pos()
                        dx = x - self.main_character.rect.centerx
                        dy = y - self.main_character.rect.centery
                        _, direction = pygame.math.Vector2((dx, dy)).as_polar()
                        fireball = Fire_ball(
                            self.main_character.rect.center, direction, self.maps[self.current_map].groups['MONSTERS'])
                        self.maps[self.current_map].groups['SKILLS'].add(fireball)
                elif event.type == TYPES['REBORN']:
                    self.maps[self.current_map].groups['MONSTERS'].add(event.monsters)
                elif event.type == TYPES['SCORE']:
                    score += event.value
                elif event.type == TYPES['ENDGAME']:
                    print(f"\nGAME OVER\nScore: {score}")
                    pygame.quit()
                    return

            # Update objects
            informations = self.get_informations()
            self.maps[self.current_map].update(informations)
            for group in self.maps[self.current_map].groups.values():
                for obj in group:
                    obj.update(informations)
            self.main_character.update(informations)

            # Update scene of the window
            picture = self.maps[self.current_map].image
            picture = pygame.transform.scale(GETIMAGE(picture), self.maps[self.current_map].size)
            for group in self.maps[self.current_map].groups.values():
                for obj in group:
                    obj.draw(picture)
            self.main_character.draw(picture)
            self.views.draw(picture, informations)

            picture = pygame.transform.scale(picture, WINDOW_SIZE)
            self.window.blit(picture, (0, 0))

            # Refresh screen
            pygame.display.flip()

            # Increase the counter
            counter.tick()

            # Maintain fps
            clock.tick_busy_loop(self.fps)

        # Quit the game and close the window
        pygame.quit()
    
    def get_informations(self):
        informations = {
            'WINDOWSIZE' : WINDOW_SIZE,
            'FPS' : self.fps,
            'MAINCHARACTER' : self.main_character,
            'GROUPS' : self.maps[self.current_map].groups,
            'RESTRICTION' : pygame.Rect((0, 0), self.maps[self.current_map].size).inflate(-30, -50),
        }
        return informations
    
    def set_map(self, name: str):
        if self.current_map is not name:
            self.current_map = name
            self.maps[self.current_map].init()
            Log(f'map setted: {name}')
    
    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        size = self.maps[self.current_map].size
        return (x * size[0] / WINDOW_SIZE[0]), (y * size[0] / WINDOW_SIZE[0])





from object.character.main_character import Main_character
from object.skill.fire_ball import Fire_ball
from maps import Map, load_maps
from lib.image import GETIMAGE, SETIMAGE, load_images
from lib.log import Log
from lib.event import TYPES, post, new
from lib import counter, views


def main():
    load_images()

    start_game = False
    blank_surface = pygame.Surface(WINDOW_SIZE)
    blank_surface.fill((0, 0, 0))
    start_font = pygame.font.Font(None, 50)
    start_text = start_font.render('Press \'space\' to start', False, (255, 255, 255))
    w, h = start_font.size('Press \'space\' to start')
    while not start_game:
        WINDOW.blit(blank_surface, (0, 0))
        WINDOW.blit(start_text, ((WINDOW_SIZE[0] - w) / 2, (WINDOW_SIZE[1] + h) / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                start_game = True

        pygame.display.flip()

    game = Game()
    game.start()

if __name__ == '__main__':
    main()
