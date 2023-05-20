import pygame


class GUI:
    def __init__(self, window):
        self.window = window
        self.black = 0, 0, 0
        self.BACK_WIDTH = 800 * 1.5
        self.BACK_HEIGHT = 600 * 1.5

        backImage = pygame.image.load(r"assets\images\b2.png")
        self.back = pygame.transform.scale(backImage, (self.BACK_WIDTH, self.BACK_HEIGHT))
        frameImage = pygame.image.load(r"assets\images\frame.png")
        self.frame = pygame.transform.scale(frameImage, (400, 600))
        shopImage = pygame.image.load(r"assets\images\shop.png")
        self.shop = pygame.transform.scale(shopImage, (300, 100))
        frame2Image = pygame.image.load(r"assets\images\frame2.png")
        self.frame2 = pygame.transform.scale(frame2Image, (500, 150))
        upgradeFrameImage = pygame.image.load(r"assets\images\upgradesFrame.png")
        self.upgradeFrame = pygame.transform.scale(upgradeFrameImage, (300, 100))

    def drawBackG(self):
        self.window.blit(self.back, (0, 0))

    def drawFrame(self):
        self.window.blit(self.shop, (850, 10))
        self.window.blit(self.frame, (815, 60))
        self.window.blit(self.frame2, (350, 80))
        self.window.blit(self.frame2, (350, 210))
        self.window.blit(self.frame2, (350, 340))
        self.window.blit(self.frame2, (350, 470))
        self.window.blit(self.upgradeFrame, (442, 10))
