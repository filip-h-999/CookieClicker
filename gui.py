import pygame


class GUI:
    def __init__(self, window, path, shopBgPath, shopSize, shopFramePath, frameIcon, upgradeFramePath, posXY):
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
        self.frame = pygame.transform.scale(shopBgPath, (shopSize))
        # shopImage = pygame.image.load(r"assets/images/shop.png")
        self.shop = pygame.transform.scale(shopFramePath, (300, 100))
        # frame2Image = pygame.image.load(r"assets/images/frame2.png")
        self.frame2 = pygame.transform.scale(frameIcon, (500, 150))
        # upgradeFrameImage = pygame.image.load(r"assets/images/upgradesFrame.png")
        self.upgradeFrame = pygame.transform.scale(upgradeFramePath, (posXY))

    def drawBackG(self):
        self.window.blit(self.back, (0, 0))

    def drawFrame(self, shopPoss, upgradePoss):
        self.shopPossition = shopPoss
        self.shopPossition = upgradePoss
        self.window.blit(self.frame, (shopPoss))
        self.window.blit(self.shop, (850, 10))
        self.window.blit(self.frame2, (350, 80))
        self.window.blit(self.frame2, (350, 210))
        self.window.blit(self.frame2, (350, 340))
        self.window.blit(self.frame2, (350, 470))
        self.window.blit(self.upgradeFrame, (upgradePoss))
