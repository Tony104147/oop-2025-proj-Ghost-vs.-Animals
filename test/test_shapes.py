#!usr/bin/env python3.10
# -*- coding utf-8 -*-

import add_path
from shapes import Circle, Rectangle, Triangle
import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

c1 = Circle(20, 40, white, 20)
r1 = Rectangle(50, 20, red, 50, 30)
t1 = Triangle(blue, [[0, 60], [40, 60], [20, 80]])

move_up = False
move_left = False
move_down= False
move_right = False

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_d:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_d:
                move_right = False

    # 更新移動
    if move_up:
        r1.move(dy=-5)
    if move_left:
        r1.move(dx=-5)
    if move_down:
        r1.move(dy=5)
    if move_right:
        r1.move(dx=5)
    
    # 更新畫面
    c1.draw(window)
    r1.draw(window)
    t1.draw(window)
    pygame.display.update()

pygame.quit()
