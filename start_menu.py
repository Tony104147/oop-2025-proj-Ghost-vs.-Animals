#!python3.10
# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label
from text import Text

class StartMenu:
    screen = None

    def __init__(self, size):
        img1 = pygame.image.load('src/start_menu/forest.png').convert()
        bg = pygame.transform.scale(img1, size)
        StartMenu.screen = Screen(size, bg)

        # objects
        Buttons = get_Buttons(self)
        self.button_settings = Buttons.pop(0)
        self.button_start = Buttons.pop(0)
        self.button_load = Buttons.pop(0)
        self.button_guide = Buttons.pop(0)

        # load objects
        StartMenu.screen.add_object(self.button_settings)
        StartMenu.screen.add_object(self.button_start)
        StartMenu.screen.add_object(self.button_load)
        StartMenu.screen.add_object(self.button_guide)

        # vars
        self.size = size

        # keyboard
        StartMenu.screen.keyboard.add_callback(StartMenu.goto_setting_page, pygame.K_ESCAPE)


    def goto_setting_page():
        Window.set_screen('setting_page')

    def button_start_click(self):
        Window.set_screen('start_village')
        pass

    def button_load_click(self):
        pass

    def button_guide_click(self):
        pass

def get_Buttons(self):
    # textures
    tex = pygame.image.load('src/setting_icon.bmp').convert_alpha()
    textures0 = [tex]*3
    # button textures
    tex0 = pygame.image.load('src/button0.bmp').convert_alpha()
    tex1 = pygame.image.load('src/button1.bmp').convert_alpha()
    tex2 = pygame.image.load('src/button2.bmp').convert_alpha()
    textures1 = [tex0, tex1, tex2]

    buttons_set = [
    #  | text   | pos       | size      | textures | text_size | callback 
    #   -----------------------------------------------------------------------
        (''     , (0  , 0  ), (50 , 50 ), textures0, 0         , StartMenu.goto_setting_page),
        ('Start', (160, 260), (480, 80 ), textures1, 60        , self.button_start_click),
        ('Load' , (160, 350), (230, 60 ), textures1, 40        , self.button_load_click),
        ('Guide', (410, 350), (230, 60 ), textures1, 40        , self.button_guide_click)
    ]

    buttons = []
    for text, pos, size, textures, text_size, callback in buttons_set:
        # text
        text = Text(text, text_size, (0, 0, 0))
        text.typeset(size, Text.CENTER)

        # textures
        tex0, tex1, tex2 = textures
        tex0 = pygame.transform.scale(tex0, size)
        tex1 = pygame.transform.scale(tex1, size)
        tex2 = pygame.transform.scale(tex2, size)

        buttons.append(Button((*pos, *size), [tex0, tex1, tex2],
                              [callback] + [Object.do_nothing]*4, text))

    return buttons
