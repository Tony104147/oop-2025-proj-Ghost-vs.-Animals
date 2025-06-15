# -*- codinng utf-8 -*-

import os
import pygame

# Image management module for loading and accessing images in Pygame
IMAGES: dict[str, pygame.Surface] = dict()

# Load images from the 'images' directory relative to this file's location
def load_images():
    images = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images/')
    for file in os.listdir(images):
        if not file.endswith((".png", ".jpg", ".bmp")):
            continue

        image_name = file.split('.')[0].replace("_", " ")
        image = pygame.image.load(images + "/" + file).convert_alpha()
        IMAGES[image_name] = image

# Function to get an image by name
def GETIMAGE(name: str):
    return IMAGES[name]

# Function to set an image in the IMAGES dictionary
def SETIMAGE(name: str, value: pygame.Surface):
    IMAGES[name] = value
