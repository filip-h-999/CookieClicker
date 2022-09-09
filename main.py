import pygame
from cookie import Cookie
from gui import GUI
from score import Score
from buttons import Button


def main():
    pygame.init()
    running = True
    window = pygame.display.set_mode((1200, 650))
    cookie = Cookie(window)
    gui = GUI(window)
    score = Score(window)

    btn1 = Button(window, r"assets\images\Finger-buttons.png",
                  pygame.Rect(884, 145, 250, 70))
    btn2 = Button(window, r"assets\images\Grany-buttons.png",
                  pygame.Rect(884, 230, 250, 70))
    btn3 = Button(window, r"assets\images\Oven-buttons.png",
                  pygame.Rect(884, 315, 250, 70))
    btn4 = Button(window, r"assets\images\Factory-buttons.png",
                  pygame.Rect(884, 315 + 85, 250, 70))
    btn5 = Button(window, r"assets\images\Aliens-buttons.png",
                  pygame.Rect(884, 315 + 170, 250, 70))

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cookie.score >= 50:
                    btn1.buttonClick(onButton1Click)
                if cookie.score >= 500:
                    btn2.buttonClick(onButton2Click)
                if cookie.score >= 1500:
                    btn3.buttonClick(onButton3Click)
                if cookie.score >= 2500:
                    btn4.buttonClick(onButton4Click)
                if cookie.score >= 5000:
                    btn5.buttonClick(onButton5Click)
                cookie.clickCookie()

        window.blit(window, (0, 0))
        gui.drawBackG()
        cookie.drawCookie()
        gui.drawFrame()
        score.drawScore(cookie.score)

        btn1.drawButton()
        btn2.drawButton()
        btn3.drawButton()
        btn4.drawButton()
        btn5.drawButton()

        pygame.display.update()


if __name__ == '__main__':
    main()
