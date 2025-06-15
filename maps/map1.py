# -*- coding utf-8 -*-

import random

import pygame

from maps import Map
from object import Object
from object.monsters import bat, frog
from lib.image import SETIMAGE
from lib.event import post, new
from lib.counter import Counter

SIZE  = 1600, 1200
IMAGE = 'map1'
surface = pygame.Surface((1, 1))
surface.fill((226, 143, 15))
SETIMAGE(IMAGE, surface)

def randpos(): return random.uniform(0, SIZE[0]), random.uniform(0, SIZE[1])

def INIT():
    bat1 = bat.Bat(randpos(), 'bat1')
    bat2 = bat.Bat(randpos(), 'bat2')
    frog1 = frog.Frog(randpos(), 'frog1')

    MAP.groups = {
        'MONSTERS': pygame.sprite.Group(bat1, bat2, frog1),
        'BLOCKS'  : pygame.sprite.Group(),
        'SKILLS'  : pygame.sprite.Group(),
    }

    # Create event types
    new('REBORN')
    new('SCORE')

def UPDATE(informations: dict[str, Object | dict[str, pygame.sprite.Group]]):
    monsters_reborn = []
    score = 0
    for monster in informations['GROUPS']['MONSTERS']:
        if monster['HP'] == 0:
            monster['HP'] = monster['MAX_HP']
            monster.kill()

            if random.uniform(0, monster['MAX_HP']) < 50.0:
                print(f"{monster['Name']} copied")
                monster_copy = type(monster)(randpos(), monster['Name'] + '2')
                monsters_reborn.append(monster_copy)
            monster['Name'] += '1'
            monsters_reborn.append(monster)

            score += (round(monster['HP'] / 50.0) - 1)
    
    for counter, monsters in REBORNQUEUE.items():
        if counter.ok():
            post('REBORN', {'monsters': monsters})
            del REBORNQUEUE[counter]
            counter.delete()
            break
    
    if len(monsters_reborn):
        counter = Counter(120)
        counter.reset()
        REBORNQUEUE[counter] = monsters_reborn
    
    if score:
        post('SCORE', {'value': score})

REBORNQUEUE = dict()
MAP = Map(size=SIZE, image=IMAGE, init=INIT, update=UPDATE)