import pygame
import json
import os
from pygame.mixer import Channel
from cookie import Cookie, cookieSound
from gui import GUI
from score import Score
from buttons import Button
from upgradeIcon import Image, Text
from titleScreen import Title
from playtime import PlaytimeDisplay


def main():
    global started
    running = True
    ckClicked = False
    update = False

    stats = {
        "Ck_s" : 0,
        "cookies" : 0,
        "fingers" : 1,
        "gAmount": 0,
        "oAmount": 0,
        "fAmount": 0,
        "aAmount": 0,
        "event" : 0,
        "win" : 0,
        "playtime": 0
    }

    pygame.init()
    window = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Cookie Clicker")
    GREEN = 0, 255, 0

    cookie = Cookie(window)
    gui = GUI(window)
    score = Score(window)
    titleScreen = Title(window)
    playtime = PlaytimeDisplay(window)

    opacityF = 200
    opacityG = 200
    opacityO = 200
    opacityFa = 200
    opacityA = 200

    started = False

    clock = pygame.time.Clock()
    timer_event = pygame.USEREVENT + 1

    InfoFrameImage = pygame.image.load(r"assets/images/info-Frame.png")
    infoFrame = pygame.transform.scale(InfoFrameImage, (500, 500))

    infoButton = Button(window, r"assets/buttons/info.png", 255, 30, 30, 40, 40, pygame.Rect(1150, 570, 30, 30))
    pauseMusic = Button(window, r"assets/images/mute.png", 255, 30, 30, 40, 40, pygame.Rect(10, 600, 30, 30))

    granny = Image(window, r"assets/upgrades/granny.png", 80, 80)
    oven = Image(window, r"assets/upgrades/oven.png", 80, 80)
    factory = Image(window, r"assets/upgrades/factory.png", 80, 80)
    alien = Image(window, r"assets/upgrades/alien.png", 80, 80)

    grannyAmount = Text(window, 50, "Amount: %d" % stats["gAmount"], GREEN)
    ovenAmount = Text(window, 50, "Amount: %d" % stats["oAmount"], GREEN)
    factoryAmount = Text(window, 50, "Amount: %d" % stats["fAmount"], GREEN)
    aliensAmount = Text(window, 50, "Amount: %d" % stats["aAmount"], GREEN)

    if os.path.exists("statsDic.json"):
        with open("statsDic.json", "r") as file:
            stats = json.load(file)
    
    def music():
        backgroundMusic = r"assets/sounds/beat.mp3"
        # mixer.music.load(backgroundMusic)
        # mixer.music.set_volume(0.05)
        # pygame.mixer.music.play(loops=100)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(backgroundMusic), loops=-1)
        Channel(1).set_volume(0.1)
        # mixer.music.play()

    def reset():
        global started
        stats["Ck_s"] = 0
        stats["cookies"] = 0
        stats["fingers"] = 1
        stats["gAmount"] = 0
        stats["oAmount"] = 0
        stats["fAmount"] = 0
        stats["aAmount"] = 0
        stats["event"] = 0
        stats["win"] = 0
        started = True
        stats["playtime"] = 0

    def onButtonFingerClick():
        stats["cookies"] -= 50
        stats["fingers"] += 1
        # cookie.increaseS = stats["fingers"]
        stats["fingers"] += 1

    def onButtonGrannyClick():
        stats["cookies"] -= 500
        pygame.time.set_timer(timer_event, 1000)
        stats["gAmount"] += 1
        stats["Ck_s"] += 10
        stats["event"] = 1

    def onButtonOvenClick():
        stats["cookies"] -= 2000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 20
        stats["oAmount"] += 1


    def onButtonFactoryClick():
        stats["cookies"] -= 10000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 100
        stats["fAmount"] += 1

    def onButtonAliensClick():
        stats["cookies"] -= 50000
        pygame.time.set_timer(timer_event, 1000)
        stats["Ck_s"] += 500
        stats["aAmount"] += 1

    def onInfoClick():
        infoButton.num_clickedInfo += 1

    def onMuteClick():
        pauseMusic.num_clickedMute += 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("statsDic.json", "w") as file:
                        json.dump(stats, file)
                running = False

            if event.type == timer_event:
                stats["cookies"] += stats["Ck_s"]
                cookieSound()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    started = True
                    music()

                    if stats["event"] == 1:
                        pygame.time.set_timer(timer_event, 1000)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                    music()
                    with open("statsDic.json", "w") as file:
                        json.dump(stats, file)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    update = False
                    stats["cookies"] += 1
                    stats["win"] = 1
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)


            if event.type == pygame.MOUSEBUTTONUP:
                if cookie.is_mouse_on_coockie():
                    ckClicked = True
                    cookie.clickCookie()
                    stats["cookies"] += stats["fingers"]

            if event.type == pygame.MOUSEBUTTONDOWN:
                ckClicked = False
                if stats["cookies"] >= 50:
                    opacityF = 255
                    f_btn.buttonClick(onButtonFingerClick)
                else:
                    opacityF = 200

                if stats["cookies"] >= 500:
                    opacityG = 255
                    g_btn.buttonClick(onButtonGrannyClick)
                else:
                    opacityG = 200

                if stats["cookies"] >= 2000:
                    opacityO = 255
                    o_btn.buttonClick(onButtonOvenClick)
                else:
                    opacityO = 200

                if stats["cookies"] >= 10000:
                    opacityFa = 255
                    fa_btn.buttonClick(onButtonFactoryClick)
                else: 
                    opacityFa = 200

                if stats["cookies"] >= 50000:
                    opacityA = 255
                    a_btn.buttonClick(onButtonAliensClick)
                else:
                    opacityA = 200
                
                if stats["cookies"] >= 100000:
                    update = True
                
                infoButton.buttonClick(onInfoClick)
                pauseMusic.buttonClick(onMuteClick)

        if not started:
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
            titleScreen.drawScreen()

        if started:
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            window.blit(window, (0, 0))
            stats["playtime"] += playtime.ticks
            playtime.run(stats["playtime"])
            gui.drawBackG()
            gui.drawFrame()
            score.drawScore(stats["cookies"])


            if not ckClicked:
                cookie.drawCookie()
            else:
                cookie.drawBigCookies()

            granny.drawImage(430, 117)
            grannyAmount.text = "Amount: %d" % stats["gAmount"]
            grannyAmount.drawText(520, 140)

            oven.drawImage(420, 245)
            ovenAmount.text = "Amount: %d" % stats["oAmount"]
            ovenAmount.drawText(520, 270)

            factory.drawImage(425, 375)
            factoryAmount.text = "Amount: %d" % stats["fAmount"]
            factoryAmount.drawText(520, 400)

            alien.drawImage(430, 515)
            aliensAmount.text = "Amount: %d" % stats["aAmount"]
            aliensAmount.drawText(520, 530)

            if infoButton.num_clickedInfo % 2:
                window.blit(infoFrame, (340, 100))

            if pauseMusic.num_clickedMute % 2:
                Channel(1).pause()
            else:
                Channel(1).unpause()


            f_btn = Button(window, r"assets/buttons/Finger-buttons.png", opacityF, 125, 70, 140, 80, pygame.Rect(870, 145, 140, 70))
            g_btn = Button(window, r"assets/buttons/Granny-buttons.png", opacityG, 125, 70, 140, 80, pygame.Rect(1005, 145, 140, 70))
            o_btn = Button(window, r"assets/buttons/Oven-buttons.png", opacityO, 125, 70, 140, 80, pygame.Rect(870, 230, 140, 70))
            fam_btn = Button(window, r"assets/buttons/Farm-buttons.png", opacityO, 125, 70, 140, 80, pygame.Rect(1005, 230, 140, 70))
            fa_btn = Button(window, r"assets/buttons/Factory-buttons.png", opacityFa, 125, 70, 140, 80, pygame.Rect(870, 315, 140, 70))
            b_btn = Button(window, r"assets/buttons/Bank-buttons.png", opacityA, 125, 70, 140, 80, pygame.Rect(1005, 315, 140, 70))
            a_btn = Button(window, r"assets/buttons/Aliens-buttons.png", opacityA, 125, 70, 140, 80, pygame.Rect(870, 400, 140, 70))
            t_btn = Button(window, r"assets/buttons/Tesla-buttons.png", opacityA, 125, 70, 140, 80, pygame.Rect(1005, 400, 140, 70))
            r_btn = Button(window, r"assets/buttons/Rocket-buttons.png", opacityA, 125, 70, 140, 80, pygame.Rect(870, 485, 140, 70))
            e_btn = Button(window, r"assets/buttons/Elon-buttons.png", opacityA, 125, 70, 140, 80, pygame.Rect(1005, 485, 140, 70))


            f_btn.drawButton()
            g_btn.drawButton()
            o_btn.drawButton()
            fam_btn.drawButton()
            fa_btn.drawButton()
            b_btn.drawButton()
            a_btn.drawButton()
            t_btn.drawButton()
            r_btn.drawButton()
            e_btn.drawButton()
            infoButton.drawButton()
            pauseMusic.drawButton()

            if update and stats["win"] != 1 and stats["cookies"] >= 500000:
                titleScreen.drawUpdateCommingSoon()
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
