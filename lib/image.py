# -*- codinng utf-8 -*-

import os
import pygame

IMAGES: dict[str, pygame.Surface] = dict()

def load_images():
    images = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images/')
    for file in os.listdir(images):
        if not file.endswith((".png", ".jpg", ".bmp")):
            continue

        image_name = file.split('.')[0].replace("_", " ")
        image = pygame.image.load(images + "/" + file).convert_alpha()
        IMAGES[image_name] = image
load_images()



def GETIMAGE(name: str):
    return IMAGES[name]

def SETIMAGE(name: str, value: pygame.Surface):
    IMAGES[name] = value