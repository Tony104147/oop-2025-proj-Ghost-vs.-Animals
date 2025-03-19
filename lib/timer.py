#!usr/bin.env python3
# -*- coding: utf-8 -*-

import pygame

class game_timer:
    def __init__(self):
        self.starttime = pygame.time.get_ticks()
        self.endtime = 0
        self.__pausetime = 0
        self.__pausepoint = 0

    def end(self):
        self.endtime = pygame.time.get_ticks()
        return self.endtime - self.starttime - self.__pausetime

    def pause(self):
        if self.__pausepoint == 0:
            self.__pausepoint = pygame.time.get_ticks()

    def resume(self):
        if self.__pausepoint != 0:
            self.__pausetime += pygame.time.get_ticks() - self.__pausepoint
            self.__pausepoint = 0
