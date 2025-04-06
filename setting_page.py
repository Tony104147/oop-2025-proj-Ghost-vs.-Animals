# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label, Box
from text import Text

class SettingPage(Screen):
    screen = None

    button_textures = None
    label_textures = None
    setting_page_tex = None

    def __init__(self, size):
        SettingPage.screen = Screen(None, SettingPage.init)

        # button textures
        tex0 = pygame.image.load('src/button0.bmp').convert()
        tex1 = pygame.image.load('src/button1.bmp').convert()
        tex2 = pygame.image.load('src/button2.bmp').convert()
        tex0.set_colorkey((0, 0, 0))
        tex1.set_colorkey((0, 0, 0))
        tex2.set_colorkey((0, 0, 0))

        SettingPage.button_textures = [tex0, tex1, tex2]

        # label texture
        tex0 = pygame.image.load('src/Label0.bmp').convert()
        tex1 = pygame.Surface((0, 0)).convert()

        SettingPage.label_textures = [tex0, tex1]

        # setting page texture
        bg = pygame.Surface(size).convert_alpha()
        bg_mask = pygame.Surface((size[0] - 120, size[1] - 120)).convert_alpha()
        bg.fill((255, 255, 255, 100))
        bg_mask.fill((170, 170, 170, 255))
        bg.blit(bg_mask, (60, 60))

        SettingPage.setting_page_tex = bg

        # objects
        self.button_quit = get_Button1('Quit game', (70, size[1] - 105), Window.quit)
        self.button_back = get_Button1('Back', (70, 70), Window.back_screen)

        self.box1 = get_Box()
        # volume
        self.label_volume = get_Label1('Volume', (0, 0))
        self.label_volume_val = get_Label2('100', (200, 0))
        self.button_volume_add = get_Button2('+', (400, 4), self.volume_add)
        self.button_volume_sub = get_Button2('-', (164, 4), self.volume_sub)
        self.box1.add_object(self.label_volume)
        self.box1.add_object(self.label_volume_val)
        self.box1.add_object(self.button_volume_add)
        self.box1.add_object(self.button_volume_sub)
        # fps
        self.label_fps = get_Label1('Fps', (0, 44))
        self.label_fps_val = get_Label2('30', (200, 44))
        self.button_fps_add = get_Button2('+', (400, 48), self.fps_add)
        self.button_fps_sub = get_Button2('-', (164, 48), self.fps_sub)
        self.box1.add_object(self.label_fps)
        self.box1.add_object(self.label_fps_val)
        self.box1.add_object(self.button_fps_add)
        self.box1.add_object(self.button_fps_sub)

        # load objects
        SettingPage.screen.add_object(self.button_quit)
        SettingPage.screen.add_object(self.button_back)
        SettingPage.screen.add_object(self.box1)

        # keyboard
        SettingPage.screen.keyboard.add_callback(Window.back_screen, pygame.K_ESCAPE)

        # ...

    def init():
        SettingPage.screen.bg = Window.window.copy()
        SettingPage.screen.bg.blit(SettingPage.setting_page_tex, (0, 0))

    def fps_add(self):
        if Window.fps < 60:
            Window.fps += 15
            self.label_fps_val.text.text = str(Window.fps)

    def fps_sub(self):
        if Window.fps > 30:
            Window.fps -= 15
            self.label_fps_val.text.text = str(Window.fps)

    def volume_add(self):
        if Window.volume < 100:
            Window.volume += 1
            self.label_volume_val.text.text = str(Window.volume)
            self.label_volume_val.text.typeset((200, 44), Text.CENTER)

    def volume_sub(self):
        if Window.volume > 0:
            Window.volume -= 1
            self.label_volume_val.text.text = str(Window.volume)
            self.label_volume_val.text.typeset((200, 44), Text.CENTER)

def get_Label1(text, pos):
    size = (440, 44)

    # text
    text = Text(text, 28, (0, 0, 0))
    text.typeset((160, size[1]), Text.CENTER)

    return Label((*pos, *size),
                  SettingPage.label_textures[0],
                  text)

def get_Label2(text, pos):
    size = (200, 44)

    # text
    text = Text(text, 28, (0, 0, 0))
    text.typeset(size, Text.CENTER)

    return Label((*pos, *size),
                  SettingPage.label_textures[1],
                  text)

def get_Button1(text, pos, callback):
    size = (200, 35)
    tex0, tex1, tex2 = SettingPage.button_textures

    #textures
    tex0 = pygame.transform.scale(tex0, size)
    tex1 = pygame.transform.scale(tex1, size)
    tex2 = pygame.transform.scale(tex2, size)

    # text
    text = Text(text, 25, (0, 0, 0))
    text.typeset(size, Text.CENTER)

    return Button((*pos, *size),
                  [tex0, tex1, tex2],
                  [callback] + [Object.do_nothing]*4,
                  text)

def get_Button2(text, pos, callback):
    size = (36, 36)
    tex0, tex1, tex2 = SettingPage.button_textures

    #textures
    tex0 = pygame.transform.scale(tex0, size)
    tex1 = pygame.transform.scale(tex1, size)
    tex2 = pygame.transform.scale(tex2, size)

    # text
    text = Text(text, 32, (0, 0, 0))
    text.typeset(size, Text.CENTER)

    return Button((*pos, *size),
                  [tex0, tex1, tex2],
                  [callback] + [Object.do_nothing]*4,
                  text)

def get_Box():
    size = (440, 460)
    pos = (280, 70)
    texture = pygame.Surface(size).convert()
    texture.fill((170, 170, 170))

    return Box((*pos, *size), texture)
            
