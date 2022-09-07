import pygame
from cookie import Cookie
from gui import GUI
from score import Score


def main():
    pygame.init()
    running = True
    window = pygame.display.set_mode((850, 650))
    cookie = Cookie(window)
    gui = GUI(window)
    score = Score(window)

    def onButton1Click():
        print("test")

    def onButton2Click():
        print("test2")

    def onButton3Click():
        print("test3")

    def onButton4Click():
        print("test4")

    def onButton5Click():
        print("test5")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(window, (0, 0))
        gui.drawBackG()
        cookie.drawCookie()
        gui.drawFrame()
        cookie.clickCookie()
        score.drawScore(cookie.score)

        gui.button(145, onButton1Click)
        gui.button(230, onButton2Click)
        gui.button(315, onButton3Click)
        gui.button(315 + 85, onButton4Click)
        gui.button(315 + 170, onButton5Click)

        pygame.display.update()


if __name__ == '__main__':
    main()
