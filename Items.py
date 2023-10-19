import pygame

class Items:
    def __init__(self, img, l, h, amount):
        self.img = img
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))
        self.amount = amount