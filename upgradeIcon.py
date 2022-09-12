import pygame
from pygame import font


class Image:
    def __init__(self, window, imageFile, sizeX, sizeY):
        self.window = window
        img = pygame.image.load(imageFile)
        self.image = pygame.transform.scale(img, (sizeX, sizeY))

    def drawImage(self, posX, posY):
        self.window.blit(self.image, (posX, posY))


class Text:
    def __init__(self, window, size, text, color):
        self.color = color
        self.window = window
        self.font1 = font.SysFont('didot.ttc', size)
        self.text = text

    def drawText(self, posX, posY):
        self.window.blit(self.font1.render(self.text, True, self.color), (posX, posY))
