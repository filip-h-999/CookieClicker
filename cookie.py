import pygame
from pygame import mixer


def cookieSound(clickSound, text):
    # clickSoundCookie = r"assets/sounds/cookieS.mp3"
    # clickSoundBattery = r"assets/sounds/batteryS.mp3"
    if text == "on":
        mixer.music.load(clickSound)
        mixer.music.set_volume(0.2)
        mixer.music.play()
    else:
        mixer.music.stop()
    # pygame.mixer.Channel(0).play(pygame.mixer.Sound(clickSound), maxtime=300)
    # Channel(0).set_volume(0.2)


class Cookie:
    def __init__(self, window, imgPath, width, height):
        self.window = window
        self.COOKIE_WIGHT = width
        self.COOKIE_HEIGHT = height
        self.black = 0, 0, 0
        # self.score = 0
        # self.increaseS = 1

        self.cookieImage = imgPath
        self.cookie = pygame.transform.scale(imgPath, (self.COOKIE_WIGHT, self.COOKIE_HEIGHT))
        self.cookie2 = pygame.transform.scale(imgPath, (self.COOKIE_WIGHT + 10, self.COOKIE_HEIGHT + 10))
        self.rect = pygame.Rect(31, 190, self.COOKIE_HEIGHT, self.COOKIE_WIGHT)
        self.collisionRect = self.rect.inflate(-90, -90)


    def drawCookie(self, poss):
        self.poss = poss
        self.window.blit(self.cookie, (poss))


    def drawBigCookies(self):
        self.window.blit(self.cookie2, self.cookie2.get_rect(center=self.collisionRect.center))


    # def increaseScore(self, n):
    #     self.score += n

    def clickCookie(self, clickSound, text):
        cookieSound(clickSound, text)
        # self.increaseScore(self.increaseS)


    def is_mouse_on_coockie(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.collisionRect.collidepoint(mouse_pos):
            return True
        else:
            return False