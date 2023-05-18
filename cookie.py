import pygame
from pygame.mixer import Channel


def cookieSound():
    snowS = r"assets\sounds\cookieS.mp3"
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(snowS), maxtime=500)
    Channel(0).set_volume(0.2)


class Cookie:
    def __init__(self, window):
        self.window = window
        self.COOKIE_WIGHT = 330
        self.COOKIE_HEIGHT = 330
        self.black = 0, 0, 0
        # self.score = 0
        # self.increaseS = 1

        self.cookieImage = pygame.image.load(r"assets\images\cookie3.png")
        self.cookie = pygame.transform.scale(self.cookieImage, (self.COOKIE_WIGHT, self.COOKIE_HEIGHT))
        self.cookie2 = pygame.transform.scale(self.cookieImage, (self.COOKIE_WIGHT + 10, self.COOKIE_HEIGHT + 10))
        self.rect = pygame.Rect(31, 190, self.COOKIE_HEIGHT, self.COOKIE_WIGHT)
        self.collisionRect = self.rect.inflate(-90, -90)


    def drawCookie(self):
        self.window.blit(self.cookie, (31, 190))


    def drawBigCookies(self):
        self.window.blit(self.cookie2, self.cookie2.get_rect(center=self.collisionRect.center))


    # def increaseScore(self, n):
    #     self.score += n

    def clickCookie(self):
        cookieSound()
        # self.increaseScore(self.increaseS)


    def is_mouse_on_coockie(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.collisionRect.collidepoint(mouse_pos):
            return True
        else:
            return False