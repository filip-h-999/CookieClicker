import pygame


class GUI:
    def __init__(self, window, path, shopBgPath, shopSize, shopFramePath, shopFrameSize, frameIcon, upgradeFramePath, upgradeSize):
        self.window = window
        self.black = 0, 0, 0
        self.BACK_WIDTH = 800 * 1.5
        self.BACK_HEIGHT = 600 * 1.5

        self.backgroundPath = path
        self.shopBgPath = shopBgPath
        self.shopSize = shopSize
        self.shopFramePath = shopFramePath
        self.upgradesFramePath = upgradeFramePath
        # backImage = pygame.image.load(r"assets/images/backgoundWood.png")
        self.back = pygame.transform.scale(path, (self.BACK_WIDTH, self.BACK_HEIGHT))
        # frameImage = pygame.image.load(r"assets/images/frame.png")
        self.shopBackground = pygame.transform.scale(shopBgPath, (shopSize))
        # shopImage = pygame.image.load(r"assets/images/shop.png")
        self.shopFrame = pygame.transform.scale(shopFramePath, (shopFrameSize))
        # frame2Image = pygame.image.load(r"assets/images/frame2.png")
        self.upgradeButtons = pygame.transform.scale(frameIcon, (500, 150))
        # upgradeFrameImage = pygame.image.load(r"assets/images/upgradesFrame.png")
        self.upgradeFrame = pygame.transform.scale(upgradeFramePath, (upgradeSize))

    def drawBackG(self):
        self.window.blit(self.back, (0, 0))

    def drawFrame(self, shopPoss, upgradePoss, shopFramePoss):
        self.shopPossition = shopPoss
        self.shopPossition = upgradePoss
        self.window.blit(self.shopBackground, (shopPoss))
        self.window.blit(self.shopFrame, (shopFramePoss))
        self.window.blit(self.upgradeButtons, (350, 80))
        self.window.blit(self.upgradeButtons, (350, 210))
        self.window.blit(self.upgradeButtons, (350, 340))
        self.window.blit(self.upgradeButtons, (350, 470))
        self.window.blit(self.upgradeFrame, (upgradePoss))
