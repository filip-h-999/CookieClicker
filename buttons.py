import pygame
from pygame.rect import Rect


class Button:

    def __init__(self, window, rect: Rect = None):
        self.window = window
        self.black = 0, 0, 0
        self.brightRed = 255, 0, 0
        buttonImage = pygame.image.load(r"assets\images\buttons.png")
        self.button1 = pygame.transform.scale(buttonImage, (250, 70))
        self.button2 = pygame.transform.scale(buttonImage, (270, 80))
        self.rect = rect

    def buttonClick(self, onButtonClick):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        on_button = self.rect.collidepoint(mouse)

        if on_button and click[0] == 1:
            onButtonClick()

    def drawButton(self):
        mouse = pygame.mouse.get_pos()

        on_button = self.rect.collidepoint(mouse)

        if on_button:
            pygame.draw.rect(self.window, self.brightRed, self.rect, 10)
            self.window.blit(self.button2, self.button2.get_rect(center=self.rect.center))
        else:
            pygame.draw.rect(self.window, self.black, self.rect, 10)
            self.window.blit(self.button1, self.button1.get_rect(center=self.rect.center))
