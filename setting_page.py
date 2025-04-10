# -*- coding utf-8 -*-

import pygame
import add_path
from window import Window, Screen
from objects import Object, Button, Label, Box
from text import Text

class SettingPage:
    screen = None

    textures_button = None
    textures_button_bar = None
    textures_page = None

    current_page = None
    current_button = None

    def __init__(self, size):
        SettingPage.screen = Screen(size, pygame.Surface(size), self.init)


        # setting page texture
        bg = pygame.Surface(size).convert_alpha()
        bg_mask = pygame.Surface((size[0] - 120, size[1] - 120)).convert_alpha()
        bg.fill((255, 255, 255, 100))
        bg_mask.fill((170, 170, 170, 255))
        bg.blit(bg_mask, (60, 60))
        SettingPage.textures_page = bg

        tex0 = pygame.image.load('src/setting_page/button0.bmp').convert()
        tex1 = pygame.image.load('src/setting_page/button1.bmp').convert()
        SettingPage.textures_button = [tex0, tex1, tex0]
        tex0 = pygame.image.load('src/setting_page/button0_bar.bmp').convert()
        tex1 = pygame.image.load('src/setting_page/button1_bar.bmp').convert()
        SettingPage.textures_button_bar = [tex0, tex1, tex0]

        # objects
        Labels = get_Label()
        self.label_volume = Labels[0]
        self.label_volume_val = Labels[1]
        self.label_fps = Labels[2]
        self.label_fps_val = Labels[3]

        Buttons = get_Buttons(self)
        self.button_back = Buttons[0]
        self.button_quit = Buttons[1]
        self.button_volume_add = Buttons[2]
        self.button_volume_sub = Buttons[3]
        self.button_fps_add = Buttons[4]
        self.button_fps_sub = Buttons[5]
        self.button_general = Buttons[6]
        self.button_keyboard = Buttons[7]
        self.button_view = Buttons[8]

        # general page
        self.page_general = get_Box((290, 70), (440, 460), (170, 170, 170))
        # general page - volume
        self.page_general.add_object(self.label_volume)
        self.page_general.add_object(self.label_volume_val)
        self.page_general.add_object(self.button_volume_add)
        self.page_general.add_object(self.button_volume_sub)
        # general page - fps
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
        SettingPage.current_button.texture = SettingPage.textures_button
        button.texture = SettingPage.textures_button_bar
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

def get_Label():
    text_size = 28

    # textures
    tex0 = pygame.image.load('src/setting_page/Label0.bmp').convert()
    tex1 = pygame.Surface((0, 0)).convert()

    labels_set = [
    #  | text    | pos      | size     | texture
    #   ------------------------------------------
        ('Volume', (0  , 0) , (160, 44), tex0),
        ('100'   , (200, 0) , (200, 44), tex1),
        ('Fps'   , (0  , 44), (160, 44), tex0),
        ('60'    , (200, 44), (200, 44), tex1)
        ]

    labels = []
    for text, pos, size, texture in labels_set:
        # text
        text = Text(text, text_size, (0, 0, 0))
        text.typeset(size, Text.CENTER)

        labels.append(Label((*pos, *size), texture, text))

    return labels

def get_Buttons(self):
    text_size = 28

    # textures
    tex = pygame.image.load('src/setting_icon.bmp').convert_alpha()
    tex = pygame.transform.scale(tex, (50, 50))
    textures0 = [tex]*3
    tex0 = pygame.image.load('src/button0.bmp').convert_alpha()
    tex1 = pygame.image.load('src/button1.bmp').convert_alpha()
    tex2 = pygame.image.load('src/button2.bmp').convert_alpha()
    tex0 = pygame.transform.scale(tex0, (190, 35))
    tex1 = pygame.transform.scale(tex1, (190, 35))
    tex2 = pygame.transform.scale(tex2, (190, 35))
    textures1 = [tex0, tex1, tex2]
    tex0 = pygame.transform.scale(tex0, (36, 36))
    tex1 = pygame.transform.scale(tex1, (36, 36))
    tex2 = pygame.transform.scale(tex2, (36, 36))
    textures2 = [tex0, tex1, tex2]
    textures3 = SettingPage.textures_button
    textures3_bar = SettingPage.textures_button_bar

    buttons_set = [
    #  | text       | pos       | size      | textures | text_size | callback 
    #   -----------------------------------------------------------------------
        (''         , (0  , 0  ), (50 , 50 ), textures0, 0         , Window.back_screen),
        ('Quit Game', (80 , 495), (190, 35 ), textures1, text_size , Window.quit),
        ('+'        , (400, 4  ), (36 , 36 ), textures2, text_size , self.volume_add),
        ('-'        , (164, 4  ), (36 , 36 ), textures2, text_size , self.volume_sub),
        ('+'        , (400, 48 ), (36 , 36 ), textures2, text_size , self.fps_add),
        ('-'        , (164, 48 ), (36 , 36 ), textures2, text_size , self.fps_sub),
        ('Genaral'  , (0  , 2  ), (210, 50 ), textures3, text_size , self.show_general_page),
        ('Keyboard' , (0  , 52 ), (210, 50 ), textures3, text_size , self.show_keyboard_page),
        ('View'     , (0  , 102), (210, 50 ), textures3, text_size , self.show_view_page)
    ]

    buttons = []
    for text, pos, size, textures, text_size, callback in buttons_set:
        # text
        text = Text(text, text_size, (0, 0, 0))
        text.typeset(size, Text.CENTER)

        buttons.append(Button((*pos, *size), textures,
                              [callback] + [Object.do_nothing]*4, text))

    return buttons

def get_Box(pos, size, color):
    texture = pygame.Surface(size).convert()
    texture.fill(color)

    return Box((*pos, *size), texture)
            
