#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import add_path
from square import Square
from timer import game_timer
import pygame
import random

backgroud_color = (255, 255, 255)

N = int(input("N: "))
pygame.init()

# 設定視窗
width, height = 540, 580
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("test")
# 設定背景
screen.fill(backgroud_color)

# 建立物件
buttons = []
button_size = width//N
button_size_nomergin = button_size-4
for i in range(N):
    for j in range(N):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        buttons.append(Square(i*button_size+2,
                              j*button_size+42,
                              button_size_nomergin,
                              button_size_nomergin,
                              color))

for obj in buttons:
    obj.draw(screen)
pygame.display.update()

endtime_font = pygame.font.SysFont("simhei", 36)
gamestate = 1
while gamestate > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamestate = 0
        elif 1 <= gamestate <= 2 and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for obj in buttons:
                if obj.x < pos[0] < obj.x+obj.width and obj.y < pos[1] < obj.y+obj.height:
                    if gamestate == 1:
                        gamestate = 2
                        timer = game_timer()
                    buttons.remove(obj)
                    if len(buttons) == 0:
                        gamestate = 3
                    break
        elif gamestate == 3 and event.type == pygame.KEYDOWN:
            gamestate = 0

    # 更新畫面
    if gamestate == 2:
        screen.fill(backgroud_color)
        for obj in buttons:
            obj.draw(screen)
        text = endtime_font.render(str(float(timer.end())/1000) + 's', False, (0, 0, 0))
        screen.blit(text, (0, 0))
        pygame.display.update()

# 結束
pygame.quit()
