# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label, Box
from text import Text

class SettingPage:
    screen = None

    textures_button1 = None
    textures_button2 = None
    textures_button2_bar = None
    textures_label = None
    textures_page = None

    current_page = None
    current_button = None

    def __init__(self, size):
        SettingPage.screen = Screen(size, pygame.Surface(size), self.init)

        # button textures
        tex0 = pygame.image.load('src/button0.bmp').convert_alpha()
        tex1 = pygame.image.load('src/button1.bmp').convert_alpha()
        tex2 = pygame.image.load('src/button2.bmp').convert_alpha()
        SettingPage.textures_button1 = [tex0, tex1, tex2]

        tex0 = pygame.image.load('src/setting_page/button0.bmp').convert()
        tex1 = pygame.image.load('src/setting_page/button1.bmp').convert()
        SettingPage.textures_button2 = [tex0, tex1, tex1]

        tex0 = pygame.image.load('src/setting_page/button0_bar.bmp').convert()
        tex1 = pygame.image.load('src/setting_page/button1_bar.bmp').convert()
        SettingPage.textures_button2_bar = [tex0, tex1, tex1]

        # label texture
        tex0 = pygame.image.load('src/setting_page/Label0.bmp').convert()
        tex1 = pygame.Surface((0, 0)).convert()
        SettingPage.textures_label = [tex0, tex1]

        # setting page texture
        bg = pygame.Surface(size).convert_alpha()
        bg_mask = pygame.Surface((size[0] - 120, size[1] - 120)).convert_alpha()
        bg.fill((255, 255, 255, 100))
        bg_mask.fill((170, 170, 170, 255))
        bg.blit(bg_mask, (60, 60))
        SettingPage.textures_page = bg

        # objects
        self.button_back = get_Button_back()
        self.button_quit = get_Button1('Quit game', (80, 495), (190, 35), Window.quit)

        # general page
        self.page_general = get_Box((290, 70), (440, 460), (170, 170, 170))
        # general page - volume
        self.label_volume = get_Label1('Volume', (0, 0))
        self.label_volume_val = get_Label2('100', (200, 0))
        self.button_volume_add = get_Button1('+', (400, 4), (36, 36), self.volume_add)
        self.button_volume_sub = get_Button1('-', (164, 4), (36, 36), self.volume_sub)
        self.page_general.add_object(self.label_volume)
        self.page_general.add_object(self.label_volume_val)
        self.page_general.add_object(self.button_volume_add)
        self.page_general.add_object(self.button_volume_sub)
        # general page - fps
        self.label_fps = get_Label1('Fps', (0, 44))
        self.label_fps_val = get_Label2('60', (200, 44))
        self.button_fps_add = get_Button1('+', (400, 48), (36, 36), self.fps_add)
        self.button_fps_sub = get_Button1('-', (164, 48), (36, 36), self.fps_sub)
        self.page_general.add_object(self.label_fps)
        self.page_general.add_object(self.label_fps_val)
        self.page_general.add_object(self.button_fps_add)
        self.page_general.add_object(self.button_fps_sub)

        # keyboard page
        self.page_keyboard = get_Box((290, 70), (440, 460), (170, 170, 170))

        # view page
        self.page_view = get_Box((290, 70), (440, 460), (170, 170, 170))

        # select box
        self.box_page_select = get_Box((70, 70), (210, 154), (150, 150, 150))
        self.button_general = get_Button2('General', (0, 2), self.show_general_page)
        self.button_keyboard = get_Button2('Keyboard', (0, 52), self.show_keyboard_page)
        self.button_view = get_Button2('View', (0, 102), self.show_view_page)
        self.box_page_select.add_object(self.button_general)
        self.box_page_select.add_object(self.button_keyboard)
        self.box_page_select.add_object(self.button_view)
        SettingPage.current_page = self.page_general
        SettingPage.current_button = self.button_general

        # load objects
        SettingPage.screen.add_object(self.box_page_select)
        SettingPage.screen.add_object(self.page_general)
        SettingPage.screen.add_object(self.button_quit)
        SettingPage.screen.add_object(self.button_back)

        # keyboard
        SettingPage.screen.keyboard.add_callback(Window.back_screen, pygame.K_ESCAPE)

        # ...

    def init(self):
        SettingPage.screen.texture = Window.window.copy()
        SettingPage.screen.texture.blit(SettingPage.textures_page, (0, 0))
        self.show_general_page()

    def show_setting_page(self, page, button):
        SettingPage.screen.remove_object(SettingPage.current_page)
        SettingPage.screen.add_object(page)
        SettingPage.current_button.texture = SettingPage.textures_button2
        button.texture = SettingPage.textures_button2_bar
        SettingPage.current_button = button
        SettingPage.current_page = page

    def show_general_page(self):
        self.show_setting_page(self.page_general, self.button_general)

    def show_keyboard_page(self):
        self.show_setting_page(self.page_keyboard, self.button_keyboard)

    def show_view_page(self):
        self.show_setting_page(self.page_view, self.button_view)

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
                  SettingPage.textures_label[0],
                  text)

def get_Label2(text, pos):
    size = (200, 44)

    # text
    text = Text(text, 28, (0, 0, 0))
    text.typeset(size, Text.CENTER)

    return Label((*pos, *size),
                  SettingPage.textures_label[1],
                  text)

def get_Button(text, rect, textures, callback):
    pos = rect[:2]
    size = rect[2:]

    # text
    text = Text(*text, (0, 0, 0))
    text.typeset(size, Text.CENTER)

    #textures
    tex0, tex1, tex2 = textures
    tex0 = pygame.transform.scale(tex0, size)
    tex1 = pygame.transform.scale(tex1, size)
    tex2 = pygame.transform.scale(tex2, size)

    return Button(rect,
                  [tex0, tex1, tex2],
                  [callback] + [Object.do_nothing]*4,
                  text)

def get_Button_back():
    size = (50, 50)
    pos = (0, 0)

    # textures
    tex = pygame.image.load('src/setting_icon.bmp').convert_alpha()
    tex = pygame.transform.scale(tex, size)

    return get_Button(('', 0), (*pos, *size), [tex]*3, Window.back_screen)

def get_Button1(text, pos, size, callback):
    return get_Button((text, 28), (*pos, *size), SettingPage.textures_button1, callback)

def get_Button2(text, pos, callback):
    size = (210, 50)

    return get_Button((text, 30), (*pos, *size), SettingPage.textures_button2, callback)

def get_Box(pos, size, color):
    texture = pygame.Surface(size).convert()
    texture.fill(color)

    return Box((*pos, *size), texture)
            
