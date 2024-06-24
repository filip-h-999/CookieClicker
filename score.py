import pygame
from pygame import font


class Score:
    def __init__(self, window, cookieFramePath):
        self.window = window
        self.black = 0, 0, 0
        self.cookieFrameImage = cookieFramePath
        # cookieFrameImage = pygame.image.load(r"assets/images/cookieCount.png")
        self.cookieFrame = pygame.transform.scale(cookieFramePath, (300, 100))

    def drawScore(self, score: int, poss):
        self.poss = poss
        self.window.blit(self.cookieFrame, (poss))
        font1 = font.SysFont('didot.ttc', 50)
        
        if score >= 1000000000:
            display_score = "{:.1f}bio".format(score / 1000000000)
        elif score >= 1000000:
            display_score = "{:.1f}mio".format(score / 1000000)
        elif score >= 1000:
            display_score = "{:.1f}k".format(score / 1000)
        else:
            display_score = str(score)
        
        gameScore = font1.render("Ck: " + display_score, True, self.black)
        self.window.blit(gameScore, (100, 40))
