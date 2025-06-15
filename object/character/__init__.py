# -*- coding utf-8 -*-

import pygame

from object import Object

class Character(Object):
    ''''''
    def __init__(self, *,
                 rect = (0, 0, 0, 0),
                 image: str | None = None,
                 Name = "character",
                 MAX_HP = 100.0,
                 HP = 100.0,
                 ATK = 10.0,
                 DEF = 10.0,
                 speed = 3):
        super().__init__(rect=rect, image=image)

        # Character datas
        self.Name = Name
        self.MAX_HP = MAX_HP
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.speed = speed

    def attacked(self, value):
        self["HP"] = max(self["HP"] - value * (1 - self["DEF"] / (100 + self["DEF"])), 0)
    
    def heal(self, value):
        self["HP"] = min(self["HP"] + value, self["MAX_HP"])
    
    def move(self,
             offset: tuple[int | float],
             blocks_group: pygame.sprite.Group = None,
             restriction: pygame.Rect = None):
        # Move
        original_pos = self.rect.topleft
        dx, dy = offset
        self.rect.move_ip(dx, dy)

        # Clamp character into restriction
        if restriction:
            self.rect.clamp_ip(restriction)

        # Back to the original position if being blocked
        if blocks_group and pygame.sprite.spritecollideany(self, blocks_group):
            self.rect.topleft = original_pos
            return False
        return True
