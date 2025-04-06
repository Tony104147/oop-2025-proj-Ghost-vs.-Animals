#!python3.10
# -*- coding utf-8 -*-

import pygame
from objects import Object
from keyboard import KeyBoard

class Window:
    window = None

    # vars
    fps = None
    volume = 100
    _clock = None
    _screen = None
    screens = {}
    last_screen = ['_']

    # flags
    running = True

    def __init__(self,
                 size,
                 fps = 30,
                 title = '',
                 flags = 0):
        pygame.init()
        Window.window = pygame.display.set_mode(size, flags)
        pygame.display.set_caption(title)

        # const vars

        # vars
        Window.fps = fps
        Window._clock = pygame.time.Clock()
        Window._screen = Screen(pygame.Surface(size))

    def set_screen(screen_name):
        if Window.last_screen[-1] != screen_name:
            Window._screen = Window.screens[screen_name]
            Window._screen.init()
            Window.last_screen.append(screen_name)
        print(Window.last_screen)

    def back_screen():
        if len(Window.last_screen) > 2:
            Window.last_screen.pop()
            Window._screen = Window.screens[Window.last_screen[-1]]
            Window._screen.init()
        print(Window.last_screen)

    def add_screen(screen_name, screen):
        Window.screens[screen_name] = screen

    def _mouse_button_down(event):
        Window._screen.mouse_down_event(event)

    def _mouse_button_up(event):
        Window._screen.mouse_up_event(event)

    def _key_button_down(event):
        Window._screen.keyboard.key_press(event.key, event.mod)

    def _key_button_up(event):
        Window._screen.keyboard.key_release(event.key, event.mod)

    def _mouse_motion(event):
        end_pos = event.pos[0] + event.rel[0], event.pos[1] + event.rel[1]
        Window._screen.mouse_motion_event(event.pos, end_pos, event.buttons)

    def event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Window.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Window._mouse_button_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                Window._mouse_button_up(event)
            elif event.type == pygame.MOUSEMOTION:
                Window._mouse_motion(event)
            elif event.type == pygame.KEYDOWN:
                Window._key_button_down(event)
            elif event.type == pygame.KEYDOWN:
                Window._key_button_up(event)

    def update(self):
        Window._clock.tick_busy_loop(Window.fps)
        Window._screen.draw(Window.window)
        pygame.display.flip()
        if not Window.running:
            pygame.quit()

    def quit():
        Window.running = False

# This class is for handling screen objects
class Screen:
    def __init__(self, background, init = Object.do_nothing):
        self.bg = background
        self.objects = []
        self.keyboard = KeyBoard()
        self.init = init
 
    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def set_background(self, background):
        self.bg = background

    def draw(self, window):
        bg = pygame.transform.scale(self.bg, window.get_size())
        window.blit(bg, (0, 0))
        for obj in self.objects:
            obj.draw(window)

    def mouse_down_event(self, event):
        for obj in self.objects:
            if obj.rect.collidepoint(event.pos):
                obj.mouse_down_event(event)

    def mouse_up_event(self, event):
        for obj in self.objects:
            if obj.rect.collidepoint(event.pos):
                obj.mouse_up_event(event)

    def mouse_motion_event(self, begin_pos, end_pos, buttons):
        for obj in self.objects:
            begin = obj.rect.collidepoint(begin_pos)
            end = obj.rect.collidepoint(end_pos)
            event = obj.mouse_motion_event((begin_pos, end_pos), buttons, (begin, end))

    def update(self):
        for obj in self.objects:
            obj.update()

class Signal:
    EVENT_NONE = 0
    EVENT_CLICK = 1
    EVENT_INTERRUPT = 2


