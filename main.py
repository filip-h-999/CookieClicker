import pygame
from pygame import mixer
from cookie import Cookie
from gui import GUI
from score import Score
from buttons import Button
from upgradeIcon import Image, Text

Ck_s = 0
gAmount = 0
oAmount = 0
fAmount = 0
aAmount = 0


def main():
    global gAmount, oAmount, fAmount, aAmount
    pygame.init()
    running = True
    window = pygame.display.set_mode((1200, 650))
    cookie = Cookie(window)
    gui = GUI(window)
    score = Score(window)
    GREEN = 0, 255, 0

    clock = pygame.time.Clock()
    timer_event = pygame.USEREVENT + 1

    InfoFrameImage = pygame.image.load(r"assets\images\info-Frame.png")
    infoFrame = pygame.transform.scale(InfoFrameImage, (500, 500))

    btn1 = Button(window, r"assets\buttons\Finger-buttons.png", 250, 70, 270, 80,
                  pygame.Rect(884, 145, 250, 70))
    btn2 = Button(window, r"assets\buttons\Grany-buttons.png", 250, 70, 270, 80,
                  pygame.Rect(884, 230, 250, 70))
    btn3 = Button(window, r"assets\buttons\Oven-buttons.png", 250, 70, 270, 80,
                  pygame.Rect(884, 315, 250, 70))
    btn4 = Button(window, r"assets\buttons\Factory-buttons.png", 250, 70, 270, 80,
                  pygame.Rect(884, 315 + 85, 250, 70))
    btn5 = Button(window, r"assets\buttons\Aliens-buttons.png", 250, 70, 270, 80,
                  pygame.Rect(884, 315 + 170, 250, 70))
    infoButton = Button(window, r"assets\buttons\info.png", 30, 30, 40, 40,
                        pygame.Rect(1150, 570, 30, 30))

    grany = Image(window, r"assets\upgreades\grany.png", 80, 80)
    oven = Image(window, r"assets\upgreades\oven.png", 80, 80)
    factory = Image(window, r"assets\upgreades\factory.png", 80, 80)
    alien = Image(window, r"assets\upgreades\alien.png", 80, 80)

    granyAmount = Text(window, 50, "Amount: %d" % gAmount, GREEN)
    ovenAmount = Text(window, 50, "Amount: %d" % oAmount, GREEN)
    factoryAmount = Text(window, 50, "Amount: %d" % fAmount, GREEN)
    aliensAmount = Text(window, 50, "Amount: %d" % aAmount, GREEN)

    def music():
        backgroundMusic = r"assets\sounds\beat.mp3"
        mixer.music.load(backgroundMusic)
        mixer.music.set_volume(0.05)
        mixer.music.play()

    music()

    def onButtonFingerClick():
        cookie.score -= 50
        cookie.increaseS += 1

    def onButtonGranyClick():
        global Ck_s, gAmount
        cookie.score -= 500
        pygame.time.set_timer(timer_event, 1000)
        gAmount += 1
        Ck_s += 10
        print(gAmount)

    def onButtonOvenClick():
        global Ck_s, oAmount
        cookie.score -= 1500
        Ck_s += 15
        oAmount += 1

    def onButtonFactoryClick():
        global Ck_s, fAmount
        cookie.score -= 2500
        Ck_s += 20
        fAmount += 1

    def onButtonAliensClick():
        global Ck_s, aAmount
        cookie.score -= 5000
        Ck_s += 40
        aAmount += 1

    def onInfoClick():
        infoButton.num_clicked += 1

    while running:
        global Ck_s
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == timer_event:
                cookie.score += Ck_s

            if event.type == pygame.MOUSEBUTTONDOWN:
                if cookie.score >= 50:
                    btn1.buttonClick(onButtonFingerClick)
                if cookie.score >= -500:
                    btn2.buttonClick(onButtonGranyClick)
                if cookie.score >= 1500:
                    btn3.buttonClick(onButtonOvenClick)
                if cookie.score >= 2500:
                    btn4.buttonClick(onButtonFactoryClick)
                if cookie.score >= 5000:
                    btn5.buttonClick(onButtonAliensClick)
                cookie.clickCookie()
                infoButton.buttonClick(onInfoClick)

        window.blit(window, (0, 0))
        gui.drawBackG()
        cookie.drawCookie()
        gui.drawFrame()
        score.drawScore(cookie.score)

        grany.drawImage(430, 117)
        granyAmount.text = "Amount: %d" % gAmount
        granyAmount.drawText(520, 140)

        oven.drawImage(420, 245)
        ovenAmount.text = "Amount: %d" % oAmount
        ovenAmount.drawText(520, 270)

        factory.drawImage(425, 375)
        factoryAmount.text = "Amount: %d" % fAmount
        factoryAmount.drawText(520, 400)

        alien.drawImage(430, 515)
        aliensAmount.text = "Amount: %d" % aAmount
        aliensAmount.drawText(520, 530)

        if infoButton.num_clicked % 2:
            window.blit(infoFrame, (340, 100))

        btn1.drawButton()
        btn2.drawButton()
        btn3.drawButton()
        btn4.drawButton()
        btn5.drawButton()
        infoButton.drawButton()

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
