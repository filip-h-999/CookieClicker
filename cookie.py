import pygame


class Cookie:
    def __init__(self, window):
        self.window = window
        self.COOKIE_WIGHT = 350
        self.COOKIE_HEIGHT = 350
        self.black = 0, 0, 0
        self.score = 0

        self.cookieImage = pygame.image.load(r"assets\images\cookie3.png")
        self.cookie = pygame.transform.scale(self.cookieImage, (self.COOKIE_WIGHT, self.COOKIE_HEIGHT))
        self.cookie2 = pygame.transform.scale(self.cookieImage, (self.COOKIE_WIGHT + 10, self.COOKIE_HEIGHT + 10))
        self.rect = pygame.Rect(31, 150, self.COOKIE_HEIGHT, self.COOKIE_WIGHT)
        self.collisionRect = self.rect.inflate(-90, -90)

    def drawCookie(self):
        self.window.blit(self.cookie, (31, 150))

    def increaseScore(self):
        self.score += 1

    def clickCookie(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        on_button = self.collisionRect.collidepoint(mouse)
        # pygame.draw.rect(self.window, self.black, self.collisionRect, 10)

        if on_button and click[0] == 1:
            # self.cookie = pygame.transform.scale(self.cookieImage, (self.COOKIE_WIGHT+15, self.COOKIE_HEIGHT+15))
            self.window.blit(self.cookie2, self.cookie2.get_rect(center=self.collisionRect.center))
            self.increaseScore()
            # print(self.score)
