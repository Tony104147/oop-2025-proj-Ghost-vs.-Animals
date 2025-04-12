#!python3.10
# -*- coding utf-8 -*-

import pygame
from objects import Object, Box
from keyboard import KeyBoard

class Window:
    window = None

    # vars
    fps = None
    volume = 100
    _clock = None
    _screen = None
    screens = {}
    screen_log = ['_']

    # flags
    running = True

    def __init__(self,
                 size,
                 fps = 60,
                 title = '',
                 flags = 0):
        pygame.init()
        Window.window = pygame.display.set_mode(size, flags)
        pygame.display.set_caption(title)

        # const vars

        # vars
        Window.fps = fps
        Window._clock = pygame.time.Clock()
        Window._screen = Screen(size, pygame.Surface(size))
        Window.screens['_'] = Window._screen

    def set_screen(screen_name):
        if Window.screen_log[-1] != screen_name:
            Window._screen = Window.screens[screen_name]
            Window._screen.init()
            Window.screen_log.append(screen_name)
        print(Window.screen_log)

    def back_screen():
        if len(Window.screen_log) > 1:
            Window.screen_log.pop()
            Window._screen = Window.screens[Window.screen_log[-1]]
            Window._screen.init()
        print(Window.screen_log)

    def add_screen(screen_name, screen):
        Window.screens[screen_name] = screen

    def _mouse_button_down(event):
        Window._screen.mouse_down_event(event.pos, event.button)

    def _mouse_button_up(event):
        Window._screen.mouse_up_event(event.pos, event.button)

    def _key_button_down(event):
        Window._screen.keyboard.key_press(event.key, event.mod)

    def _key_button_up(event):
        Window._screen.keyboard.key_release(event.key, event.mod)

    def _mouse_motion(event):
        end_pos = event.pos[0] + event.rel[0], event.pos[1] + event.rel[1]
        Window._screen.mouse_motion_event((event.pos, end_pos), event.buttons, (True, True))

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
        Window._screen.update()
        Window._screen.draw(Window.window)
        pygame.display.flip()
        if not Window.running:
            pygame.quit()

    def quit():
        Window.running = False

# This class is for handling screen objects
class Screen(Box):
    def __init__(self, size, background, init = Object.do_nothing):
        super().__init__((0, 0, *size), background)
        self.keyboard = KeyBoard()
        self.init = init
 
class Signal:
    EVENT_NONE = 0
    EVENT_CLICK = 1
    EVENT_INTERRUPT = 2


