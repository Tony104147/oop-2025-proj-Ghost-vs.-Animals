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
    clock = None
    screen = None
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
        Window.clock = pygame.time.Clock()
        Window.screen = Screen(size, pygame.Surface(size))
        Window.screens['_'] = Window.screen

    def set_screen(screen_name):
        if Window.screen_log[-1] != screen_name:
            Window.screen = Window.screens[screen_name]
            Window.screen.init()
            Window.screen_log.append(screen_name)
        print(Window.screen_log)

    def back_screen():
        if len(Window.screen_log) > 1:
            Window.screen_log.pop()
            Window.screen = Window.screens[Window.screen_log[-1]]
            Window.screen.init()
        print(Window.screen_log)

    def add_screen(screen_name, screen):
        Window.screens[screen_name] = screen

    def _mouse_button_down(event):
        Window.screen.mouse_down_event(event.pos, event.button)

    def _mouse_button_up(event):
        Window.screen.mouse_up_event(event.pos, event.button)

    def _key_button_down(event):
        Window.screen.keyboard.key_press(event.key, event.mod)

    def _key_button_up(event):
        Window.screen.keyboard.key_release(event.key, event.mod)

    def _mouse_motion(event):
        end_pos = event.pos[0] + event.rel[0], event.pos[1] + event.rel[1]
        Window.screen.mouse_motion_event((event.pos, end_pos), event.buttons, (True, True))

    def event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Window.running = False
            else:
                event_id, args = None, None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    event_id, args = pygame.MOUSEBUTTONDOWN, (event.pos, event.button)
                elif event.type == pygame.MOUSEBUTTONUP:
                    event_id, args = pygame.MOUSEBUTTONUP, (event.pos, event.button)
                elif event.type == pygame.MOUSEMOTION:
                    event_id, args = pygame.MOUSEMOTION, (event.pos, event.rel, event.buttons)
                elif event.type == pygame.KEYDOWN:
                    event_id, args = pygame.KEYDOWN, (event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    event_id, args = pygame.KEYUP, (event.key, event.mod)

                self.screen.event.react(event_id, args)

    def update(self):
        Window.screen.update()
        Window.screen.draw(Window.window)
        pygame.display.flip()
        Window.clock.tick_busy_loop(Window.fps)

    def quit():
        Window.running = False

# This class is for handling screen objects
class Screen(Box):
    def __init__(self, size, background, character = None):
        super().__init__((0, 0, *size))
        self.texture = background
        self.keyboard = KeyBoard()
        self.entities = []
        self.character = character

    def init(self):
        pass
 
class Signal:
    EVENT_NONE = 0
    EVENT_CLICK = 1
    EVENT_INTERRUPT = 2


