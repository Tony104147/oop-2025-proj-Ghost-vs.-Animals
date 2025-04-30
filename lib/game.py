# -*- coding utf-8 -*-

import pygame

class Game:
    def __init__(self, *,
                 fps = 120,
                 size = (800, 600),
                 title = '',
                 do_quit = None):
        self.fps = fps
        self.size = size
        self.title = title

        self.do_quit = do_quit

        self.run = True
    
    def loop(self):
        # Open a window and start the game
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()

        # Game loop
        while self.run:
            # Maintain fps
            clock.tick_busy_loop(self.fps)
            break
        
        # Do something before quiting the game
        if self.do_quit: self.do_quit()

        # Quit the game and close the window
        pygame.quit()