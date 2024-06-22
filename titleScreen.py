import pygame
from pygame.rect import Rect


class Title:
    def __init__(self, window):
        self.window = window
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 650

    def drawScreen(self):
        titleScreen = pygame.image.load(r"assets/images/titlescreen.jpg")
        self.window.blit(pygame.transform.scale(titleScreen, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)), (0, 0))

    def drawNextLvlScreen(self):
        ucs = pygame.image.load(r"assets\images\nextLvL.png")
        self.window.blit(pygame.transform.scale(ucs, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)), (0, 0))
