#!usr/bin/env python3.10
# -*- coding: utf-8 -*-

import add_path
from label import Label
import pygame

def test_label(screen):
    label1 = Label(100, 100, 20, 'Hello, world!', (0, 0, 0), (150, 150, 150))
    label1.draw(screen)
    label1.move(label1.x, label1.y + label1.height)
    pygame.display.update()

    text = input('Enter a new text: ')
    label1.set_text(text)
    label1.set_font_size(40)
    label1.set_font_color((255, 255, 255))
    label1.set_backgroud_color(None)
    label1.draw(screen)
    label1.move(label1.x, label1.y + label1.height)
    pygame.display.update()
    pygame.time.wait(2000)

    label1.set_text('Goodbye, world!')
    label1.set_font_color((255, 0, 0))
    label1.set_font_size(30)
    label1.set_backgroud_color((0, 255, 0))
    label1.draw(screen)
    pygame.display.update()
    pygame.time.wait(2000)

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    screen.fill((0, 0, 0))
    label2 = pygame.font.Font(None, 40).render('Press SPACE to test Label', True, (255, 255, 255))
    screen.blit(label2, (300, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                test_label(screen)
    pygame.display.update()
pygame.quit()
