#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import add_path
from lib.square import Square
import pygame
import random

backgroud_color = (255, 255, 255)

N = int(input("N: "))
pygame.init()

# 設定視窗
width, height = 540, 540
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("test")
# 設定背景
screen.fill(backgroud_color)

# 建立物件
buttons = []
button_size = width//N
button_size_nomergin = button_size-4
for i in range(10):
    for j in range(10):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        buttons.append(Square(i*button_size+2,
                              j*button_size+2,
                              button_size_nomergin,
                              button_size_nomergin,
                              color))

# 更新畫面
for obj in buttons:
    obj.draw(screen)
pygame.display.update()

count = N**2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for obj in buttons:
                if obj.x < pos[0] < obj.x+obj.width and obj.y < pos[1] < obj.y+obj.height:
                    if obj.color is not backgroud_color:
                        count -= 1
                        obj.color = backgroud_color
                    obj.draw(screen)
                    pygame.display.update()
                    break
    if count == 0:
        running = False

print("end")
endtime = pygame.time.get_ticks()
endtime_font = pygame.font.SysFont("simhei", 36)
text = endtime_font.render(str(float(endtime)/1000) + 's', True, (0, 0, 0))
screen.blit(text, (0, 0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            pygame.quit()
pygame.quit()
