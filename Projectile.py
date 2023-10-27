import pygame 

class Projectile:
    def __init__(self, x, y, img, l ,h, dmg):
        self.x = x
        self.y = y
        self.img = img
        self.vel = 30
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))
        self.dmg = dmg

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))