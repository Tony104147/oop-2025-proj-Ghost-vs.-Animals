#!usr/bin.env python3
# -*- coding: utf-8 -*-

import pygame

class game_timer:
    def __init__(self):
        self.starttime = pygame.time.get_ticks()
        self.__pausetime = 0
        self.__pausepoint = 0
        self.__pauseflag = False

    def get(self):
        if self.is_pause():
            endtime = self.__pausepoint
        else:
            endtime = pygame.time.get_ticks()
        return endtime - self.starttime - self.__pausetime

    def pause(self):
        if not self.is_pause():
            self.__pausepoint = pygame.time.get_ticks()
            self.__pauseflag = True

    def resume(self):
        if self.is_pause():
            self.__pausetime += pygame.time.get_ticks() - self.__pausepoint
            self.__pauseflag = False

    def is_pause(self):
        return self.__pauseflag
