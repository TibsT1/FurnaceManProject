import pygame

class Enemies:
    def __init__(self, x, y, img, l, h, health, vel):
        self.x = x
        self.y = y
        self.img = img
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))
        self.health = health
        self.vel = vel

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))