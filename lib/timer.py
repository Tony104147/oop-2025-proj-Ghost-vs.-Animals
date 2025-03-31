#!usr/bin.env python3
# -*- coding: utf-8 -*-

import pygame

class game_timer:
    def __init__(self):
        self.starttime = pygame.time.get_ticks()
        self._pausetime = 0
        self._pausepoint = 0
        self._pauseflag = False

    def get(self):
        if self.is_pause():
            endtime = self._pausepoint
        else:
            endtime = pygame.time.get_ticks()
        return endtime - self.starttime - self._pausetime

    def pause(self):
        if not self.is_pause():
            self._pausepoint = pygame.time.get_ticks()
            self._pauseflag = True

    def resume(self):
        if self.is_pause():
            self._pausetime += pygame.time.get_ticks() - self._pausepoint
            self._pauseflag = False

    def reset(self):
        self.__init__()

    def is_pause(self):
        return self._pauseflag
