#!python3.10
# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label
from text import Text

class StartMenu(Screen):
    screen = None

    button_textures = None

    def __init__(self, size):
        img1 = pygame.image.load('src/forest.png').convert()
        bg = pygame.transform.scale(img1, size)
        StartMenu.screen = Screen(bg)

        # button textures
        tex0 = pygame.image.load('src/button0.bmp').convert()
        tex1 = pygame.image.load('src/button1.bmp').convert()
        tex2 = pygame.image.load('src/button2.bmp').convert()
        tex0.set_colorkey((0, 0, 0))
        tex1.set_colorkey((0, 0, 0))
        tex2.set_colorkey((0, 0, 0))

        StartMenu.button_textures = [tex0, tex1, tex2]

        # objects
        self.button_settings = Button_settings(StartMenu.goto_setting_page, size)
        self.button_start = Button_start(self.button_start_click, size)
        self.button_load = Button_load(self.button_load_click, size)
        self.button_guide = Button_guide(self.button_guide_click, size)

        # load objects
        StartMenu.screen.add_object(self.button_settings)
        StartMenu.screen.add_object(self.button_start)
        StartMenu.screen.add_object(self.button_load)
        StartMenu.screen.add_object(self.button_guide)

        # flags

        # vars
        self.size = size

        # keyboard
        StartMenu.screen.keyboard.add_callback(StartMenu.goto_setting_page, pygame.K_ESCAPE)


    def goto_setting_page():
        Window.set_screen('setting_page')

    def button_start_click(self):
        pass

    def button_load_click(self):
        pass

    def button_guide_click(self):
        pass

def Button_settings(callback, size):
    SIZE = (50, 50)
    pos = (0, 0)

    # textures
    tex = pygame.image.load('src/setting_icon.bmp').convert()
    tex = pygame.transform.scale(tex, SIZE)
    tex.set_colorkey((0, 0, 0))

    return Button((*pos, *SIZE),
                  [tex]*3,
                  [callback] + [Object.do_nothing]*4)

def Button_start(callback, size):
    SIZE = (480, 80)
    pos = round((size[0] - SIZE[0]) / 2), round(size[1] / 2 - SIZE[1] / 2)

    # textures
    tex0, tex1, tex2 = StartMenu.button_textures
    tex0 = pygame.transform.scale(tex0, SIZE)
    tex1 = pygame.transform.scale(tex1, SIZE)
    tex2 = pygame.transform.scale(tex2, SIZE)

    # text
    text = Text('Start', 60, (0, 0, 0))
    text.typeset(SIZE, Text.CENTER)

    return Button((*pos, *SIZE),
                  [tex0, tex1, tex2],
                  [callback] + [Object.do_nothing]*4,
                  text)

def Button_load(callback, size):
    SIZE = (230, 60)
    pos = round(size[0] / 2 - SIZE[0] - 10), round(size[1] / 2 + 60)

    # textures
    tex0, tex1, tex2 = StartMenu.button_textures
    tex0 = pygame.transform.scale(tex0, SIZE)
    tex1 = pygame.transform.scale(tex1, SIZE)
    tex2 = pygame.transform.scale(tex2, SIZE)

    # text
    text = Text('Load', 40, (0, 0, 0))
    text.typeset(SIZE, Text.CENTER)

    return Button((*pos, *SIZE),
                  [tex0, tex1, tex2],
                  [callback] + [Object.do_nothing]*4,
                  text)

def Button_guide(callback, size):
    SIZE = (230, 60)
    pos = round(size[0] / 2 + 10), round(size[1] / 2 + 60)

    # textures
    tex0, tex1, tex2 = StartMenu.button_textures
    tex0 = pygame.transform.scale(tex0, SIZE)
    tex1 = pygame.transform.scale(tex1, SIZE)
    tex2 = pygame.transform.scale(tex2, SIZE)

    # text
    text = Text('Guide', 40, (0, 0, 0))
    text.typeset(SIZE, Text.CENTER)

    return Button((*pos, *SIZE),
                  [tex0, tex1, tex2],
                  [callback] + [Object.do_nothing]*4,
                  text)
