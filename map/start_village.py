# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label, Box, Entity
from text import Text
from character import Character

class StartVillage:
    screen = None
    walls = []

    def __init__(self, size):
        StartVillage.screen = Screen(size, pygame.Surface(size), self.init)

        walls = get_walls()
        StartVillage.walls = walls.copy()
        self.wall_1 = walls.pop(0)
        self.wall_2 = walls.pop(0)
        self.wall_3 = walls.pop(0)
        self.wall_4 = walls.pop(0)

        # load objects
        StartVillage.screen.add_object(self.wall_1)
        StartVillage.screen.add_object(self.wall_2)
        StartVillage.screen.add_object(self.wall_3)
        StartVillage.screen.add_object(self.wall_4)
        StartVillage.screen.add_object(Character.entity)

    def init(self):
        Character.current_map = self

    def character_move_up():
        Character.move(0, -Character.speed, StartVillage.walls)

    def character_move_left():
        Character.move(-Character.speed, 0, StartVillage.walls)

    def character_move_down():
        Character.move(0, Character.speed, StartVillage.walls)

    def character_move_right():
        Character.move(Character.speed, 0, StartVillage.walls)

def get_walls():
    size = (300, 60)
    texture0 = pygame.Surface(size)
    texture0.fill((50, 210, 30))

    wall_sets = [
    #  | pos       | size     | texture |
    #   ---------------------------------
        ((0  , 0  ), size     , texture0),
        ((500, 0  ), size     , texture0),
        ((0  , 540), size     , texture0),
        ((500, 540), size     , texture0),
    ]

    walls = []
    for pos, size, texture in wall_sets:
        walls.append(Entity((*pos, *size), texture, (0, 0, *size)))

    return walls







