import pygame
from pygame.rect import Rect
# from cookie import Cookie


class Button:
    def __init__(self, window, imageFile: str, opacity, sizeX: int, sizeY: int,
                 hoverSizeX, hoverSizeY, rect: Rect = None):
        self.num_clickedInfo = 0
        self.num_clickedMute = 0
        self.num_clickedShop = 0
        # self.cookie = Cookie(window)
        self.window = window
        self.black = 0, 0, 0
        self.brightRed = 255, 0, 0
        img = pygame.image.load(imageFile)
        img.set_alpha(opacity)
        self.normalSize = pygame.transform.scale(img, (sizeX, sizeY))
        self.hoverSize = pygame.transform.scale(img, (hoverSizeX, hoverSizeY))
        self.rect = rect
        self.buttonSound = pygame.mixer.Sound("assets/sounds/buttonSound.wav")

    def buttonClick(self, onButtonClick, musicOnOff):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        on_button = self.rect.collidepoint(mouse)

        if on_button and click[0] == 1:
            onButtonClick()
            if musicOnOff == 1:
                pygame.mixer.Channel(6).play(pygame.mixer.Sound(self.buttonSound))
                pygame.mixer.Channel(6).set_volume(0.5)
            elif musicOnOff == 0:
                pygame.mixer.Channel(6).set_volume(0)

    def drawButton(self):
        mouse = pygame.mouse.get_pos()
        on_button = self.rect.collidepoint(mouse)

        if on_button:
            # pygame.draw.rect(self.window, self.brightRed, self.rect, 10)
            self.window.blit(self.hoverSize, self.hoverSize.get_rect(center=self.rect.center))
        else:
            # pygame.draw.rect(self.window, self.black, self.rect, 10)
            self.window.blit(self.normalSize, self.normalSize.get_rect(center=self.rect.center))
