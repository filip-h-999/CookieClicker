import pygame
from pygame import font


class Score:
    def __init__(self, window):
        self.window = window
        self.black = 0, 0, 0
        cookieFrameImage = pygame.image.load(r"assets\images\cookieCount.png")
        self.cookieFrame = pygame.transform.scale(cookieFrameImage, (300, 100))

    def drawScore(self, score: int):
        self.window.blit(self.cookieFrame, (60, 10))
        font1 = font.SysFont('didot.ttc', 50)
        gameScore = font1.render("Cookies: %d" % score, True, self.black)
        self.window.blit(gameScore, (100, 40))
