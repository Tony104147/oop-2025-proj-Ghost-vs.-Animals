#!usr/bin/env python3
# -*- coding: utf-8 -*-

from pygame import *
import pygame
from lib.game import Game

WINDOW_SIZE = (800, 600)
pygame.init()

game = Game(window_size=WINDOW_SIZE, current_map="test map", title="Game")
game.start()