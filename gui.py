import pygame


class GUI:
    def __init__(self, window):
        self.window = window
        self.black = 0, 0, 0
        self.brightRed = 255, 0, 0
        self.BACK_WIDTH = 800 * 2
        self.BACK_HEIGHT = 600 * 2

        backImage = pygame.image.load(r"assets\images\b2.png")
        self.back = pygame.transform.scale(backImage, (self.BACK_WIDTH, self.BACK_HEIGHT))
        stone_image = pygame.image.load(r"assets\images\buttons.png")
        self.st = pygame.transform.scale(stone_image, (250, 70))
        self.st2 = pygame.transform.scale(stone_image, (270, 80))
        frameImage = pygame.image.load(r"assets\images\frame.png")
        self.frame = pygame.transform.scale(frameImage, (400, 600))
        shopImage = pygame.image.load(r"assets\images\shop.png")
        self.shop = pygame.transform.scale(shopImage, (300, 100))

    def drawBackG(self):
        self.window.blit(self.back, (0, 0))

    def drawFrame(self):
        self.window.blit(self.shop, (500, 10))
        self.window.blit(self.frame, (460, 60))

    def button(self, posY, onClick):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        rect = pygame.Rect(528, posY, 250, 70)
        on_button = rect.collidepoint(mouse)

        if on_button:
            pygame.draw.rect(self.window, self.brightRed, rect, 10)
            self.window.blit(self.st2, self.st2.get_rect(center=rect.center))
        else:
            pygame.draw.rect(self.window, self.black, rect, 10)
            self.window.blit(self.st, self.st.get_rect(center=rect.center))

        if on_button and click[0] == 1:
            onClick()
