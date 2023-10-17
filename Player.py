import pygame 

class Player:
    def __init__(self, x, y, img, l, h, health):
        self.x = x
        self.y = y
        self.img = img
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))
        self.health = health