import pygame
from pygame import mixer
from cookie import Cookie, cookieSound
from gui import GUI
from score import Score
from buttons import Button
from upgradeIcon import Image, Text


Ck_s = 0
ckClicked = False

gAmount = 0
oAmount = 0
fAmount = 0
aAmount = 0

#todo title screen(reset or play further)

def main():
    global gAmount, oAmount, fAmount, aAmount, ckClicked
    pygame.init()
    running = True
    window = pygame.display.set_mode((1200, 650))
    cookie = Cookie(window)
    gui = GUI(window)
    score = Score(window)
    GREEN = 0, 255, 0

    opacityF = 200
    opacityG = 200
    opacityO = 200
    opacityFa = 200
    opacityA = 200

    clock = pygame.time.Clock()
    timer_event = pygame.USEREVENT + 1

    InfoFrameImage = pygame.image.load(r"assets\images\info-Frame.png")
    infoFrame = pygame.transform.scale(InfoFrameImage, (500, 500))

    infoButton = Button(window, r"assets\buttons\info.png", 255, 30, 30, 40, 40, pygame.Rect(1150, 570, 30, 30))
    pauseMusic = Button(window, r"assets\images\mute.png", 255, 30, 30, 40, 40, pygame.Rect(10, 600, 30, 30))

    granny = Image(window, r"assets\upgrades\granny.png", 80, 80)
    oven = Image(window, r"assets\upgrades\oven.png", 80, 80)
    factory = Image(window, r"assets\upgrades\factory.png", 80, 80)
    alien = Image(window, r"assets\upgrades\alien.png", 80, 80)

    grannyAmount = Text(window, 50, "Amount: %d" % gAmount, GREEN)
    ovenAmount = Text(window, 50, "Amount: %d" % oAmount, GREEN)
    factoryAmount = Text(window, 50, "Amount: %d" % fAmount, GREEN)
    aliensAmount = Text(window, 50, "Amount: %d" % aAmount, GREEN)

    def music():
        backgroundMusic = r"assets\sounds\beat.mp3"
        mixer.music.load(backgroundMusic)
        mixer.music.set_volume(0.05)
        pygame.mixer.music.play(loops=100)
        # mixer.music.play()

    music()

    def onButtonFingerClick():
        cookie.score -= 50
        cookie.increaseS += 1

    def onButtonGrannyClick():
        global Ck_s, gAmount
        cookie.score -= 500
        pygame.time.set_timer(timer_event, 1000)
        gAmount += 1
        Ck_s += 10

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
        infoButton.num_clickedInfo += 1

    def onMuteClick():
        pauseMusic.num_clickedMute += 1

    while running:
        global Ck_s
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == timer_event:
                cookie.score += Ck_s
                cookieSound()

            if event.type == pygame.MOUSEBUTTONUP:
                if cookie.is_mouse_on_coockie():
                    ckClicked = True
                    cookie.clickCookie()

            if event.type == pygame.MOUSEBUTTONDOWN:
                ckClicked = False
                if cookie.score >= 50:
                    opacityF = 255
                    btn1.buttonClick(onButtonFingerClick)
                else:
                    opacityF = 200

                if cookie.score >= 500:
                    opacityG = 255
                    btn2.buttonClick(onButtonGrannyClick)
                else:
                    opacityG = 200

                if cookie.score >= 1500:
                    opacityO = 255
                    btn3.buttonClick(onButtonOvenClick)
                else:
                    opacityO = 200

                if cookie.score >= 2500:
                    opacityFa = 255
                    btn4.buttonClick(onButtonFactoryClick)
                else: 
                    opacityFa = 200

                if cookie.score >= 5000:
                    opacityA = 255
                    btn5.buttonClick(onButtonAliensClick)
                else:
                    opacityA = 200

                #todo comming out soon window
                
                infoButton.buttonClick(onInfoClick)
                pauseMusic.buttonClick(onMuteClick)

        window.blit(window, (0, 0))
        gui.drawBackG()
        gui.drawFrame()
        score.drawScore(cookie.score)

        if not ckClicked:
             cookie.drawCookie()
        else:
            cookie.drawBigCookies()

        granny.drawImage(430, 117)
        grannyAmount.text = "Amount: %d" % gAmount
        grannyAmount.drawText(520, 140)

        oven.drawImage(420, 245)
        ovenAmount.text = "Amount: %d" % oAmount
        ovenAmount.drawText(520, 270)

        factory.drawImage(425, 375)
        factoryAmount.text = "Amount: %d" % fAmount
        factoryAmount.drawText(520, 400)

        alien.drawImage(430, 515)
        aliensAmount.text = "Amount: %d" % aAmount
        aliensAmount.drawText(520, 530)

        if infoButton.num_clickedInfo % 2:
            window.blit(infoFrame, (340, 100))

        if pauseMusic.num_clickedMute % 2:
            mixer.music.pause()
        else:
            mixer.music.unpause()


        btn1 = Button(window, r"assets\buttons\Finger-buttons.png", opacityF, 250, 70, 270, 80, pygame.Rect(884, 145, 250, 70))
        btn2 = Button(window, r"assets\buttons\Granny-buttons.png", opacityG, 250, 70, 270, 80, pygame.Rect(884, 230, 250, 70))
        btn3 = Button(window, r"assets\buttons\Oven-buttons.png", opacityO, 250, 70, 270, 80, pygame.Rect(884, 315, 250, 70))
        btn4 = Button(window, r"assets\buttons\Factory-buttons.png", opacityFa, 250, 70, 270, 80, pygame.Rect(884, 315 + 85, 250, 70))
        btn5 = Button(window, r"assets\buttons\Aliens-buttons.png", opacityA, 250, 70, 270, 80, pygame.Rect(884, 315 + 170, 250, 70))
        
        btn1.drawButton()
        btn2.drawButton()
        btn3.drawButton()
        btn4.drawButton()
        btn5.drawButton()
        infoButton.drawButton()
        pauseMusic.drawButton()

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
