import pygame 

class Projectile:
    def __init__(self, x, y, img, l , h):
        self.x = x
        self.y = y
        self.img = img
        self.vel = 5
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))