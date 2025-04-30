# -*- coding utf-8 -*-

import pygame

from lib.character import Character

main_character_setter = Character.Setter(
    rect = (0, 0, 0, 0),
    image = None,
    Name = "main character",
    MAX_HP = 100.0,
    HP = 100.0,
    ATK = 10.0,
    DEF = 10.0
)

class Main_character(Character):
    def __init__(self):
        super().__init__(main_character_setter)