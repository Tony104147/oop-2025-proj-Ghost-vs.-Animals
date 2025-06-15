# -*- coding: utf-8 -*-

import pygame

from object import Object

class Views:
    def __init__(self):
        self.settings = {
            'HP_bar_color' : (0, 255, 0, 100),
        }
    
    def draw(self, surface: pygame.Surface, informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
        HP_bar_color = self.settings['HP_bar_color']
        def draw_HP_bar(obj):
            bar_size = obj.rect.width * (obj['HP'] / obj['MAX_HP']), 10
            bar_pos = obj.rect.bottomleft
            pygame.draw.rect(surface, HP_bar_color, pygame.Rect(*bar_pos, *bar_size))
        
        for monster in informations['GROUPS']['MONSTERS']:
            draw_HP_bar(monster)
        draw_HP_bar(informations['MAINCHARACTER'])