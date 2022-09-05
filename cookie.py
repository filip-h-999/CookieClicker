import pygame


class Cookie:
    def __init__(self, window):
        self.window = window
        self.COOKIE_WIGHT = 350
        self.COOKIE_HEIGHT = 350
        self.cookieImage = pygame.image.load(r"assets\images\cookie3.png")
        self.cookie = pygame.transform.scale(self.cookieImage, (self.COOKIE_WIGHT, self.COOKIE_HEIGHT))

    def drawCookie(self):
        self.window.blit(self.cookie, (31, 150))
