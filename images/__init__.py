# -*- codinng utf-8 -*-

import os

import pygame

def load_images(func):
    IMAGES = dict()
    images = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    for file in os.listdir(images):
        if not file.endswith((".png", ".jpg", ".bmp")):
            continue

        image_name = file.split('.')[0].replace("_", " ")
        image = pygame.image.load(images + "/" + file)
        IMAGES[image_name] = image
    setattr(func, "IMAGES", IMAGES)
    
    return func

@load_images
def GETIMAGE(name: str):
    return GETIMAGE.IMAGES[name]