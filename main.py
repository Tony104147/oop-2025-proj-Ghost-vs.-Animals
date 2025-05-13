#!usr/bin/env python3
# -*- coding: utf-8 -*-

WINDOW_SIZE = (800, 600)

import pygame

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.init()

import pygame
from lib.game import Game

game = Game(window=window, current_map="test map", title="Game")
game.start()