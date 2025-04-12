#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import add_path
import pygame

from window import Window
from start_menu import StartMenu
from setting_page import SettingPage
from start_village import StartVillage
from character import Character

SIZE = (800, 600)
window = Window(SIZE)

ch = Character()
START_MENU = StartMenu(SIZE)
SETTING_PAGE = SettingPage(SIZE)
START_VILLAGE = StartVillage(SIZE)

Window.add_screen("start_menu", StartMenu.screen)
Window.add_screen("setting_page", SettingPage.screen)
Window.add_screen("start_village", StartVillage.screen)

Window.set_screen("start_menu")
# Window.set_screen("setting_page")

while window.running:
    window.event_handle()
    window.update()
